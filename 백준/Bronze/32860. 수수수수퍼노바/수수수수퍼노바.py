import string

N, M = map(int, input().split())

alphabet = list(string.ascii_lowercase)
r = str(N)
if M<=26:
  r += chr(M+64)
else:
  m = M-27
  r += alphabet[m//26]+alphabet[m%26]

print('SN', r)