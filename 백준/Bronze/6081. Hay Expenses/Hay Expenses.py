# Gemini
N, Q = map(int, input().split())

h_counts = [0] # 0번째 인덱스는 사용하지 않음 (1-기반 인덱싱을 위해)
for _ in range(N):
  h_counts.append(int(input()))

# 누적 합 배열 만들기
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
  prefix_sum[i] = prefix_sum[i-1] + h_counts[i]

# 쿼리 처리
for _ in range(Q):
  S, E = map(int, input().split())
  # S부터 E까지의 합 = (0부터 E까지의 합) - (0부터 S-1까지의 합)
  print(prefix_sum[E] - prefix_sum[S-1])