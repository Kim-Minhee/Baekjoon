def is_american(word):
  if len(word)<=4:
    return False
  
  vowel = 'aeiouy'
  if word[-3] not in vowel and word[-2:]=='or':
    return True
  
  return False

while True:
  W = input()
  if W=='quit!':
    break
  
  if is_american(W):
    print(W[:-2]+'our')
  else:
    print(W)