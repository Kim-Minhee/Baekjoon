S = input()

r = S[0]
for s in S[1:]:
  if s!=r[-1]:
    r += s

print(r)