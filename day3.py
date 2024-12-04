import re

def part1(s):
    pat = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(pat, s)
    result = 0
    for match in matches:
        a = int(match.group(1))
        b = int(match.group(2))
        result += a * b
    return result


def part2(s):
    pat = r"(?:do\(\)|^)(?:.*mul\(\d+,\d+\))*?.*?(?:don't()|$)"
    pat2 = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(pat, s)
    result = 0
    for match in matches:
        sub_matches = re.finditer(pat2, match.group(0))
        for sub_match in sub_matches:
            a = int(sub_match.group(1))
            b = int(sub_match.group(2))
            result += a * b
    return result


f = open("day3.txt")
s = f.read().replace("\n", "")

print(part1(s))
print(part2(s))