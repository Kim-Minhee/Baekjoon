def check(s):
  if len(s)!=7: return False
  if len(set(s))!=2: return False
  if s[0]==s[1]==s[4] and s[2]==s[3]==s[5]==s[6]: return True
  else: return False

for _ in range(int(input())):
  N = input()
  chk = check(N)
  if chk: print(1)
  else: print(0)