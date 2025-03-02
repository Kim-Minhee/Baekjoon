darts = list(map(int, input().split()))

i = darts.index(20)
i_l, i_r = i-1, i+1
if i==0: i_l = 19
elif i==19: i_r = 0

a = (20+darts[i_l]+darts[i_r])/3
if a>10.5: print('Alice')
elif a<10.5: print('Bob')
else: print('Tie')