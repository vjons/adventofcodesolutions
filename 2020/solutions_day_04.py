import aoc_lib as al
import re

raw=al.get_aoc_input(al.session_cookie,day=4).strip("\n")

data=[dict([field.split(":") for field in part.replace("\n"," ").split(" ")])\
      for part in raw.split("\n\n")]

fields="byr","iyr","eyr","hgt","hcl","ecl","pid"

def validate1(pp):
    return all(k in pp for k in fields)

def validate2(pp):
    patterns="^(19[2-9]\\d|200[0-2])$","^20(1\\d|20)$","^(20(2\\d|30))$",\
             "^((1[5-8]\\d|19[0-3])cm|(59|6\\d|7[0-6])in)$",\
             "^#(\\d|[a-f]){6}$","^(amb|blu|brn|gry|grn|hzl|oth)$","^\\d{9}$"
    return all(re.match(pattern,pp[key]) for pattern,key in zip(patterns,fields))

valid_pps_1=list(filter(validate1,data))
valid_pps_2=list(filter(validate2,valid_pps_1))

answer1=len(valid_pps_1)
answer2=len(valid_pps_2)

print("answer 1:",answer1,"answer 2:",answer2)