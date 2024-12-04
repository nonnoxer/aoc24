import heapq

def part1(l1, l2):
    heapq.heapify(l1)
    heapq.heapify(l2)
    result = 0
    for _ in range(len(l1)):
        a = heapq.heappop(l1)
        b = heapq.heappop(l2)
        if (a > b):
            result += a - b
        else:
            result += b - a
    return result

def part2(l1, l2):
    d1 = {}
    d2 = {}
    for n in l1:
        d1[n] = d1.get(n, 0) + 1
    for n in l2:
        d2[n] = d2.get(n, 0) + 1

    result = 0
    for n, a in d1.items():
        result += n * a * d2.get(n, 0)
    
    return result

l1 = []
l2 = []
f = open("day1.txt")
lines = f.readlines()
for line in lines:
    split = line.split("   ")
    l1.append(int(split[0]))
    l2.append(int(split[1]))

print(part1(l1.copy(), l2.copy()))
print(part2(l1, l2))