c = int(input())
d = list(map(int, input().split()))
d.sort()
n = d[0]*d[-1]
print(n)