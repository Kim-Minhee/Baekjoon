# 입력
for _ in range(int(input())):
  A, B = input(), input()

  # 풀이
  cnt = 0
  for i in range(len(A)):
    if A[i]!=B[i]:
      cnt += 1

  # 출력
  print(f'Hamming distance is {cnt}.')