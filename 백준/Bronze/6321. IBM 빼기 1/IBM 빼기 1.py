import string
eng = [i for i in string.ascii_uppercase]
eng.append('A')
n = int(input())
for i in range(1, n+1):
  name = input()
  name = name.upper()
  name_ = str()
  for n in name:
    name_ += eng[eng.index(n)+1]
  print(f'String #{i}')
  print(name_)
  if i!=n:
    print()