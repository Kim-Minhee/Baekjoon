s = list(map(int, input().split()))
s.sort()
r = 2*s[2]-s[0]-s[1]
print(r)