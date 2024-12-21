N, S = int(input()), list(input())

ran = int()
if N%2==0: ran = N//2+1
else: ran = N//2+2

for i in range(1, ran):
  if S[i-1]==S[-i]=='?':
    S[i-1] = 'a'
    S[-i] = 'a'
  elif S[i-1]=='?':
    S[i-1] = S[-i]
  elif S[-i]=='?':
    S[-i] = S[i-1]

print(''.join(S))