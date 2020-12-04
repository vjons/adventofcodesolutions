import aoc_lib as al
import re

raw=al.get_aoc_input(al.session_cookie,day=5).strip("\n")

data=[dict([field.split(":") for field in part.replace("\n"," ").split(" ")])\
      for part in raw.split("\n\n")]

# fields="byr","iyr","eyr","hgt","hcl","ecl","pid"

# def validate1(pp):
#     return all(k in pp for k in fields)

# def validate2(pp):
#     patterns="19[2-9][0-9]|200[0-2]","20(1[0-9]|20)","20(2[0-9]|30)",\
#              "(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in",\
#              "#([0-9]|[a-f]){6}","amb|blu|brn|gry|grn|hzl|oth","[0-9]{9}"
#     return all(re.match(pattern,pp[key]) for pattern,key in zip(patterns,fields))

# valid_pps_1=list(filter(validate1,data))
# valid_pps_2=list(filter(validate2,valid_pps_1))

# answer1=len(valid_pps_1)
# answer2=len(valid_pps_2)

# print("answer 1:",answer1,"answer 2:",answer2)
