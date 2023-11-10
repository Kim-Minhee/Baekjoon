t = int(input())
for i in range(t):
  n = int(input())
  if n<3:
    for _ in range(n):
      print('#'*n)
  else:
    print('#'*n)
    for _ in range(n-2):
      print('#'+'J'*(n-2)+'#')
    print('#'*n)
  if i!=t-1:
    print()