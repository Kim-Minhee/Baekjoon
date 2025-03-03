def check_ana(s):
  if len(s)<3: return False
  if s.count('N')!=1: return False
  return True

N = int(input())
S = input()

cnt = 0
if N>=3 and S.count('A')>=2 and S.count('N')>=1:
  index_a = [i for i, s in enumerate(S) if s=='A']
  for i in range(len(index_a)-1):
    start_a = index_a[i]
    end_a = index_a[i+1]
    if check_ana(S[start_a:end_a+1]):
      cnt += 1

print(cnt)