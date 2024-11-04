for _ in range(int(input())):
  max_c, name = 0, ''
  for _ in range(int(input())):
    # 입력
    C, N = map(str, input().split())
    
    # 풀이
    if int(C)>max_c:
      max_c = int(C)
      name = N

  # 출력
  print(name)