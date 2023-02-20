a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
o1, o2 = a, b
if t>30:
  o1 += ((t-30)*x)*21
  if t>45:
    o2 = b + ((t-45)*y)*21
print(o1, o2)