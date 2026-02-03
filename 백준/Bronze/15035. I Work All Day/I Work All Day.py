import sys
input = sys.stdin.readline

N = int(input().strip())
H = list(map(int, input().split()))
T = int(input().strip())

min_loss, r = T, int()
for h in H:
    loss = T % h
    if loss < min_loss:
        min_loss = loss
        r = h
print(r)