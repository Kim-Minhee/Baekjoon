for _ in range(int(input())):
  S = input()

  change_num_index = [0]
  for i in range(1, len(S)):
    if S[i-1]!=S[i]:
      change_num_index.append(i)

  r = ''
  for index in range(len(change_num_index)-1):
    r += str(change_num_index[index+1]-change_num_index[index])
    r += str(S[change_num_index[index]])

  r += str(len(S)-change_num_index[-1])
  r += str(S[change_num_index[-1]])

  print(r)