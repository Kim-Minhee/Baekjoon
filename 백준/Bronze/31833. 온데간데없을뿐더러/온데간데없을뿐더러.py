N = int(input())
A = list(input().split())
B = list(input().split())
a, b = '', ''
for i in A:
  a += i
for j in B:
  b += j
print(min(int(a), int(b)))