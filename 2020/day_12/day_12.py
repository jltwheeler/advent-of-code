import re
import math

regex = re.compile(r"([A-Za-z]*)(\d+)")


def part_one(inputs: list) -> int:
    dirn = "E"
    east = 0
    north = 0

    dirs = {"N": 0, "E": 90, "S": 180, "W": 270}
    bearings = {
        0: "N",
        90: "E",
        180: "S",
        270: "W",
        360: "N",
    }

    for line in inputs:
        action, amount = regex.findall(line)[0]
        amount = int(amount)

        if action == "N":
            north += amount
        elif action == "S":
            north -= amount
        elif action == "E":
            east += amount
        elif action == "W":
            east -= amount
        elif action == "L":
            bearing = dirs[dirn]
            bearing -= amount
            if bearing <= 0:
                bearing += 360
            dirn = bearings[bearing]
        elif action == "R":
            bearing = dirs[dirn]
            bearing += amount
            if bearing >= 360:
                bearing -= 360
            dirn = bearings[bearing]
        elif action == "F":
            if dirn == "N":
                north += amount
            elif dirn == "S":
                north -= amount
            elif dirn == "E":
                east += amount
            elif dirn == "W":
                east -= amount

    return abs(east) + abs(north)


def rotate_pt(x, y, rot):
    rad = math.radians(rot)
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)
    return new_x, new_y


def part_two(inputs: list) -> int:
    waypoint = [10, 1]
    ship = [0, 0]

    for line in inputs:
        action, amount = regex.findall(line)[0]
        amount = int(amount)

        if action == "N":
            waypoint[1] += amount
        elif action == "S":
            waypoint[1] -= amount
        elif action == "E":
            waypoint[0] += amount
        elif action == "W":
            waypoint[0] -= amount
        elif action == "L":
            rot = amount
            new_x, new_y = rotate_pt(waypoint[0], waypoint[1], rot)
            waypoint = [new_x, new_y]
        elif action == "R":
            rot = -1 * amount
            new_x, new_y = rotate_pt(waypoint[0], waypoint[1], rot)
            waypoint = [new_x, new_y]
        elif action == "F":
            ship[0] += waypoint[0] * amount
            ship[1] += waypoint[1] * amount

    return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(part_one(inputs))
    print(part_two(inputs))
