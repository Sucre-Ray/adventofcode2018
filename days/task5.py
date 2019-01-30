import math

from AOCDay import AOCDay


class Day5(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 5
        self.input_link = self.input_link.format(day=self.day)
        self.input_data = self.download_input(self.input_link)

    @staticmethod
    def remove_appropriate(line):
        pos = 0
        line_list = list(line)
        while pos < len(line_list) - 1:
            if line_list[pos].islower() and line_list[pos + 1] == line_list[pos].upper():
                line_list.pop(pos)
                line_list.pop(pos)
                pos = max(pos - 2, 0)
            if line_list[pos].isupper() and line_list[pos + 1] == line_list[pos].lower():
                line_list.pop(pos)
                line_list.pop(pos)
                pos = max(pos - 2, 0)
            else:
                pos += 1
        return len(line_list)

    def best_polymer(self, line):
        letters = set(line.lower())
        min_len = math.inf
        for l in letters:
            prepared_line = [i for i in line if i != l and i != l.upper()]
            new_min_len = self.remove_appropriate(prepared_line)
            if new_min_len < min_len:
                min_len = new_min_len
        return min_len

    def main2(self):
        return self.best_polymer(self.input_data[0])

    def main1(self):
        return self.remove_appropriate(self.input_data[0])
