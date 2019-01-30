from AOCDay import AOCDay


class Day1(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 1
        self.input_link = self.input_link.format(day=self.day)
        self.input_data = self.download_input(self.input_link)

    @staticmethod
    def cycled_counter(ln):
        while True:
            for j in range(ln):
                yield j

    def main1(self):

        frequency = sum(int(i) for i in self.input_data)
        return frequency

    # part2
    def main2(self):
        int_data = [int(i) for i in self.input_data]
        frequency = 0
        counter = self.cycled_counter(len(int_data))
        seen = set()

        while frequency not in seen:
            seen.add(frequency)
            frequency += int_data[next(counter)]
        return frequency

    # frequency = 0
    # counter = cycled_counter(len(int_data))
    # seen = set()
    #
    # while frequency not in seen:
    #     seen.add(frequency)
    #     frequency += int_data[next(counter)]
    # print(frequency)
    # pass
