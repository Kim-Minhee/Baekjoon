while 1:
  # 입력
  S = input()
  if S=='#': break

  # 풀이
  vowels = 'aeiou'
  s = 0
  for i in range(len(S)):
    if S[i] in vowels:
      s = i
      break

  # 출력
  print(S[s:]+S[:s]+'ay')