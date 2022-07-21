import re

def is_valid_passport(dict_: dict) -> bool:
    re_hcl = re.compile(r"#[0-9a-f]+")

    if int(dict_["byr"]) < 1920 or int(dict_["byr"]) > 2002:
        return False
    if int(dict_["iyr"]) < 2010 or int(dict_["iyr"]) > 2020:
        return False
    if int(dict_["eyr"]) < 2020 or int(dict_["eyr"]) > 2030:
        return False
    if "cm" in dict_["hgt"]:
        if int(dict_["hgt"][:-2]) < 150 or int(dict_["hgt"][:-2]) > 193:
            return False
    elif "in" in dict_["hgt"]:
        print(dict_["hgt"])
        if int(dict_["hgt"][:-2]) < 59 or int(dict_["hgt"][:-2]) > 76:
            return False
    else:
        return False
    if  not re_hcl.findall(dict_["hcl"]):
        return False
    if dict_["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if len(dict_["pid"]) != 9:
        return False

    return True

def part_one(passports: list, required_fields: list) -> int:
    return sum(
        1
        for i, passport in enumerate(passports)
        if all(req in passport for req in required_fields)
    )

def part_two(passports: list, required_fields:list) -> int:
    regex = re.compile(r"(\w\w\w)(:)(.+)")

    num_valid = 0
    for passport in passports:
        if any(req not in passport for req in required_fields):
            continue

        fields = passport.split()
        passport_dict = {}
        for field in fields:
            key = regex.match(field).group(1)
            val = regex.match(field).group(3)
            passport_dict[key] = val

        print(passport_dict)
        if is_valid_passport(passport_dict):
            num_valid += 1

    return num_valid

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        passports = f.read().split("\n\n")

    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    print(part_one(passports, required_fields))
    print(part_two(passports, required_fields))
