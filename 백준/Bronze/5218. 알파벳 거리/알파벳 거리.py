import string

for _ in range(int(input())):
  # 입력
  S1, S2 = map(str, input().split())
  
  # 풀이
  alphabet = ['']+list(string.ascii_uppercase)
  distances = list()
  for i in range(len(S1)):
    a1 = alphabet.index(S1[i])
    a2 = alphabet.index(S2[i])
    if a1>a2:
      a2 += 26
    distances.append(a2-a1)
  
  # 출력
  print('Distances:', *distances)