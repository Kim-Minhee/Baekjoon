# 입력
num = list()
for _ in range(5):
  num.append(int(input()))

# 풀이
num.sort()
r1 = sum(num)//5
r2 = num[2]

# 출력
print(r1)
print(r2)