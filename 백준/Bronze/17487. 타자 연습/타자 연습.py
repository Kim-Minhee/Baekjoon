left_lower, left_upper = 'qwertyasdfgzxcvb', 'QWERTYASDFGZXCVB'
right_lower, right_upper = 'uiophjklnm', 'UIOPHJKLNM'
left, right, both = 0, 0, 0

S = input()
for s in S:
  if s==' ': both += 1
  elif s in left_lower: left += 1
  elif s in right_lower: right += 1
  else:
    both += 1
    if s in left_upper: left += 1
    else: right += 1

while both>0:
  if left<=right: left += 1
  else: right += 1
  both -= 1

print(left, right)