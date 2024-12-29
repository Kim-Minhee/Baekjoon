N = list(input())

left, right = 0, 0
for l in N[:len(N)//2]: left += int(l)
for r in N[len(N)//2:]: right += int(r)

if left==right: print('LUCKY')
else: print('READY')