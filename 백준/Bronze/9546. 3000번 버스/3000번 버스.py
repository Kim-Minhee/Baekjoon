for _ in range(int(input())):
  # 입력
  K = int(input())

  # 풀이
  n = 1
  for _ in range(K-1):
    n += 0.5
    n *= 2
    
  # 출력
  print(int(n))