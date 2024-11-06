# 입력
X = input()

# 풀이
if X[0]=='0':
  if X[1]=='x':
    r = int(X, 16)
  else:
    r = int(X, 8)
else:
  r = X

# 출력
print(r)