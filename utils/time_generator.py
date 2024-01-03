from dateutil.parser import parse
import random as rd
import datetime
def timeGenerator(start_time_str, end_time_str):
    start_time = parse(start_time_str)
    end_time = parse(end_time_str)

    # Check if start_time has a valid UTC offset
    if start_time.utcoffset() is None:
        raise ValueError("start_time must have a valid UTC offset")

    tz_offset = int(start_time.utcoffset().total_seconds() // 60)
    print(tz_offset)

    time_range = (end_time - start_time).total_seconds()
    random_second = rd.randrange(int(time_range))
    random_time = start_time + datetime.timedelta(seconds=random_second)
    iso_time = random_time.isoformat(timespec='seconds')

    tz_sign = '+' if tz_offset >= 0 else '-'
    tz_hours = abs(tz_offset) // 60
    tz_minutes = abs(tz_offset) % 60
    iso_time_with_tz = f"T{iso_time[-8:]}{tz_sign}{tz_hours:02d}:{tz_minutes:02d}"

    return iso_time_with_tz