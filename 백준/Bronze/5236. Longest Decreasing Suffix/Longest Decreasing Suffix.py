for _ in range(int(input())):
  S = input()

  r = S[-1]
  for i in range(-2, -len(S)-1, -1):
    if ord(S[i])>ord(S[i+1]):
      r = S[i]+r
    else:
      break

  print(f'The longest decreasing suffix of {S} is {r}', )