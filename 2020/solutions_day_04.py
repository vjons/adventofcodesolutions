import aoc_lib as al
import re


def answers(raw):
    data=[dict([field.split(":") for field in \
          part.replace("\n"," ").split(" ")]) for part in raw.split("\n\n")]

    fields="byr","iyr","eyr","hgt","hcl","ecl","pid"

    #Part 1
    def validate1(pp):
        return all(k in pp for k in fields)

    valid_pps_1=list(filter(validate1,data))
    yield len(valid_pps_1)

    #Part 2
    def validate2(pp):
        regs="^(19[2-9]\\d|200[0-2])$","^20(1\\d|20)$","^(20(2\\d|30))$",\
             "^((1[5-8]\\d|19[0-3])cm|(59|6\\d|7[0-6])in)$",\
             "^#(\\d|[a-f]){6}$","^(amb|blu|brn|gry|grn|hzl|oth)$","^\\d{9}$"
        return all(re.match(reg,pp[key]) for reg,key in zip(regs,fields))

    yield len(list(filter(validate2,valid_pps_1)))

if __name__=="__main__":
    al.present_answers(4,answers)