"""

James is a businessman. He is on a tight schedule this week.
The week starts on Monday at 00:00 and ends on Sunday at 24:00.
His schedule consists of M meetings he needs to take part in.
Each of them will take place in a period of time,
beginning and ending on the same day (there are no two ongoing meetings at the same time).
James is very tired, thus he needs to find the longest possible time slot to sleep.
In other words, he wants to find the longest period of time when there are no ongoing meetings.
The sleeping break can begin and end on different days and should begin and end in the same week.
You are given a string containing M lines. Each line is a substring representing one meeting in the schedule,
in the format "Ddd hh:mm-hh: mm". "Ddd" is a three-letter abbreviation for the day of the week
when the meeting takes place: "Mon" (Monday), "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" hh :mm-hh: mm" means
the beginning time and the ending time of the meeting (from 00:00 to 24:00 inclusive)
The given times represent exact moments of time. So, there are exactly five minutes between 13:40 and 13:45.

Ex - 1

"Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00"

James should sleep on Sunday from 21:00 to 24:00 (180 minutes).

Ex - 2

"Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 09:99-23:59
Mon 05:00-13:00
Mon 15:00-21:00"

James should sleep on tuesday 20:00 to Wednesday 04:25 which give 8hr 25 min  = 505 minutes

"""
from datetime import datetime


def parse_string(schedule: str):
    meeting_list = schedule.split("\n")
    parsed_res = []
    day_mapping = {
        "Mon": 1,
        "Tue": 2,
        "Wed": 3,
        "Thu": 4,
        "Fri": 5,
        "Sat": 6,
        "Sun": 7
    }
    for meeting in meeting_list:
        tmp = meeting.split(" ")
        day = day_mapping.get(tmp[0].strip())
        start_time = tmp[1].split("-")[0]
        end_time = tmp[1].split("-")[1]
        parsed_res.append((day, start_time, "23:59" if end_time == "24:00" else end_time))

    parsed_res.sort(key=lambda val: (val[0], int(val[1].split(":")[0]),
                                     int(val[1].split(":")[1]),
                                     int(val[2].split(":")[0]),
                                     int(val[2].split(":")[0])
                                     ))
    # print(parsed_res)
    return parsed_res


def get_gap(curr_meeting, prev_meeting):
    format = "%d %H:%M"
    gap = datetime.strptime(f"{curr_meeting[0]} {curr_meeting[1]}", format) - \
          datetime.strptime(f"{prev_meeting[0]} {prev_meeting[2]}", format)
    return gap


def calculate_sleep(sorted_schedule):
    n = len(sorted_schedule)
    max_sleep = 0

    for i in range(1, n):
        prev_meeting = sorted_schedule[i - 1]
        curr_meeting = sorted_schedule[i]
        gap = get_gap(curr_meeting, prev_meeting)
        # print(prev_meeting, " - ", curr_meeting, ":", gap.seconds / 60)
        max_sleep = max(max_sleep, gap.seconds / 60)

    max_sleep = max(max_sleep, get_gap((str(7), '00:00', '00:00'), sorted_schedule[-1]).seconds / 60)

    return max_sleep


meeting_sch1 = """Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00"""

meeting_sch2 = """Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00"""

# parse_string(meeting_sch1)
calculate_sleep(parse_string(meeting_sch2))

calculate_sleep(parse_string(meeting_sch1))
