for _ in range(int(input())):
  # 입력
  S = list(input().split())
  
  # 출력
  print(*S[2:], *S[:2])