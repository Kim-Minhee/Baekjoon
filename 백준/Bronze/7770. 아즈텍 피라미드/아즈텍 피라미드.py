N = int(input())

N -= 1
floor = 1
while True:
    block = [i for i in range(1, 2 * (floor + 1), 2)]
    min_block = sum(block) + sum(block[:-1])
    N -= min_block
    if N < 0:
        break
    floor += 1

print(floor)