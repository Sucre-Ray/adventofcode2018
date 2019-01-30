from collections import Counter
from itertools import combinations

from AOCDay import AOCDay


class Day2(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 2
        self.input_link = self.input_link.format(day=self.day)
        self.input_data = self.download_input(self.input_link)

    def main1(self):
        two_c = 0
        three_c = 0
        for word in self.input_data:
            c = Counter(list(word))
            if 2 in c.values() and 3 in c.values():
                two_c += 1
                three_c += 1
            elif 2 in c.values():
                two_c += 1
            elif 3 in c.values():
                three_c += 1
        return three_c * two_c

    @staticmethod
    def simple_dist(str1, str2, error=1):
        err_pos = set()
        if len(str1) == len(str2):
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    err_pos.add(i)
                    if len(err_pos) > error:
                        return
            list_str = list(str1)
            for i in err_pos:
                list_str[i] = ''
            return ''.join(list_str)

    def main2(self):
        for combination in combinations(self.input_data, 2):
            if self.simple_dist(combination[0], combination[1]):
                return self.simple_dist(combination[0], combination[1])
