# GPT 5
import sys
input = sys.stdin.readline

words = input().strip().split()

total = len(words)
cnt = sum(1 for w in words if "ae" in w)

if cnt * 100 >= total * 40:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")