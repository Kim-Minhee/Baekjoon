# 입력
N, K = map(int, input().split())

# 풀이
max_r = 1
for k in range(1, K+1):
  r = int(str(N*k)[::-1])
  if r>max_r: max_r = r

# 출력
print(max_r)