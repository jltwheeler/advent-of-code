use std::fs;

fn main() {
    let lines = read_and_convert_lines("test.txt");

    part_one(&lines);
    part_two(&lines);
}

fn part_two(lines: &Vec<u32>) {
    let mut summed = 0;
    let mut vec: Vec<u32> = Vec::new();

    for (i, item) in lines.iter().enumerate() {
        if i >= 2 {
            summed = item + lines[i - 1] + lines[i - 2];
            vec.push(summed);
        }
    }

    part_one(&vec);
}

fn part_one(lines: &Vec<u32>) {
    let mut increase_count = 0;
    for (i, item) in lines.iter().enumerate() {
        if i > 0 {
            if item > &lines[i - 1] {
                increase_count += 1;
            }
        }
    }
    println!("number of increases: {}", increase_count)
}

fn read_and_convert_lines(filename: &str) -> Vec<u32> {
    let file_text = fs::read_to_string(filename).unwrap();
    let lines: Vec<u32> = file_text
        .lines()
        .map(|x| x.trim().parse().unwrap())
        .collect();

    return lines;
}
