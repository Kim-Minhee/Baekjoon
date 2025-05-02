M, N = map(int, input().split())

hided, public = [], M
for _ in range(N):
  hided.append(public//N + public%N)
  public = public//N*(N-1)

hided.sort(reverse=True)
print(*hided)
print(public)