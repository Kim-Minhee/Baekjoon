# GPT 5
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()

m = N // 4

Q1 = S[0:m]
Q2 = S[m:2*m]
Q3 = S[2*m:3*m]
Q4 = S[3*m:4*m]

r = K % 3

if r == 0:
    result = Q1 + Q2 + Q3 + Q4
elif r == 1:
    result = Q1 + Q4 + Q2 + Q3
else:  # r == 2
    result = Q1 + Q3 + Q4 + Q2

print(result)