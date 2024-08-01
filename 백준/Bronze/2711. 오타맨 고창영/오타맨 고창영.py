for _ in range(int(input())):
  # 입력
  I, S = map(str, input().split())

  # 풀이
  i = int(I)-1
  r = S[:i]+S[i+1:]

  # 출력
  print(r)