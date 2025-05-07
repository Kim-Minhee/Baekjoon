nums = {}

for _ in range(int(input())):
  N = int(input())
  if N in nums.keys():
    nums[N] += 1
  else:
    nums[N] = 1

max_cnt = max(nums.values())
min_key = max(nums.keys())
for (key, value) in nums.items():
  if value==max_cnt and key<min_key:
    min_key = key

print(min_key)