import string
a = [i for i in string.ascii_uppercase]

S = input()
s, cnt = a.index(S), 0
for i in 'IILOVEYONSEI':
  cnt += abs(s - a.index(i))
  s = a.index(i)
print(cnt)