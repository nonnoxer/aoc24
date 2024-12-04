def check(g, i, j, x, y, dx, dy):
    for k, letter in zip(range(1, 4), list("MAS")):
        temp_i = i + k * dx
        temp_j = j + k * dy
        if temp_i < 0 or temp_i >= x:
            return 0
        if temp_j < 0 or temp_j >= y:
            return 0
        if g[temp_i][temp_j] != letter:
            return 0
    return 1


def part1(g):
    result = 0
    x = len(g)
    y = len(g[0])
    for i in range(x):
        for j in range(y):
            if g[i][j] != 'X':
                continue
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    result += check(g, i, j, x, y, dx, dy)
    return result


def check2(g, i, j, x, y, dx, dy):
    for k, letter in zip([-1, 1], list('MS')):
        temp_i = i + k * dx
        temp_j = j + k * dy
        if temp_i < 0 or temp_i >= x:
            return 0
        if temp_j < 0 or temp_j >= y:
            return 0
        if g[temp_i][temp_j] != letter:
            return 0
    return 1


def part2(g):
    result = 0
    x = len(g)
    y = len(g[0])
    for i in range(x):
        for j in range(y):
            if g[i][j] != 'A':
                continue
            temp_result = 0
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    temp_result += check2(g, i, j, x, y, dx, dy)
            if temp_result == 2:
                result += 1
    return result


f = open("day4.txt")
lines = f.readlines()
g = [list(line.strip()) for line in lines]

print(part1(g))
print(part2(g))