import string

alpha = list(string.ascii_lowercase)

for _ in range(int(input())):
  # 입력
  S = input().lower()

  # 풀이  
  notin = []
  for a in alpha:
    if a not in S:
      notin.append(a)

  # 출력
  if len(notin)==0:
    print('pangram')
  else:
    print(f"missing {''.join(notin)}")