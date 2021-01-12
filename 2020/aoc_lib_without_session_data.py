import datetime as dt
from requests import Session
import os
from time import time

SESSION_COOKIE="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def get_aoc_input(day=None,year=None):
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
    text=Session().get(url,cookies=dict(session=SESSION_COOKIE)).text
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(filename,'w') as file:
        file.write(text)
    return text

def present_answers(year,day,f,rep=0):
    raw = get_aoc_input(day=day,year=year).strip("\n")
    for i,a in enumerate(f(raw)):
        print(f"Answer {i+1}: {a}")
    if rep:
        t0=time()
        for _ in range(rep): list(f(raw))
        duration=time()-t0
        print(f"Running time: {1000*duration/rep:.2f} ms")