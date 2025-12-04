import argparse

def challenge1(input_file):  
    with open(input_file+".txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
        num_lines = len(lines)
        line_length = len(lines[0])
        v = 0
        for i in range(num_lines):
            for j in range(line_length):
                if lines[i][j] == "@":
                    min_i, max_i = max(0, i-1), min(num_lines-1, i+1)
                    min_j, max_j = max(0, j-1), min(line_length-1, j+1)
                    adjacents = [lines[k][l] for k in range(min_i, max_i+1) for l in range(min_j, max_j+1) if k != i or l != j]
                    if adjacents.count('@') < 4:
                        v += 1
        print(v)

def challenge2(input_file):
    final_count = 0
    with open(input_file+".txt", "r") as file:
        lines = [list(line.strip()) for line in file.readlines()]
        num_lines = len(lines)
        line_length = len(lines[0])
        
        v = -1
        while v != 0:
            v = 0
            for i in range(num_lines):
                for j in range(line_length):
                    if lines[i][j] == "@":
                        min_i, max_i = max(0, i-1), min(num_lines-1, i+1)
                        min_j, max_j = max(0, j-1), min(line_length-1, j+1)
                        adjacents = [lines[k][l] for k in range(min_i, max_i+1) for l in range(min_j, max_j+1) if k != i or l != j]
                        if adjacents.count('@') < 4:
                            v += 1
                            lines[i][j] = '.'
            final_count += v
        print(final_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 4 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
