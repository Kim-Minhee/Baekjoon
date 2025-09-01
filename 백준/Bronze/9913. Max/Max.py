from collections import Counter

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

counter = Counter(nums)
print(max(counter.values()))