from operator import itemgetter
import re
from datetime import datetime
from itertools import groupby
from collections import Counter

from AOCDay import AOCDay


class Day4(AOCDay):
    def __init__(self):
        super().__init__()
        self.day = 4
        self.input_data = self.load_input(self.day)

    @staticmethod
    def sort_log(data):
        log = []
        reg_ex = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] ([^\n]+)')
        for record in data:
            m = re.search(reg_ex, record)
            log.append(dict(datetime=datetime(int(m.group(1)),
                                              int(m.group(2)),
                                              int(m.group(3)),
                                              int(m.group(4)),
                                              int(m.group(5))), info=m.group(6)))
        sorted_log = sorted(log, key=itemgetter('datetime'))
        return sorted_log

    @staticmethod
    def make_sleep_db(sorted_log):
        db = []
        guard = None
        dt = None
        sleep_start = None
        sleep_end = None
        reg_ex_shift = re.compile(r'Guard #(\d+) begins shift')
        text_asleep = 'falls asleep'
        text_awake = 'wakes up'
        for record in sorted_log:
            if re.search(reg_ex_shift, record['info']):
                guard = re.search(reg_ex_shift, record['info']).group(1)
                dt = record['datetime'].date()
            if record['info'] == text_asleep:
                sleep_start = record['datetime'].minute
            if record['info'] == text_awake:
                sleep_end = record['datetime'].minute
                db.append({'Guard': guard,
                           'date': dt,
                           'sleep_duration': sleep_end - sleep_start,
                           'sleep_start': sleep_start,
                           'sleep_end': sleep_end - 1})

        return db

    @staticmethod
    def max_sleep_guard(db):
        summary_db = []
        order_by_guard = sorted(db, key=itemgetter('Guard'))
        for guard, items in groupby(order_by_guard, key=itemgetter('Guard')):
            summary_db.append({'Guard': guard,
                               'total_duration': sum(i['sleep_duration'] for i in items)})
        return max(summary_db, key=itemgetter('total_duration'))

    @staticmethod
    def most_sleeply_minute(guard_db):
        minutes_list = []
        for item in guard_db:
            minutes_list.extend([i for i in range(item['sleep_start'], item['sleep_end'] + 1)])
        minutes_list_c = Counter(minutes_list)
        return minutes_list_c.most_common(1)[0]

    def main1(self):
        sorted_log = self.sort_log(self.input_data)
        db = self.make_sleep_db(sorted_log)
        guard = self.max_sleep_guard(db)
        guard_db = [i for i in db if i['Guard'] == guard['Guard']]
        minute = self.most_sleeply_minute(guard_db)[0]
        return int(guard['Guard']) * minute

    def main2(self):
        sorted_log = self.sort_log(self.input_data)
        minute_res = -1
        guard_res = -1
        times = 0
        db = self.make_sleep_db(sorted_log)
        order_by_guard = sorted(db, key=itemgetter('Guard'))
        for guard, items in groupby(order_by_guard, key=itemgetter('Guard')):
            minute = self.most_sleeply_minute(items)
            if minute[1] > times:
                minute_res = minute[0]
                guard_res = int(guard)
                times = minute[1]
        return guard_res * minute_res
