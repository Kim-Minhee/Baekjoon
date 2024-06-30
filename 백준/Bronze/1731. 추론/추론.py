# 입력
l = list()
for _ in range(int(input())):
  l.append(int(input()))

# 풀이
q1 = l[1]-l[0]
q2 = l[2]-l[1]
if q1==q2:
  r = l[-1]+q1
else:
  r = int(l[-1]*(l[1]/l[0]))

# 출력
print(r)