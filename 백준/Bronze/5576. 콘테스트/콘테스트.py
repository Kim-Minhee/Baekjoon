# 입력
W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]

# 풀이
W.sort(reverse=True)
K.sort(reverse=True)
w = sum(W[:3])
k = sum(K[:3])

# 출력
print(w, k)