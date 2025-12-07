import argparse
from functools import lru_cache

def challenge1(input_file):
    splits = 0
    with open(input_file+".txt", "r") as file:
        lines = list(map(str.strip, file.readlines()))
        beam_positions = set([lines[0].index('S')])

        for line_num in range(1, len(lines)):
            for position in list(beam_positions):
                if lines[line_num][position] == '^':
                    splits += 1
                    beam_positions.remove(position)
                    beam_positions.add(position-1)
                    beam_positions.add(position+1)

        print(splits)

def challenge2(input_file):
    with open(input_file+".txt", "r") as file:
        lines = tuple(map(str.strip, file.readlines()))
        beam_idx = lines[0].index('S')

        @lru_cache(maxsize=None)
        def process_line(line_num, beam_idx):
            if line_num == len(lines):
                return 1
            
            if lines[line_num][beam_idx] == '^':
                return process_line(line_num+1, beam_idx-1) + process_line(line_num+1, beam_idx+1)
            
            return process_line(line_num+1, beam_idx)

        total_timelines = process_line(1, beam_idx)
        print(total_timelines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 7 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
