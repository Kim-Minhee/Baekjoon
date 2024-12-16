import re

N, S = int(input()), input()

cnt = 0
if len(S)==len(re.sub('[A-Z]', '', S)): # 대문자 포함 X
  cnt += 1
if len(S)==len(re.sub('[a-z]', '', S)): # 소문자 포함 X
  cnt += 1
if len(S)==len(re.sub('[0-9]', '', S)): # 숫자 포함 X
  cnt += 1
if len(S)==len(re.sub('[!@#$%^&*()-+]', '', S)): # 특수문자 포함 X
  cnt += 1
if cnt+len(S)<6:
  cnt += 6-cnt-len(S)

print(cnt)