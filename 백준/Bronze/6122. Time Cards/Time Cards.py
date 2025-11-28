import sys
input = sys.stdin.readline

def cal_time(start_h, start_m, end_h, end_m):
    start_time = start_h * 60 + start_m
    end_time = end_h * 60 + end_m
    return end_time - start_time

N, L = map(int, input().split())
times = [0] * N
cows = [[] for _ in range(N)]
for _ in range(L):
    DATA = input().split()
    cow_idx = int(DATA[0]) - 1
    time = int(DATA[2]) * 60 + int(DATA[3])
    if DATA[1] == 'START':
        cows[cow_idx].append(time)
    else:
        times[cow_idx] += time - cows[cow_idx][0]
        cows[cow_idx] = []

for t in times:
    print(t // 60, t % 60)