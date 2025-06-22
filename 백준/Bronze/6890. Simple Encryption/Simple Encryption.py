import re

KEY = input()
MSG = input()
msg = re.sub(r'[^A-Z]', '', MSG)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = len(KEY)

r = ''
for i in range(len(msg)):
  idx = alphabet.index(msg[i])
  move = alphabet.index(KEY[i%l])
  r += alphabet[(idx+move)%26]
  
print(r)