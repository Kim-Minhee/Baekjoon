n = int(input())
d = list(input())
c = [d.count('N'), d.count('S'), d.count('W'), d.count('E')]
print(n-max(c))