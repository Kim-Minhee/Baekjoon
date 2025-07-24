max_len = 0

for _ in range(int(input())):
  NAME = input()
  name_len = len(set(NAME))
  max_len = max(name_len, max_len)

print(max_len)