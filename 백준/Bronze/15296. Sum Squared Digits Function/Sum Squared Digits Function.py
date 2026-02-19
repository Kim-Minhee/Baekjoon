# GPT 5.1
import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    K, b, n = map(int, input().split())
    
    ssd = 0
    while n > 0:
        digit = n % b
        ssd += digit * digit
        n //= b
    
    print(K, ssd)