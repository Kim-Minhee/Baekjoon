def change_string(s):
  change_indexes = [0]
  num_counts = []
  for i in range(1, len(s)):
    if s[i]!=s[i-1]:
      num_counts.append(i-change_indexes[-1])
      change_indexes.append(i)
  num_counts.append(len(s)-change_indexes[-1])

  new_s = ''
  for i in range(len(num_counts)):
    new_s += str(num_counts[i])
    new_s += str(s[change_indexes[i]])

  return new_s

N = int(input())
s = input()
for _ in range(N):
  s = change_string(s)

print(s)