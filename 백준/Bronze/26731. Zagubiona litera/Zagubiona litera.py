from string import ascii_uppercase
a = list(ascii_uppercase)
s = list(input())
for a_ in a:
  if a_ not in s:
    print(a_)