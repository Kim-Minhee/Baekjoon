import re

r = ''
for _ in range(int(input())):
  S = input()
  if r=='' and len(S)<=10:
    s1 = re.sub(r'[0-9]', '', S)
    s2 = re.sub(r'[^A-Z]', '', S)
    s3 = re.sub(r'[^a-z]', '', S)
    if len(s1)>0 and len(s2)<=len(s3):
      r = S

print(r)