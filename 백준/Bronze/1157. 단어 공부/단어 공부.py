import string

alphabet = list(string.ascii_uppercase)
counting = [0 for i in range(26)]

s = input()
s = s.upper()
for a in s:
  counting[alphabet.index(a)] += 1

counting_re = sorted(counting, reverse=True)
max_val = -1
if counting_re[0]!=counting_re[1]: max_val = counting_re[0]
if max_val == -1:
  print('?')
else:
  print(alphabet[counting.index(max_val)])