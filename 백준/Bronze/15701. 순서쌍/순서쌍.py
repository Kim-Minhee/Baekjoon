# 입력
N = int(input())

# 풀이
d = []
for n in range(1, int(N**(1/2))+1):
  if N%n==0:
    d.append(n)
    if N//n not in d:
      d.append(N//n)

# 출력
print(len(d))