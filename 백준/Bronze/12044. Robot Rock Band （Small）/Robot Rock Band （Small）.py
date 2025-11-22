# Gemini 3 Pro
import sys
from collections import defaultdict

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    Xorbitant 로봇 밴드 문제 해결 함수
    Meet-in-the-middle 알고리즘을 사용하여 O(N^2) 시간 복잡도로 해결합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스 수 T를 읽습니다.
        line = input().strip()
        if not line:
            return
        T = int(line)
    except ValueError:
        return

    for i in range(1, T + 1):
        try:
            # 각 테스트 케이스의 N과 K를 읽습니다.
            line = input().strip()
            while not line: # 빈 줄 처리
                line = input().strip()
            N, K = map(int, line.split())
            
            # 4개의 리스트 A, B, C, D를 읽습니다.
            A = list(map(int, input().split()))
            B = list(map(int, input().split()))
            C = list(map(int, input().split()))
            D = list(map(int, input().split()))
            
            # 1단계: A와 B 리스트의 모든 조합에 대해 XOR 값을 계산하고 빈도를 저장합니다.
            # 시간 복잡도: O(N^2)
            ab_xor_counts = defaultdict(int)
            for a in A:
                for b in B:
                    # a ^ b 값을 키로, 등장 횟수를 값으로 저장
                    ab_xor_counts[a ^ b] += 1
            
            ans = 0
            
            # 2단계: C와 D 리스트의 조합을 순회하며 필요한 값이 1단계 결과에 있는지 확인합니다.
            # 식: a ^ b ^ c ^ d = K  ==>  a ^ b = K ^ c ^ d
            # 즉, 우리가 1단계에서 저장한 (a ^ b) 값들 중 (K ^ c ^ d)와 같은 것이 몇 개인지 찾습니다.
            # 시간 복잡도: O(N^2)
            for c in C:
                for d in D:
                    target = K ^ c ^ d
                    # 딕셔너리에서 target 값의 빈도수를 조회 (없으면 0)
                    if target in ab_xor_counts:
                        ans += ab_xor_counts[target]
            
            # 결과 출력 형식: Case #x: y
            print(f"Case #{i}: {ans}")
            
        except ValueError:
            break

if __name__ == "__main__":
    solve()