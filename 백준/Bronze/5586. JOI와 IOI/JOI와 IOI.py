# 입력
S = input()

# 풀이
joi, ioi = 0, 0
for i in range(len(S)-2):
  s = S[i:i+3]
  if s=='JOI':
    joi += 1
  elif s=='IOI':
    ioi += 1

# 출력
print(joi)
print(ioi)