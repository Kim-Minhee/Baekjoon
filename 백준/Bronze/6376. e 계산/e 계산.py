import math

print(f'n e')
print(f'- -----------')
for n in range(10):
  e = 0
  for i in range(n+1):
    e += 1/math.factorial(i)
  if int(e)==e:
    e = int(e)
  if n<3:
    print(f'{n} {round(e, 1)}')
  else:
    print(f'{n} {e:.9f}')