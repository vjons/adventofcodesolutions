import datetime as dt
from requests import Session
import os

def get_aoc_input(session,day=None,year=None):
    now=dt.datetime.now(dt.timezone.utc)
    day=now.day if day is None else day
    year=now.year if year is None else year
    release_time=dt.datetime(year,12,day,5,tzinfo=dt.timezone.utc)
    url=f"https://adventofcode.com/{year}/day/{day}/input"
    folder=f"../{year}"
    filename=os.path.join(folder,f"input_day_{day:0>2}.txt")
    if os.path.exists(filename):
        with open(filename,"r") as file:
            return file.read()
    if year<2015 or day>25:
        msg=f"There are no puzzles for {year}-12-{day}"
        raise Exception(msg)
    if now<release_time:
        msg=f"The puzzle is not released before {release_time.strftime('%Y-%m-%d %H:%M')} UTC+00:00"
        raise Exception(msg)
    text=Session().get(url,cookies=dict(session=session)).text
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(filename,'w') as file:
        file.write(text)
    return text








