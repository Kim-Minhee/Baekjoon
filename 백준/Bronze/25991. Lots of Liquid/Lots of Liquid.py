n = int(input())
c = list(map(float, input().split()))
hap = 0
for i in c:
  hap += i**3
print(hap**(1/3))