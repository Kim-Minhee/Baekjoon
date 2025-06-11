N = input()

roman_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

r = 0
for i in range(0, len(N), 2):
  n = int(N[i])*roman_num[N[i+1]]
  if i+3<=len(N) and roman_num[N[i+1]]<roman_num[N[i+3]]:
    r -= n
  else:
    r += n

print(r)