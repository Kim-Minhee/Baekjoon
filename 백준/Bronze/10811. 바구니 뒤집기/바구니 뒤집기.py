# 입력
N, M = map(int, input().split())

# 풀이
box = [x for x in range(1, N+1)]
for _ in range(M):
  I, J = map(int, input().split())
  temp = box[:I-1]
  for t in box[I-1:J][::-1]:
    temp.append(t)
  temp += box[J:]
  box = temp

# 출력
print(*box)