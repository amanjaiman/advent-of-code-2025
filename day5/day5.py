import argparse

def challenge1(input_file):
    total_valid = 0
    with open(input_file+".txt", "r") as file:
        lines = file.read().split('\n\n')
        ranges = sorted([tuple(map(int, r.split('-'))) for r in lines[0].split('\n')])
        ingredients = sorted([int(x) for x in lines[1].split('\n')])

        current_range_idx = 0

        for ingredient in ingredients:
            while current_range_idx < len(ranges) and ingredient > ranges[current_range_idx][1]:
                current_range_idx += 1

            if current_range_idx == len(ranges):
                break
            
            if ingredient < ranges[current_range_idx][0]:
                continue
            elif ingredient > ranges[current_range_idx][1]:
                current_range_idx += 1
            else:
                total_valid += 1

        print(total_valid)

def challenge2(input_file):
    total_valid = 0
    with open(input_file+".txt", "r") as file:
        lines = file.read().split('\n\n')
        ranges = sorted([tuple(map(int, r.split('-'))) for r in lines[0].split('\n')])

        current_range_idx = 1
        current_range_min = ranges[0][0]
        current_range_max = ranges[0][1]

        while current_range_idx < len(ranges):
            if ranges[current_range_idx][0] <= current_range_max:
                current_range_max = max(current_range_max, ranges[current_range_idx][1])
            else:
                total_valid += (current_range_max - current_range_min + 1)
                current_range_min = ranges[current_range_idx][0]
                current_range_max = ranges[current_range_idx][1]
            current_range_idx += 1
        
        total_valid += (current_range_max - current_range_min + 1)
        print(total_valid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 5 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
