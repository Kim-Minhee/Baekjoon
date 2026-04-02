# GPT 5
import sys
input = sys.stdin.readline

N = int(input())

def get_bottle(k):
    if k == 0:
        return "no more bottles"
    elif k == 1:
        return "1 bottle"
    else:
        return f"{k} bottles"

for k in range(N, 0, -1):
    print(f"{get_bottle(k)} of beer on the wall, {get_bottle(k)} of beer.")
    
    next_k = k - 1
    print(f"Take one down and pass it around, {get_bottle(next_k)} of beer on the wall.")
    
    print()  # 빈 줄

# 마지막 부분
print("No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {get_bottle(N)} of beer on the wall.")