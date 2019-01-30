import sys
from argparse import ArgumentParser
import days as d


def parse_input(argv):
    parser = ArgumentParser()
    parser.add_argument("-d", "--day", dest="day", choices=[str(i) for i in range(1, 26)],
                        help="specify day, what you want to solve (1-25)")
    parser.add_argument("-p", "--part", dest="part", choices=['1', '2'],
                        help="specify part, what you want to solve (1 or 2)")
    # process options
    try:
        args = parser.parse_args(argv)
    except Exception:
        parser.error("Invalid input parameters.")
        sys.exit(0)

    # get all input parameters
    return args.day, args.part


def get_day_task(day_number):
    """
    factory method
    :return:
    """
    days = {
        '1': d.Day1,
        '2': d.Day2,
        '3': d.Day3,
        '4': d.Day4,
        '5': d.Day5,
        '6': d.Day6,
        '7': d.Day7,
    }
    try:
        cls = days[day_number]
        return cls()
    except KeyError:
        print('Looks like this day haven\'t solved yet. '
              'Try another day from {} to {}.'.format(min(days), max(days)))
        sys.exit(0)


def main():
    day_number, part = parse_input(sys.argv[1:])
    day_task = get_day_task(day_number)
    answer = day_task.solve(part)
    print('Day:{}\nPart:{}\nAnswer:{}'.format(day_number, part, answer))


if __name__ == '__main__':
    main()
