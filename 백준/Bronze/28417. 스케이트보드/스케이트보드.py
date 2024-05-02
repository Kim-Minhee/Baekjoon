s = list()
for _ in range(int(input())):
  S = list(map(int, input().split()))
  h = max(S[0], S[1])
  S = S[2:]
  S.sort()
  h += S[-2]
  h += S[-1]
  s.append(h)
print(max(s))