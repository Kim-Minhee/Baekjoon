def reverseLR(lst):
  reLst = list()
  r = len(lst)
  c = len(lst[0])
  for i in range(r):
    re = list()
    for j in range(c):
      re.append(lst[i][-j-1])
    reLst.append(re)
  return reLst

def reverseUD(lst):
  reLst = list()
  for i in range(len(lst)):
    reLst.append(lst[-i-1])
  return reLst

def concatLR(lstL, lstR):
  conLst = list()
  for i in range(len(lstL)):
    conLst.append(lstL[i]+lstR[i])
  return conLst

r, c = map(int, input().split())
designLU = list()
for _ in range(r):
  d = list(input())
  designLU.append(d)
error = list(map(int, input().split()))

designRU = reverseLR(designLU)
designLD = reverseUD(designLU)
designRD = reverseLR(designLD)
designU = concatLR(designLU, designRU)
designD = concatLR(designLD, designRD)
designF = designU + designD
e = designF[error[0]-1][error[1]-1]
if e=='#':
  designF[error[0]-1][error[1]-1] = '.'
elif e=='.':
  designF[error[0]-1][error[1]-1] = '#'

for i in range(len(designF)):
  print(''.join(designF[i]))