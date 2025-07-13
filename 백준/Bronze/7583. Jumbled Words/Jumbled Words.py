while True:
  S = input()
  if S=='#': break

  jumbled = []
  for word in S.split():
    if len(word)<3:
      jumbled_word = word
    else:
      jumbled_word = word[0]
      jumbled_word += word[-2:0:-1]
      jumbled_word += word[-1]
    jumbled.append(jumbled_word)
  
  print(' '.join(jumbled))