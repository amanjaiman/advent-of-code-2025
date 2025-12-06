import argparse
import math

def challenge1(input_file):
    nums = []
    with open(input_file+".txt", "r") as file:
        lines_split = [line.strip().split() for line in file.readlines()]
        problems = [[line[i] for line in lines_split] for i in range(0, len(lines_split[0]))]
        for problem in problems:
            op = problem[-1]
            if op == '+':
                nums += [sum([int(n) for n in problem[:-1]])]
            else:
                nums += [math.prod([int(n) for n in problem[:-1]])]
        print(sum(nums))

def challenge2(input_file):
    nums = []
    with open(input_file+".txt", "r") as file:
        lines_split = [list(line.split('\n')[0]) for line in file.readlines()]
        current_problem = []
        for i in range(len(lines_split[0]) - 1, -1, -1):
            col = ''.join([lines_split[line_num][i] for line_num in range(0, len(lines_split))]).strip()

            if col.strip() == '':
                continue

            if col[-1] == '+':
                current_problem += [int(col[:-1].strip())]
                nums += [sum(current_problem)]
                current_problem = []
            elif col[-1] == '*':
                current_problem += [int(col[:-1].strip())]
                nums += [math.prod(current_problem)]
                current_problem = []
            else:
                current_problem += [int(col.strip())]
                
        print(sum(nums))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 6 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
