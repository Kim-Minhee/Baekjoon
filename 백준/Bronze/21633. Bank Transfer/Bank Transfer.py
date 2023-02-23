k = int(input())
f = k*0.01+25
if f<100:
  f = 100
elif f>2000:
  f = 2000
print(f'{f:.2f}')