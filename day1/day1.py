import argparse

def challenge1(input_file):
    times_on_zero = 0
    current_position = 50
    with open(input_file+".txt", "r") as file:
        lines = file.readlines()
        
        for l in lines:
            line = l.strip()
            direction, distance = line[0], int(line[1:])
            
            if direction == "L":
                current_position = (current_position - distance) % 100
            else:
                current_position = (current_position + distance) % 100
                
            if current_position == 0:
                times_on_zero += 1
                
    print(times_on_zero)

def challenge2(input_file):
    times_on_zero = 0
    times_past_zero = 0
    extra_rotations = 0
    current_position = 50
    with open(input_file+".txt", "r") as file:
        lines = file.readlines()
        
        for l in lines:
            line = l.strip()
            direction, distance = line[0], int(line[1:])

            extra_rotations += distance // 100
            
            if direction == "L":
                new_position = (current_position - distance) % 100
                if new_position > current_position and 0 not in [new_position, current_position]:
                    times_past_zero += 1
            else:
                new_position = (current_position + distance) % 100
                if new_position < current_position and 0 not in [new_position, current_position]:
                    times_past_zero += 1
                    
            current_position = new_position
                
            if current_position == 0:
                times_on_zero += 1
                
    print(times_on_zero + times_past_zero + extra_rotations)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 1 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)