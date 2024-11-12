# 함수
def bin_and(a, b):
  r = ''
  for i in range(len(a)):
    if a[i]==b[i]=='1': r += '1'
    else: r += '0'
  return r

def bin_or(a, b):
  r = ''
  for i in range(len(a)):
    if a[i]==b[i]=='0': r += '0'
    else: r += '1'
  return r

def bin_nor(a, b):
  r = ''
  for i in range(len(a)):
    if a[i]!=b[i]: r += '1'
    else: r += '0'
  return r

def bin_not(a):
  r = ''
  for i in range(len(a)):
    if a[i]=='0': r += '1'
    else: r += '0'
  return r

# 입력
fill_num = 100000
A, B = input().zfill(fill_num), input().zfill(fill_num)

# 풀이
r1 = bin_and(A, B)
r2 = bin_or(A, B)
r3 = bin_nor(A, B)
r4 = bin_not(A)
r5 = bin_not(B)

# 출력
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)