def shift_letters(word, num):
  return word[-num:]+word[:-num]

for _ in range(int(input())):
  W, N = input().split()
  shifted_word = shift_letters(W, int(N))
  print(f'Shifting {W} by {N} positions gives us: {shifted_word}')