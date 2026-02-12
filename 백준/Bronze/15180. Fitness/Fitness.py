import sys
input = sys.stdin.readline

S = int(input().strip())
visited = [S]
while True:
    N = input().strip()
    if N == '#':
        break
    
    d, s = N[0], int(N[1])
    if d == 'A':
        S -= s
    else:
        S += s
    if S <= 0:
        S += 8
    elif S > 8:
        S -= 8
    visited.append(S)

print(*visited, end=' ')
if len(visited) != len(set(visited)) or len(visited) < 5:
    print('reject')