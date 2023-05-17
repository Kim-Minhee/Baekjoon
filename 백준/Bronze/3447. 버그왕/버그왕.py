import sys
code = sys.stdin.readlines()
out = list()

for c in code:
  while True:
    if 'BUG' in c:
      c = c.replace('BUG', '')
    else:
      print(c, end='')
      break