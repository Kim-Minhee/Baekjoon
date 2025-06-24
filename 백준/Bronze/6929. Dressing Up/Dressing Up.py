H = int(input())

ties = []
for i in range(H//2):
  tie = '*'*(2*i+1)
  tie += ' '*(2*H-4*i-2)
  tie += '*'*(2*i+1)
  print(tie)
  ties.append(tie)
print('*'*(2*H))
for tie in ties[::-1]:
  print(tie)