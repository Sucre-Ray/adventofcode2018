from AOCDay import AOCDay
import sys
sys.setrecursionlimit(2000)


class Day8(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 8
        self.input_data = self.load_input(self.day)
        self.counter = 0

    def remove_node_without_child(self, data_list, offset=1):
        header_len = 2
        child_amt_pos = 0
        meta_amt_pos = child_amt_pos + 1
        while data_list[child_amt_pos] > 0:
            offset += 1
            child_amt_pos = (offset - 1) * header_len
            meta_amt_pos = child_amt_pos + 1
        self.counter += sum(data_list[offset * header_len:(offset * header_len) + data_list[meta_amt_pos]])
        return child_amt_pos, (offset * header_len) + data_list[meta_amt_pos]

    def main1(self):
        data_list = [int(i) for i in self.input_data[0].split()]
        while data_list:
            fisrt_part_end, second_part_start = self.remove_node_without_child(data_list)
            data_list[fisrt_part_end - 2] = data_list[fisrt_part_end - 2] - 1
            del data_list[fisrt_part_end: second_part_start]
        return self.counter

    def main2(self):
        pass
