import io
import re

def parse(inputL):
    valid = 0
    data = inputL.split('\n\n')
    passport = {}
    isvalid = {
            "byr" : lambda value : 1920 <= int(value) <= 2020,
            "iyr" : lambda value : 2010 <= int(value) <= 2020,
            "eyr" : lambda value : 2020 <= int(value) <= 2030,
            "hgt" : lambda value : \
                    len(value) == 5 and 150 <= int(value[:3]) <= 193 if value[-2:] == "cm" \
                    else len(value) == 4 and 59 <= int(value[:2]) <= 76 if value[-2:] == "in" \
                    else 0,
            "hcl" : lambda value : re.match("^#[0-9a-f]{6}$", value) is not None,
            "ecl" : lambda value : \
                    value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid" : lambda value : re.match("^[0-9]{9}$", value) is not None,
            "cid" : lambda value : 1
            }

    for info in data:
        for field in info.split():
            if field.startswith('cid'):
                continue
            #print(field.split(':')[0] + ' ' + field.split(':')[1] + ' ' + \
            #        str(isvalid[field.split(':')[0]](field.split(':')[1])))
            passport[field.split(':')[0]] = \
                    isvalid[field.split(':')[0]](field.split(':')[1])
        #print('')
        valid += 1 if all(passport.values()) and len(passport) == 7 else 0
        passport={}
    return valid

def main():
    with open("../input.txt") as f:
        inputL = f.read()

    print(parse(inputL))

if __name__ == "__main__":
    main()
