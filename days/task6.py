from collections import Counter
from statistics import median_high

from AOCDay import AOCDay


class Day6(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 6
        self.input_link = self.input_link.format(day=self.day)
        self.input_data = self.download_input(self.input_link)

    @staticmethod
    def read_points(data):
        points = []
        for line in data:
            point = tuple(int(i) for i in line.split(','))
            points.append(point)
        return points

    @staticmethod
    def eval_area(points):
        left = min([p[0] for p in points])
        right = max([p[0] for p in points])
        down = min([p[1] for p in points])
        top = max([p[1] for p in points])
        return {'left': left, 'right': right, 'down': down, 'top': top}

    @staticmethod
    def manhattan_dist(point1, point2):
        if len(point1) != len(point2):
            raise Exception('Dim of points must be the same')
        return sum(abs(point1[i] - point2[i]) for i in range(len(point1)))

    def nearest_point(self, point, points_list):
        """

        :param point:
        :param points_list:
        :return: ordered number of nearest point or None if more than 1 point are nearest
        """
        point_distances = [self.manhattan_dist(point, p) for p in points_list]
        if point_distances.count(min(point_distances)) == 1:
            return point_distances.index(min(point_distances))

    def summary_dist(self, point, points_list):
        return sum([self.manhattan_dist(point, p) for p in points_list])

    @staticmethod
    def extend_area(sq_size):
        points = set()
        points.update(((i, sq_size['down'] - 1) for i in range(sq_size['left'] - 1, sq_size['right'] + 2)))
        points.update(((i, sq_size['top'] + 1) for i in range(sq_size['left'] - 1, sq_size['right'] + 2)))
        points.update(((sq_size['left'] - 1, i) for i in range(sq_size['down'] - 1, sq_size['top'] + 2)))
        points.update(((sq_size['right'] + 1, i) for i in range(sq_size['down'] - 1, sq_size['top'] + 2)))
        return points

    @staticmethod
    def extend_from_point(point, size):
        points = set()
        # top horizontal
        points.update(((i, point[1] + size) for i in range(point[0] - size, point[0] + size + 1)))
        # down horizontal
        points.update(((i, point[1] - size) for i in range(point[0] - size, point[0] + size + 1)))
        # left vertical
        points.update(((point[0] - size, i) for i in range(point[1] - size, point[1] + size + 1)))
        # right vertical
        points.update(((point[0] + size, i) for i in range(point[1] - size, point[1] + size + 1)))
        return points

    def extend_before_threshold(self, point, threshold, defined_points):
        size = 1
        min_threshold = 0
        while min_threshold < threshold:
            check_points = self.extend_from_point(point, size)
            dist = [self.summary_dist(point, defined_points) for point in check_points]
            min_threshold = min(dist)
            size += 1
            yield len(list(filter(lambda x: x < threshold, dist)))

    def main1(self):
        raw_def_points = self.read_points(self.input_data)
        sq_size = self.eval_area(raw_def_points)
        # ---------------  here we will add one extra space to check open areas
        check_points = list(self.extend_area(sq_size))
        unbounded_points = set()
        for point in check_points:
            n_p = self.nearest_point(point, raw_def_points)
            unbounded_points.add(n_p)
        # ---------------
        result_points = [i for i in range(len(raw_def_points)) if i not in unbounded_points]
        raw_undef_points = [(i, j) for i in range(sq_size['left'], sq_size['right'] + 1) for j in
                            range(sq_size['down'], sq_size['top'] + 1) if (i, j) not in raw_def_points]
        for point in raw_undef_points:
            n_p = self.nearest_point(point, raw_def_points)
            if n_p is not None and n_p not in unbounded_points:
                result_points.append(n_p)

        cnt = Counter(result_points)
        return cnt.most_common(1)[0][1]

    def main2(self):
        threshold = 10000
        raw_def_points = self.read_points(self.input_data)
        start_point = (median_high([i[0] for i in raw_def_points]),
                       median_high([i[1] for i in raw_def_points]))

        if self.summary_dist(start_point, raw_def_points) > threshold:
            return 0
        # +1 to include median point to total count
        total_regions = sum(i for i in self.extend_before_threshold(start_point, threshold, raw_def_points)) + 1
        return total_regions
