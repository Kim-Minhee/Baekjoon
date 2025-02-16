S = input()

korea = 'KOREA'
r = ''
i = 0
for s in S:
  if i>4: i = 0
  if korea[i]==s:
    r += s
    i += 1

print(len(r))