# GPT 5
import sys
input = sys.stdin.readline

# S_n의 길이: |S_n| = 2^n - 1
# googol = 10^100 이라서 n=100이면 충분히 큼
MAX_N = 100
lengths = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    lengths[i] = (1 << i) - 1  # 2^i - 1


def kth_char(K: int) -> str:
    # S_n 중에서 K번째를 보고 싶은데,
    # n은 충분히 크게(길이가 K 이상 되도록) 잡으면 됨
    n = 1
    while lengths[n] < K:
        n += 1

    flip = False  # switch가 몇 번 적용되었는지 (홀수번이면 뒤집힘)

    while n > 1:
        L = lengths[n - 1]     # 왼쪽 S_{n-1} 길이
        mid = L + 1            # 가운데 '0'의 위치

        if K == mid:
            # 가운데에 있는 문자: 항상 '0'
            return '1' if flip else '0'
        elif K < mid:
            # 왼쪽 S_{n-1} 부분 → 구조 동일, n만 줄임
            n -= 1
        else:
            # 오른쪽 switch(reverse(S_{n-1})) 부분
            # 오른쪽에서의 위치를 왼쪽 S_{n-1}의 "대칭 위치"로 변환
            pos_in_right = K - mid           # 1 ~ L
            K = L - pos_in_right + 1        # reverse 때문에 뒤에서부터
            flip = not flip                 # switch 한 번 적용됨
            n -= 1

    # n == 1 이면 S_1 = "0" (길이 1, 문자 '0')
    # flip 여부에 따라 최종 값 결정
    return '1' if flip else '0'


T = int(input().strip())
for t in range(1, T + 1):
    K = int(input().strip())
    ans = kth_char(K)
    print(f"Case #{t}: {ans}")