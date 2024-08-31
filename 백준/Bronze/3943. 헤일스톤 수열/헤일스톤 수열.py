# 함수
def hsSeq(num):
  max_num = num
  while num not in [4, 2, 1]:
    if num%2==0:
      num //= 2
    else:
      num = num*3+1
    if num>max_num:
      max_num = num
  return max_num

# 입력
for _ in range(int(input())):
  N = int(input())

  # 풀이
  r = hsSeq(N)

  # 출력
  print(r)