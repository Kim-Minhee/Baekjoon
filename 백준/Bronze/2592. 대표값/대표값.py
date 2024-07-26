# 입력
num_dict, num_list = dict(), list()
for _ in range(10):
  n = int(input())
  if n in num_dict.keys():
    num_dict[n] += 1
  else:
    num_dict[n] = 0
  num_list.append(n)

# 풀이
r1 = sum(num_list)//10
m = max(num_dict.values())
for n in num_dict.keys():
  if num_dict[n]==m:
    r2 = n
    break

# 출력
print(r1)
print(r2)