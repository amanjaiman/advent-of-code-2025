import argparse
import os

TEMPLATE = '''import argparse

def challenge1(input_file):
    pass

def challenge2(input_file):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day {day} Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new day directory')
    parser.add_argument('--day', type=int, required=True, help='Day number')
    
    args = parser.parse_args()
    day = args.day
    
    dir_name = f"day{day}"
    os.makedirs(dir_name, exist_ok=True)
    
    with open(os.path.join(dir_name, f"day{day}.py"), "w") as f:
        f.write(TEMPLATE.format(day=day))
    
    with open(os.path.join(dir_name, "test_input.txt"), "w") as f:
        pass
    
    with open(os.path.join(dir_name, "gold_input.txt"), "w") as f:
        pass
    
    print(f"Created {dir_name}/ with day{day}.py, test_input.txt, and gold_input.txt")

