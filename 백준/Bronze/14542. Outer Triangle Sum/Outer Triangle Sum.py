import sys
input = sys.stdin.readline

t = 1
while True:
    N = int(input().strip())
    if N == 0:
        break
    sum_tri = 0
    for n in range(N):
        nums = list(map(int, input().split()))
        if 0 < n < N - 1:
            sum_tri += nums[0] + nums[-1]
        else:
            sum_tri += sum(nums)
    print(f'Case #{t}:{sum_tri}')
    t += 1