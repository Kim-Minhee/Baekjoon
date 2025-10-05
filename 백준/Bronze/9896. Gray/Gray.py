import sys
input = sys.stdin.readline

N = int(input())
B = input()

gray = B[0]
for i in range(1, N):
    b = int(B[i - 1]) + int(B[i])
    if b == 1:
        gray += '1'
    else:
        gray += '0'
print(gray)