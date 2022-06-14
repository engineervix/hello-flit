#!/usr/bin/env python3

"""
core.py

create a directory tree suitable for organizing
your work using the Year / Quarter / Month / Week convention, for instance:

2017/
├── qtr_01
│   ├── 01_Jan
│   │   ├── wk01_01Jan-07Jan
│   │   ├── wk02_08Jan-14Jan
│   │   ├── wk03_15Jan-21Jan
│   │   ├── wk04_22Jan-28Jan
│   │   └── wk05_29Jan-04Feb
│   ├── 02_Feb
│   │   ├── wk05_29Jan-04Feb
│   │   ├── wk06_05Feb-11Feb
│   │   ├── wk07_12Feb-18Feb
│   │   ├── wk08_19Feb-25Feb
│   │   └── wk09_26Feb-04Mar
│   └── 03_Mar
│       ├── wk09_26Feb-04Mar
│       ├── wk10_05Mar-11Mar
│       ├── wk11_12Mar-18Mar
│       ├── wk12_19Mar-25Mar
│       └── wk13_26Mar-01Apr
├── qtr_02
│   ├── 04_Apr
│   │   ├── wk13_26Mar-01Apr
│   │   ├── wk14_02Apr-08Apr
│   │   ├── wk15_09Apr-15Apr
│   │   ├── wk16_16Apr-22Apr
│   │   ├── wk17_23Apr-29Apr
│   │   └── wk18_30Apr-06May
│   ├── 05_May
│   │   ├── wk18_30Apr-06May
│   │   ├── wk19_07May-13May
│   │   ├── etc, you get the picture!
"""

import calendar
import logging
import os
import sys
from datetime import datetime, timedelta

CURRENT_DIR = os.getcwd()


def end_date(year: int, month: int, lastday: int):
    """
    Given a particular date, this function returns the last day of the week
    (Saturday) in which the given date falls. For example,
    if our given date is 2016-12-21:
        December 2016
        Su Mo Tu We Th Fr Sa
                     1  2  3
         4  5  6  7  8  9 10
        11 12 13 14 15 16 17
        18 19 20 21 22 23 24
        25 26 27 28 29 30 31
    Then the last day of the week will be 2016-12-24
    """
    the_last_day = datetime(year, month, lastday)  # last day of the month
    day_of_week = the_last_day.weekday()
    if day_of_week == 5:
        return the_last_day
    elif day_of_week == 4:
        return the_last_day + timedelta(days=1)
    elif day_of_week == 3:
        return the_last_day + timedelta(days=2)
    elif day_of_week == 2:
        return the_last_day + timedelta(days=3)
    elif day_of_week == 1:
        return the_last_day + timedelta(days=4)
    elif day_of_week == 0:
        return the_last_day + timedelta(days=5)
    elif day_of_week == 6:
        return the_last_day + timedelta(days=6)


def which_quarter(month: int, output_dir: str, quarter_prefix: str):
    """
    Given a particular `month` as an int, this function determines which quarter
    it belongs to and assigns the path of the relevant quarter_dir (which is a
    subdirectory of the specified `output_dir`) using the supplied `quarter_prefix`
    """
    if 1 <= month <= 3:
        quarter_dir = os.path.join(output_dir, quarter_prefix + str(1).zfill(2))
    elif 4 <= month <= 6:
        quarter_dir = os.path.join(output_dir, quarter_prefix + str(2).zfill(2))
    elif 7 <= month <= 9:
        quarter_dir = os.path.join(output_dir, quarter_prefix + str(3).zfill(2))
    elif 10 <= month <= 12:
        quarter_dir = os.path.join(output_dir, quarter_prefix + str(4).zfill(2))
    return quarter_dir


def create_dirs(year: int):
    """
    Create the directory tree for the specified year.
    """

    # create output directory using the year
    output_dir = os.path.join(CURRENT_DIR, str(year))
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    else:
        logging.warning(f"The *{output_dir}* directory already exists, will not overwrite!")
        sys.exit(1)

    # create directories for each quarter of the year
    quarter_prefix = "qtr_"
    for quarter in range(1, 5):
        the_quarter = quarter_prefix + str(quarter).zfill(2)
        qtr_dir = os.path.join(output_dir, the_quarter)
        if not os.path.exists(qtr_dir):
            os.mkdir(qtr_dir)
        else:
            logging.warning(f"The *{qtr_dir}* directory already exists, will not overwrite!")
            sys.exit(1)

    # Iterate through the months
    for month_num, month_name in zip(range(0, 13), calendar.month_abbr):
        if not month_num == 0 and month_name[0]:
            the_month = str(month_num).zfill(2) + "_" + month_name
            qtr_dir = which_quarter(month_num, str(year), quarter_prefix)
            month_dir = os.path.join(CURRENT_DIR, qtr_dir, the_month)
            if not os.path.exists(month_dir):
                os.mkdir(month_dir)
            else:
                logging.warning(f"The *{month_dir}* directory already exists, will not overwrite!")
                sys.exit(1)
            day_01 = datetime(year, month_num, 1).weekday()
            last_day = calendar.monthrange(year, month_num)[1]
            if day_01 == 6:
                start_date = datetime(year, month_num, 1)
            elif day_01 == 5:
                start_date = datetime(year, month_num, 1) - timedelta(days=6)
            elif day_01 == 4:
                start_date = datetime(year, month_num, 1) - timedelta(days=5)
            elif day_01 == 3:
                start_date = datetime(year, month_num, 1) - timedelta(days=4)
            elif day_01 == 2:
                start_date = datetime(year, month_num, 1) - timedelta(days=3)
            elif day_01 == 1:
                start_date = datetime(year, month_num, 1) - timedelta(days=2)
            elif day_01 == 0:
                start_date = datetime(year, month_num, 1) - timedelta(days=1)
            total_days = (end_date(year, month_num, last_day) - start_date).days + 1
            weeks = total_days // 7
            week_starts = start_date
            week_ends = week_starts + timedelta(days=6)

            # Iterate through the weeks
            if month_num == 12:
                for _ in range(0, weeks):
                    wk_number = week_ends.isocalendar()[1]
                    custom_wk_number = wk_number
                    if wk_number == 1:
                        custom_wk_number = 53
                    the_week = (
                        "wk"
                        + str(custom_wk_number).zfill(2)
                        + "_"
                        + week_starts.strftime("%d%b")
                        + "-"
                        + week_ends.strftime("%d%b")
                    )
                    week_dir = os.path.join(month_dir, the_week)
                    if not os.path.exists(week_dir):
                        os.mkdir(week_dir)
                    else:
                        logging.warning(f"The *{week_dir}* directory already exists, will not overwrite!")
                        sys.exit(1)
                    week_starts += timedelta(days=7)
                    week_ends += timedelta(days=7)
            else:
                for _ in range(0, weeks):
                    the_week = (
                        "wk"
                        + str(week_ends.isocalendar()[1]).zfill(2)
                        + "_"
                        + week_starts.strftime("%d%b")
                        + "-"
                        + week_ends.strftime("%d%b")
                    )
                    week_dir = os.path.join(month_dir, the_week)
                    if not os.path.exists(week_dir):
                        os.mkdir(week_dir)
                    else:
                        logging.warning(f"The *{week_dir}* directory already exists, will not overwrite!")
                        sys.exit(1)
                    week_starts += timedelta(days=7)
                    week_ends += timedelta(days=7)
