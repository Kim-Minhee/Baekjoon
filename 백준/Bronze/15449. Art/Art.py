# Gemini 3 Pro
import sys

def solve():
    # 입력 받기
    # 공백으로 구분된 5개의 정수를 리스트로 변환
    try:
        sticks = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    count = 0
    n = 5 # 막대 개수는 항상 5개

    # 3개의 막대를 고르는 모든 조합 확인 (i < j < k)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 선택된 세 막대의 길이
                a = sticks[i]
                b = sticks[j]
                c = sticks[k]
                
                # 삼각형 조건 검사
                # 가장 긴 변 찾기
                max_len = max(a, b, c)
                # 세 변의 합
                sum_len = a + b + c
                
                # (나머지 두 변의 합) > (가장 긴 변) 조건
                # 전체 합에서 가장 긴 변을 빼면 나머지 두 변의 합이 됨
                if (sum_len - max_len) > max_len:
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    solve()