# GPT 5
import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print("Alice")
    print(1)  # 1과 n-1로 나누기
else:
    print("Bob")