# 입력
N = int(input())

# 풀이
if N%2==0: print('I LOVE CBNU')
else:
  print('*'*N)
  for i in range(N//2+1):
    s = ' '*(N//2-i)
    s += '*'
    if i>0:
      s += ' '*(2*i-1)
      s += '*'
    print(s)