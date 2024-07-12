import string

# 입력
S = input()

# 풀이
n = 0
for s in S:
  if s in string.ascii_lowercase:
    n += ord(s)-96
  else:
    n += ord(s)-38

is_prime = [False]+[True]*(52*len(S))
for i in range(2, len(is_prime)):
  if is_prime[i]:
    for j in range(2*i, len(is_prime), i):
      if is_prime[j]: is_prime[j] = False

# 출력
if is_prime[n]:
  print('It is a prime word.')
else:
  print('It is not a prime word.')