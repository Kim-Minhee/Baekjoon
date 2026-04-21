# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 펭귄 위치 찾기
K = A.index(-1)

# 왼쪽 최소
left_min = min(A[:K])

# 오른쪽 최소
right_min = min(A[K+1:])

print(left_min + right_min)