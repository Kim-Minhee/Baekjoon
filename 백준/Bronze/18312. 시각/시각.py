N, K = map(int, input().split())

cnt = 0
for h in range(N+1):
  for m in range(60):
    for s in range(60):
      sh, sm, ss = str(h), str(m), str(s)
      if h<10: sh = '0'+sh
      if m<10: sm = '0'+sm
      if s<10: ss = '0'+ss
      time = sh+sm+ss
      if str(K) in time: cnt += 1

print(cnt)