# 입력
N, M = map(int, input().split())

# 풀이
box = [x for x in range(1, N+1)]
for _ in range(M):
  I, J, K = map(int, input().split())
  temp = box[:I-1]+box[K-1:J]+box[I-1:K-1]+box[J:]
  box = temp

# 출력
print(*box)