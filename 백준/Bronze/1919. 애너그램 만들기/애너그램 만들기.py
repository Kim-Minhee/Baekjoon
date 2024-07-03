# 입력
A, B = list(input()), list(input())

# 풀이
b = len(B)
for a in A:
  if a in B:
    B.remove(a)
r = len(A)-b+2*len(B)

# 출력
print(r)