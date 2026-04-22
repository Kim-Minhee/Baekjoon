import sys
input = sys.stdin.readline

S = input().strip()
cur_s = 'A'
total_time = 0
for s in S:
    time = abs(ord(s) - ord(cur_s))
    if time > 13:
        time = 26 - time
    total_time += time
    cur_s = s
print(total_time)