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

    def download_input(self, url):
        try:
            SESSION_KEY = os.environ['adventofcode-session']
        except KeyError as e:
            print('Please add "adventofcode-session" variable with session string to your PATH')
            sys.exit(1)
        with requests.get(url, cookies={"session": SESSION_KEY}) as response:
            if response.ok:
                lines = response.text.split('\n')
                # remove trailing newline
                print('Input downloaded.')
                return lines[:len(lines)-1]
            else:
                print('Please check session variable "adventofcode-session".')
                print(response.reason, response.status_code)
                sys.exit(1)


