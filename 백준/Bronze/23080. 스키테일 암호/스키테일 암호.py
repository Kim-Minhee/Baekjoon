K = int(input())
S = input()
r = str()
for s in S[::K]:
  r += s
print(r)