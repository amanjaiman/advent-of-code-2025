import argparse

def challenge1(input_file):
    total = 0
    with open(input_file+".txt", "r") as file:
        for line in file.readlines():
            bank = line.strip()
            p1 = int(bank[0])
            p2 = int(bank[1])
            p = 1
            while p < len(bank):
                num = int(bank[p])
                if num > p1 and p < len(bank) - 1:
                    p1 = num
                    p2 = int(bank[p+1])
                elif num > p2:
                    p2 = num
                p += 1
            total += int(str(p1) + str(p2))

        print(total)


def challenge2(input_file):
    total = 0
    with open(input_file+".txt", "r") as file:
        for line in file.readlines():
            bank = line.strip()
            remaining_length = 12
            num = ""
            while remaining_length < len(bank) and remaining_length > 0:
                to_check = bank[0:(len(bank)-remaining_length+1)]
                max_digit = max(int(c) for c in to_check)
                max_index = to_check.index(str(max_digit))
                num += to_check[max_index]
                remaining_length -= 1
                bank = bank[max_index + 1:]
            
            if remaining_length != 0:
                num += bank
            total += int(num)
        print(total)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 3 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
