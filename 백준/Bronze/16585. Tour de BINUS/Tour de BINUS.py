# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

x1, d1 = input().split()
x1 = int(x1)

x2, d2 = input().split()
x2 = int(x2)

# Ayu
students = 0
if d1 == "left":
    for i in range(x1-1, -1, -1):
        students += A[i]
else:
    for i in range(x1-1, N):
        students += A[i]

# Budi
empty = 0
if d2 == "left":
    for i in range(x2-1, -1, -1):
        if A[i] == 0:
            empty += 1
else:
    for i in range(x2-1, N):
        if A[i] == 0:
            empty += 1

print(students, empty)