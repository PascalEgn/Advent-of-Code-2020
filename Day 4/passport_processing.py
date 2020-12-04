import re


def check_passport(passport_map):
    if ('byr' in passport_map and check_byr(passport_map['byr']) and
            'iyr' in passport_map and check_iyr(passport_map['iyr']) and
            'eyr' in passport_map and check_eyr(passport_map['eyr']) and
            'hgt' in passport_map and check_hgt(passport_map['hgt']) and
            'hcl' in passport_map and check_hcl(passport_map['hcl']) and
            'ecl' in passport_map and check_ecl(passport_map['ecl']) and
            'pid' in passport_map and check_pid(passport_map['pid'])):
        return True
    else:
        return False


def check_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


def check_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False


def check_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False


def check_hgt(hgt):
    if hgt.find('cm') != -1:
        height = hgt.split('cm')[0]
        if 150 <= int(height) <= 193:
            return True
    elif hgt.find('in') != -1:
        height = hgt.split('in')[0]
        if 59 <= int(height) <= 76:
            return True
    else:
        return False


def check_hcl(hcl):
    valid_hcl = re.search(r'^#([0-9]|[a-f]){6}$', hcl)
    if valid_hcl:
        return True
    else:
        return False


def check_ecl(ecl):
    valid_ecl = re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', ecl)
    if valid_ecl:
        return True
    else:
        return False


def check_pid(pid):
    valid_pid = re.search(r'^[0-9]{9}$', pid)
    if valid_pid:
        return True
    else:
        return False


with open('input', 'r') as input_passports:
    passport_array = []
    passport = []
    for passport_line in input_passports:
        if not passport_line.strip():
            passport_array.append(passport.copy())
            passport.clear()
        else:
            passport.extend(passport_line.split())
    passport_array.append(passport.copy())

valid_counter = 0

for passport_data in passport_array:
    passport = {}
    for x in passport_data:
        key = x.split(':')[0]
        value = x.split(':')[1]
        passport[key] = value
    if check_passport(passport):
        valid_counter += 1
    passport.clear()

print(valid_counter)
