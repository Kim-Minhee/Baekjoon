for _ in range(int(input())):
  # 입력
  N = int(input())
  S = list(map(int, input().split()))

  # 풀이
  r = 2*(max(S)-min(S))

  # 출력
  print(r)