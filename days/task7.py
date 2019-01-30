from collections import defaultdict
from AOCDay import AOCDay


class Day7(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 7
        self.input_link = self.input_link.format(day=self.day)
        self.input_data = self.download_input(self.input_link)

    @staticmethod
    def read_points(data):
        instructions = defaultdict(list)
        instructions_reverted = defaultdict(list)
        depends_on = set()
        dependent = set()
        for line in data:
            instructions[line.split()[1]].append(line.split()[7])
            instructions_reverted[line.split()[7]].append(line.split()[1])
            dependent.add(line.split()[1])
            depends_on.add(line.split()[7])
        return instructions, instructions_reverted, dependent - depends_on

    @staticmethod
    def order_route(instructions, instructions_reverted, starting_points):
        result_order = []
        available_to_chose = []
        if len(starting_points) == 1:
            last_added = starting_points.pop()
            result_order.append(last_added)
            available_to_chose.extend(instructions[last_added])
        else:
            last_added = min(starting_points)
            starting_points = set(filter(lambda x: x != last_added, starting_points))
            result_order.append(last_added)
            available_to_chose.extend(starting_points)
            added_choice = instructions[last_added]
            for i in added_choice:
                if all(elem in result_order for elem in instructions_reverted[i]):
                    available_to_chose.append(i)
            available_to_chose = list(filter(lambda x: x != last_added, available_to_chose))

        while available_to_chose:
            last_added = min(available_to_chose)
            result_order.append(last_added)
            added_choice = instructions[last_added]
            for i in added_choice:
                if all(elem in result_order for elem in instructions_reverted[i]):
                    available_to_chose.append(i)
            available_to_chose = list(filter(lambda x: x != last_added, available_to_chose))
            instructions.pop(last_added)

        return ''.join(result_order)

    def main1(self):
        instructions, instructions_reverted, starting_points = self.read_points(self.input_data)
        return self.order_route(instructions, instructions_reverted, starting_points)
