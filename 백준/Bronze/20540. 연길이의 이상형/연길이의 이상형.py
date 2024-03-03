mbti = {
    'E':'I',
    'I':'E',
    'S':'N',
    'N':'S',
    'T':'F',
    'F':'T',
    'J':'P',
    'P':'J'
}
yg = input()
r = str()
for i in yg:
  r += mbti[i]
print(r)