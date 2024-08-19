# 입력
N = int(input())
C = input()

# 풀이
adrina = 'ABC'*(N//3+1)
bruno = 'BABC'*(N//4+1)
goran = 'CCAABB'*(N//6+1)

a, b, g = 0, 0, 0
for i in range(N):
  if C[i]==adrina[i]:
    a += 1
  if C[i]==bruno[i]:
    b += 1
  if C[i]==goran[i]:
    g += 1

max_score = max(a, b, g)

# 출력
print(max_score)
if a==max_score:
  print('Adrian')
if b==max_score:
  print('Bruno')
if g==max_score:
  print('Goran')