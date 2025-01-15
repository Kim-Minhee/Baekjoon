S = input()

trans = [{'B': 'A',
          'C': 'A',
          'D': 'A',
          'F': 'A'},
         {'C': 'B',
          'D': 'B',
          'F': 'B'},
         {'D': 'C',
          'F': 'C'}]

if 'A' in S:
  s_trans = S.maketrans(trans[0])
  print(S.translate(s_trans))
elif 'B' in S:
  s_trans = S.maketrans(trans[1])
  print(S.translate(s_trans))
elif 'C' in S:
  s_trans = S.maketrans(trans[2])
  print(S.translate(s_trans))
else:
  print('A'*len(S))