import sys
input = sys.stdin.readline

JU = list(map(int, input().split()))
UJ = list(map(int, input().split()))

JU.sort(reverse=True)
UJ.sort(reverse=True)
cnt = 0
for i in range(5):
    if JU[i] > UJ[i]:
        cnt += 1
print(cnt)