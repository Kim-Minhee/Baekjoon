import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    Smax, Shyness = input().split()
    standing = 0
    need = 0
    for shyness, people in enumerate(Shyness):
        if shyness > standing + need:
            need += shyness - (standing + need)
        standing += int(people)
    print(f'Case #{t}: {need}')