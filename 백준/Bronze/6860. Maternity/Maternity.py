MG, FG = list(input()), list(input())

dominant, recessive = 'ABCDE', 'abcde'
possible_genes = []
for i in range(0, 10, 2):
  g1 = recessive[i//2] if ''.join(MG[i] + FG[i]).islower() else dominant[i//2]
  g2 = recessive[i//2] if ''.join(MG[i] + FG[i+1]).islower() else dominant[i//2]
  g3 = recessive[i//2] if ''.join(MG[i+1] + FG[i]).islower() else dominant[i//2]
  g4 = recessive[i//2] if ''.join(MG[i+1] + FG[i+1]).islower() else dominant[i//2]
  possible_genes.append(set([g1, g2, g3, g4]))

for _ in range(int(input())):
  possible = True
  for idx, bg in enumerate(list(input())):
    if bg not in possible_genes[idx]:
      possible = False
  print('Possible baby.' if possible else 'Not their baby!')