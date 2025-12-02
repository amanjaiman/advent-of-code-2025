import argparse

def challenge1(input_file):
    with open(input_file+".txt", "r") as file:
        invalid_ids = []
        ranges = file.readline().strip().split(",")
        for r in ranges:
            start, end = map(int, r.split("-"))

            for i in range(start, end + 1):
                num = str(i)
                num_parts = [num[:len(num)//2], num[len(num)//2:]]

                if num_parts[0] == num_parts[1]:
                    invalid_ids.append(i)

        print(sum(invalid_ids))

def challenge2(input_file):
    with open(input_file+".txt", "r") as file:
        invalid_ids = []
        ranges = file.readline().strip().split(",")
        for r in ranges:
            start, end = map(int, r.split("-"))

            for i in range(start, end + 1):
                num = str(i)
                p = 1
                repeated_num = None

                while p < len(num):
                    if num[0:p] == num[p:p+p]:
                        repeated_num = num[0:p]

                        if ''.join(num.split(repeated_num)) == '':
                            invalid_ids.append(int(num))
                            break

                    p += 1

        print(sum(invalid_ids))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 2 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
