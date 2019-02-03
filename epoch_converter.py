# encoding: utf-8
"""
1. 'etc now' - Returns the current time in UTC and it's corresponding UNIX timestamp
2. 'etc <unix_ts>' - Converts the given unix timestamp into both UTC time and local time


TODO: Add support for 24hour clock w/ preferences
"""

__version__ = "0.1.0"
import sys
from datetime import datetime, timedelta
import time
from workflow import Workflow, ICON_INFO
import pytz
import calendar


time_format_str = "%A, %B %d, %Y %I:%M:%S %p"  # Tuesday, January 29, 2019 07:31:32 AM


def main(wf):
    time_to_convert = wf.args[0].strip().split(' ')[0]

    if time_to_convert == 'now':
        naive_dt_now = datetime.utcnow()
        utc_dt = naive_dt_now.replace(tzinfo=pytz.UTC)
        output_str = utc_dt.strftime(time_format_str)
        timestamp = str(calendar.timegm(utc_dt.timetuple()))
        wf.add_item(title='Current UTC Time', subtitle=output_str, arg=output_str, valid=True, copytext=output_str)
        wf.add_item(title='Current Epoch Time', subtitle=timestamp, copytext=timestamp)
    else:
        # Convert epoch_ts to human readable date

        # Account for time being passed in as milli/micro/nanoseconds
        timestamp, format = normalize_to_seconds(time_to_convert)
        wf.logger.info("Input timestamp '{}' was recognized as {}".format(time_to_convert, format))

        # Create datetime objects both locally and in UTC
        naive_utc_dt = datetime.utcfromtimestamp(timestamp)
        utc_dt = naive_utc_dt.replace(tzinfo=pytz.UTC)
        local_dt = datetime.fromtimestamp(timestamp)

        # Format datetime to strings
        output_str = utc_dt.strftime(time_format_str)
        local_time_output = local_dt.strftime(time_format_str)
        offset_str = get_offset_str_between_local_and_utc(naive_utc_dt, local_dt)
        local_time_output_with_offset = "{} {}".format(local_time_output, offset_str)

        # Add to Alfred
        wf.add_item(title="UTC Time", subtitle=output_str, valid=True, copytext=output_str)
        wf.add_item(title="Local Time", subtitle=local_time_output_with_offset, valid=True, copytext=local_time_output_with_offset)


    wf.send_feedback()


def normalize_to_seconds(time_to_convert):
    len_of_input = len(time_to_convert)
    if len_of_input < 11:
        return float(time_to_convert), "seconds"
    elif len_of_input <= 14:
        # Milliseconds
        return float(time_to_convert)/ 1000, "milliseconds"
    elif len_of_input <= 17:
        # micro
        return float(time_to_convert)/ 1000000, "microseconds"
    else:
        return float(time_to_convert)/ 1000000000, "nanoseconds"


def get_offset_str_between_local_and_utc(naive_utc_dt, local_dt):
    if naive_utc_dt > local_dt:
        time_delta = naive_utc_dt - local_dt
        sign = '-'
    else:
        time_delta = local_dt - naive_utc_dt
        sign = '+'

    return 'GMT{}{}'.format(sign, str(time_delta))


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))



