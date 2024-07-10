# 입력
N = int(input())

# 풀이
a = 1/(2**N)
b = '{:.270f}'.format(a)
cnt = 0
for i in b[-1:0:-1]:
  if i=='0':
    cnt += 1
  else:
    break

# 출력
print(b[:len(b)-cnt])