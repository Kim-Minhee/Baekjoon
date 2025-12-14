# Gemini 3 Pro
import sys
import math

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    주어진 점수 리스트에서 가장 작은 점수 차이를 찾아 출력하는 함수.
    정렬을 사용하여 효율적으로 O(N log N) 복잡도로 해결합니다.
    """
    # EOF가 0으로 명시되어 있으므로, 0이 입력될 때까지 반복합니다.
    while True:
        try:
            # 학생 수 N 입력
            line = input().strip()
            if not line:
                continue
            
            n = int(line)
            
            # 입력의 끝 조건 (0이 입력되면 종료)
            if n == 0:
                break
                
            # 학생들의 점수 리스트 입력
            # 입력 데이터가 한 줄에 공백으로 구분되어 있으므로, map(int, ...)로 바로 정수 리스트 생성
            scores = list(map(int, input().strip().split()))
            
        except EOFError:
            break
        except ValueError:
            # 입력 형식이 잘못된 경우 (예: 숫자가 아닌 문자열, 빈 줄 등) 무시하고 다음 루프로
            continue

        # 1. 점수 리스트 정렬 (O(N log N))
        scores.sort()
        
        # 2. 최소 차이를 찾기 위한 초기값 설정
        # 점수는 최대 1,000,000이므로, 초기값을 그보다 큰 값이나 무한대로 설정합니다.
        min_diff = math.inf
        
        # 3. 정렬된 리스트를 순회하며 이웃한 두 점수 간의 차이를 계산 (O(N))
        # 리스트가 2개 이상의 요소를 가지고 있다는 조건 (n >= 2)이 있으므로 안전합니다.
        for i in range(1, n):
            # scores[i]와 scores[i-1]은 정렬되어 있으므로 차이는 항상 양수입니다.
            diff = scores[i] - scores[i-1]
            
            # 최소 차이 업데이트
            if diff < min_diff:
                min_diff = diff
        
        # 결과 출력
        # 문제에서 N이 2 이상이므로 min_diff는 반드시 유한한 값입니다.
        print(min_diff)

if __name__ == "__main__":
    # 재귀 제한을 늘려주는 것은 선택사항이지만, 문제의 특성상 불필요할 수 있습니다.
    # sys.setrecursionlimit(10**6) 
    solve()