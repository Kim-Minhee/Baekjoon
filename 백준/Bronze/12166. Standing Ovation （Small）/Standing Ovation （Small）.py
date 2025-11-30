# GPT 5.1
import sys
input = sys.stdin.readline

T = int(input().strip())

for t in range(1, T + 1):
    Smax, s = input().split()
    Smax = int(Smax)
    
    standing = 0
    friends = 0
    
    for k in range(Smax + 1):
        cnt = int(s[k])
        
        if standing < k:
            need = k - standing
            friends += need
            standing += need
        
        standing += cnt
    
    print(f"Case #{t}: {friends}")