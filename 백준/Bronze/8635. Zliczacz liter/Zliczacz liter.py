letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
counts = [0]*len(letters)

for _ in range(int(input())):
  S = input()
  for letter in S:
    if letter!=' ':
      counts[letters.index(letter)] += 1

for idx, cnt in enumerate(counts):
  if cnt!=0:
    print(letters[idx], cnt)