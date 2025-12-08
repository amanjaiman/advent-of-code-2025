import argparse
import math
from collections import defaultdict


def challenge1(input_file):
    to_connect = 1000 # 10 for test_input
    with open(input_file + '.txt', 'r') as file:
        points = [list(map(int, line.strip().split(','))) for line in file]

    n = len(points)

    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.dist(points[i], points[j])
            distances.append((dist, i, j))

    distances.sort()

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for dist, i, j in distances[:to_connect]:
        union(i, j)

    sizes = defaultdict(int)
    for i in range(n):
        sizes[find(i)] += 1

    top_3 = sorted(sizes.values(), reverse=True)[:3]
    print(math.prod(top_3))


def challenge2(input_file):
    with open(input_file + '.txt', 'r') as file:
        points = [list(map(int, line.strip().split(','))) for line in file]

    n = len(points)

    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.dist(points[i], points[j])
            distances.append((dist, i, j))

    distances.sort()

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    num_components = n
    last_i, last_j = 0, 0

    for dist, i, j in distances:
        if union(i, j):
            num_components -= 1
            last_i, last_j = i, j
            if num_components == 1:
                break

    print(points[last_i][0] * points[last_j][0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 8 Advent of Code')
    parser.add_argument('--challenge', type=int, required=True, choices=[1, 2],
                        help='Challenge number (1 or 2)')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file')
    
    args = parser.parse_args()
    
    if args.challenge == 1:
        challenge1(args.input)
    elif args.challenge == 2:
        challenge2(args.input)
