use std::fs;

fn main() {
    let lines = read_and_convert_lines("input.txt");
    part_one(&lines);
    part_two(&lines);
}

fn part_two(lines: &Vec<String>) {
    let mut aim: u32 = 0;
    let mut depth: u32 = 0;
    let mut forward: u32 = 0;
    for x in lines {
        let split: Vec<&str> = x.split(" ").collect();
        let amt: u32 = split[1].parse().unwrap();
        if split[0] == "down" {
            aim += amt;
        } else if split[0] == "up" {
            aim -= amt;
        } else {
            forward += amt;
            depth += amt * aim;
        }
    }

    println!("The answer to part two is: {}", depth * forward);
}

fn part_one(lines: &Vec<String>) {
    let mut depth: u32 = 0;
    let mut forward: u32 = 0;
    for x in lines {
        let split: Vec<&str> = x.split(" ").collect();
        let amt: u32 = split[1].parse().unwrap();
        if split[0] == "down" {
            depth += amt;
        } else if split[0] == "up" {
            depth -= amt;
        } else {
            forward += amt;
        }
    }

    println!("The answer to part one is: {}", forward * depth);
}

fn read_and_convert_lines(filename: &str) -> Vec<String> {
    let file_text = fs::read_to_string(filename).unwrap();
    let lines: Vec<String> = file_text.lines().map(|s| s.to_string()).collect();

    return lines;
}
