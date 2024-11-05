for _ in range(int(input())):
  # 입력
  S = list(input().split())

  # 풀이
  if S[0].lower()=='simon' and S[1].lower()=='says':

    # 출력
    print('', *S[2:])