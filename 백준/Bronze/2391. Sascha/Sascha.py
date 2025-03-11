import sys

# 테스트 케이스 개수
for _ in range(int(sys.stdin.readline().strip())):
    S = sys.stdin.readline().strip()  # Sascha가 발음한 단어
    w = int(sys.stdin.readline().strip())  # 사전 단어 개수
    
    min_cnt = len(S) + 1  # 최소 변경 횟수 (최대 변경 횟수보다 1 크게 설정)
    r = ""  # 가장 가능성이 높은 단어

    # 사전 단어 비교
    for _ in range(w):
        D = sys.stdin.readline().strip()
        cnt = sum(1 for j in range(len(S)) if S[j] != D[j])  # 다르면 +1

        # ✅ 최소 변경 횟수 갱신 (동일한 경우에는 기존 단어 유지)
        if cnt < min_cnt:
            min_cnt = cnt
            r = D

    # 결과 출력
    print(r)
