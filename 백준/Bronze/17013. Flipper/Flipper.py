import sys
input = sys.stdin.readline

nums = [[1, 2], [3, 4]]
for s in input().strip():
    if s == 'H':
        nums[0][0], nums[1][0] = nums[1][0], nums[0][0]
        nums[0][1], nums[1][1] = nums[1][1], nums[0][1]
    else:
        nums[0][0], nums[0][1] = nums[0][1], nums[0][0]
        nums[1][0], nums[1][1] = nums[1][1], nums[1][0]
for n1, n2 in nums:
    print(n1, n2)