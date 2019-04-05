import os
import sys
import requests


class AOCDay:
    def __init__(self):
        self.input_data = None
        self.input_link = 'https://adventofcode.com/2018/day/{day}/input'
        self.day = None

    def main1(self):
        """
        abstract method to solve part 1
        :return: answer to part1
        """
        pass

    def main2(self):
        """
        abstract method to solve part 2
        :return: answer to part2
        """
        pass

    def solve(self, part):
        if part == '1':
            return self.main1()
        if part == '2':
            return self.main2()

    def split_input(self, data):
        lines = data.split('\n')
        # remove trailing newline
        return lines[:len(lines) - 1]

    def download_input(self, url):
        try:
            SESSION_KEY = os.environ['adventofcode-session']
        except KeyError as e:
            print('Please add "adventofcode-session" variable with session string to your PATH')
            sys.exit(1)
        with requests.get(url, cookies={"session": SESSION_KEY}) as response:
            if response.ok:
                print('Input downloaded.')
                return self.split_input(response.text)
            else:
                print('Please check session variable "adventofcode-session".')
                print(response.reason, response.status_code)
                sys.exit(1)

    def load_input(self, day):
        here = os.path.abspath(os.path.dirname(__file__))
        local_input = os.path.join(here, 'data', str(day), 'input.txt')
        if os.path.isfile(local_input):
            return self.read_input(local_input)
        input_content = self.download_input(self.input_link.format(day=day))
        os.makedirs(os.path.dirname(local_input), exist_ok=True)
        with open(local_input, 'w') as f:
            for line in input_content:
                f.write('{line}\n'.format(line=line))
        return input_content


    def read_input(self, path):
        with open(path) as f:
            text = f.read()
        return self.split_input(text)
