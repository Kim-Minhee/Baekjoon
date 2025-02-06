S = input()

score_dict = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
score_list = []
for s in S:
  if s=='+':
    score_list[-1] += 0.5
  else:
    score_list.append(score_dict[s])

print(sum(score_list)/len(score_list))