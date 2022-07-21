import re

rule_re = re.compile(r"\d*-\d* or \d*-\d*$")


def part_one(inputs: list) -> int:
    rules = inputs[0].split("\n")
    your_ticket = [int(i) for i in inputs[1].split("\n")[-1].split(",")]
    nearby_ticks = inputs[-1].split("\n")

    rule_ranges = {}
    for rule in rules:
        rule_name = rule.split(":")[0]
        limits = rule_re.findall(rule)[0].split(" or ")
        nums = []
        for limit in limits:
            num_strs = limit.split("-")
            num_1 = int(num_strs[0])
            num_2 = int(num_strs[1]) + 1
            for i in range(num_1, num_2):
                nums.append(i)

        rule_ranges[rule_name] = nums

    invalids = []
    valids = []
    for ticket in nearby_ticks[1:]:
        valid_ticket = True
        nums = [int(num) for num in ticket.split(",")]
        for num in nums:
            valid = any(num in range_ for range_ in rule_ranges.values())
            if not valid:
                valid_ticket = False
                invalids.append(num)
        if valid_ticket:
            valids.append(ticket)
    return your_ticket, sum(invalids), valids, rule_ranges


def part_two(your_ticket, valid_tickets: list, rule_ranges: dict) -> int:
    cols = len(valid_tickets[0].split(","))
    tickets = [[int(x) for x in ticket.split(",")] for ticket in valid_tickets]

    match_fields = {i: [] for i in range(cols)}
    for key, val in rule_ranges.items():
        for i in range(cols):
            in_range = all(ticket[i] in val for ticket in tickets)
            if in_range:
                match_fields[i].append(key)

    ordered_keys = sorted(match_fields, key=lambda key: len(match_fields[key]))

    ordered_fields = {}
    correct_cols = []
    for key in ordered_keys:
        vals = match_fields[key]
        for x in vals:
            if x not in correct_cols:
                val = x
                ordered_fields[key] = val
                correct_cols.append(val)

    result = 1
    for key, val in ordered_fields.items():
        if "departure" in val:
            result *= your_ticket[key]

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.read().split("\n\n")

    your_ticket, num_invalid, valid_tickets, rule_ranges = part_one(inputs)
    print(num_invalid)

    print(part_two(your_ticket, valid_tickets, rule_ranges))

