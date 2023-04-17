import math
cD = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
n = int(input())
cSum, sSum = 0, 0
for _ in range(n):
  t, c, s = map(str, input().split())
  cSum += int(c)
  score = cD[s[0]]
  if s[0]!='F':
    if s[1]=='+':
      score += 0.3
    elif s[1]=='-':
      score -= 0.3
  sSum += int(c)*score

avg = sSum/cSum
if (avg*1000)%10>=5:
  avg = (math.trunc(avg*100)+1)/100
else:
  avg = math.trunc(avg*100)/100
print(f'{avg:.2f}')