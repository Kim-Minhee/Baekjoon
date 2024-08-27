# 입력
STRING = list(input().split())

# 풀이
ignore = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
r = STRING[0][0].upper()
for s in STRING[1:]:
  if s not in ignore:
    r += s[0].upper()

# 출력
print(r)