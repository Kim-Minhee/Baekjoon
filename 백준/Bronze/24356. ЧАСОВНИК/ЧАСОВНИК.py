t1, m1, t2, m2 = map(int, input().split())
if (t1*60+m1)>(t2*60+m2):
  t1 -= 24
m = (t2*60+m2)-(t1*60+m1)
n = m//30
print(m, n)