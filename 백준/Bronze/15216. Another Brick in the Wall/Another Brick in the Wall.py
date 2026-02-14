# GPT 5.1
import sys
input = sys.stdin.readline

h, w, n = map(int, input().split())
bricks = list(map(int, input().split()))

current_layer = 1
remain = w

for brick in bricks:
    if brick <= remain:
        remain -= brick
        
        if remain == 0:
            current_layer += 1
            remain = w
            
            if current_layer > h:
                print("YES")
                exit()
    else:
        print("NO")
        exit()

# 벽돌 다 썼는데 아직 벽 완성 못함
print("NO")