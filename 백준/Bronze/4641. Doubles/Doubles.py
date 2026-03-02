import sys
input = sys.stdin.readline

while True:
    D = input().strip()
    if D == '-1':
        break
    nums = list(map(int, D.split()))
    cnt = 0
    for num in nums[:-1]:
        if num * 2 in nums:
            cnt += 1
    print(cnt)