# 입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 풀이
winner = list()
a, b = 0, 0
for i in range(10):
  if A[i]>B[i]:
    a += 3
    winner.append('A')
  elif A[i]<B[i]:
    b += 3
    winner.append('B')
  else:
    a += 1
    b += 1
    winner.append('D')

if a>b:
  win = 'A'
elif b>a:
  win = 'B'
else:
  if winner.count('D')==10:
    win = 'D'
  else:
    for w in winner[::-1]:
      if w!='D':
        win = w
        break

# 출력
print(a, b)
print(win)