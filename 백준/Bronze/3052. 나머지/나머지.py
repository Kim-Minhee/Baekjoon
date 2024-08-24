remain = []

# 입력
for _ in range(10):
  N = int(input())
  remain.append(N%42)

# 풀이
remain = set(remain)

# 출력
print(len(remain))