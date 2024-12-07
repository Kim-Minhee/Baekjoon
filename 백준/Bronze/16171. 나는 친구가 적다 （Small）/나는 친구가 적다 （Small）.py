import re

S, K = input(), input()

S = re.sub(r'[^a-zA-Z]', '', S)

if K in S:
  print(1)
else:
  print(0)