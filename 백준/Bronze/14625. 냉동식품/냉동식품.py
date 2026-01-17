import sys
input = sys.stdin.readline

H1, M1 = input().split()
H2, M2 = input().split()
N = input().strip()

n_cnt = 0
for h in range(int(H1), int(H2) + 1):
    h = str(h).zfill(2)
    for m in range(0, 60):
        if int(h) == int(H1) and m < int(M1):
            continue
        elif int(h) == int(H2) and m > int(M2):
            break
        
        m = str(m).zfill(2)
        if N in h + m:
            n_cnt += 1
print(n_cnt)