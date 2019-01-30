from collections import Counter
import re

from AOCDay import AOCDay


class Day3(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 3
        self.input_link = self.input_link.format(day=self.day)
        self.input_data = self.download_input(self.input_link)

    def main1(self):
        params = []
        reg_ex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+).(\d+)')
        for param in self.input_data:
            m = re.search(reg_ex, param)
            params.append((int(m.group(1)),
                           int(m.group(2)),
                           int(m.group(3)),
                           int(m.group(4)),
                           int(m.group(5))))
        all_points = []
        for p in params:
            all_points.extend([(j, i) for i in range(p[1] + 1, p[1] + 1 + p[3])
                               for j in range(p[2] + 1, p[2] + 1 + p[4])])
        c = Counter(all_points)
        return sum([1 for i in c.values() if i > 1])

    def main2(self):
        params = []
        reg_ex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+).(\d+)')
        for param in self.input_data:
            m = re.search(reg_ex, param)
            params.append((int(m.group(1)),
                           int(m.group(2)),
                           int(m.group(3)),
                           int(m.group(4)),
                           int(m.group(5))))
        all_points = []
        for p in params:
            all_points.extend([(j, i) for i in range(p[1] + 1, p[1] + 1 + p[3])
                               for j in range(p[2] + 1, p[2] + 1 + p[4])])
        c = Counter(all_points)
        not_overlap = {item[0] for item in c.items() if item[1] == 1}
        for p in params:
            x = {(j, i) for i in range(p[1] + 1, p[1] + 1 + p[3])
                 for j in range(p[2] + 1, p[2] + 1 + p[4])}
            number = p[0]
            overlap = x & not_overlap
            if len(overlap) == len(x):
                return number
