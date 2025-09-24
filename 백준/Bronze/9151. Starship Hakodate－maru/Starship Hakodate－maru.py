# Gemini 2.5 Pro
import sys
import bisect

def solve():
    """
    하코다테마루 연료 문제를 해결합니다.
    큐브 수와 사면체 수의 합으로 표현될 수 있는,
    주어진 값 이하의 가장 큰 수를 찾습니다.
    """
    # 1. 사전 계산 단계
    max_val = 151200
    
    # 151200 이하의 모든 큐브 수 생성
    cubes = []
    n = 0
    while True:
        cube = n ** 3
        if cube > max_val:
            break
        cubes.append(cube)
        n += 1

    # 151200 이하의 모든 사면체 수 생성
    tetrahedrals = []
    n = 0
    while True:
        tetra = n * (n + 1) * (n + 2) // 6
        if tetra > max_val:
            break
        tetrahedrals.append(tetra)
        n += 1
    
    # 가능한 모든 합을 set에 저장하여 중복을 제거
    possible_sums = set()
    for c in cubes:
        for t in tetrahedrals:
            s = c + t
            if s <= max_val:
                possible_sums.add(s)
    
    # 검색을 위해 정렬된 리스트로 변환
    sorted_sums = sorted(list(possible_sums))

    # 2. 입력 처리 단계
    while True:
        try:
            line = sys.stdin.readline()
            # 입력이 비어있으면 종료
            if not line:
                break
            
            m = int(line)
            
            # 종료 조건 확인
            if m == 0:
                break

            # 3. 이진 탐색으로 가장 큰 값 찾기
            # bisect_right는 m이 들어갈 오른쪽 위치(m보다 큰 첫 원소의 인덱스)를 찾습니다.
            idx = bisect.bisect_right(sorted_sums, m)
            
            # 따라서 m보다 작거나 같은 가장 큰 값은 그 바로 이전 인덱스에 있습니다.
            result = sorted_sums[idx - 1]
            print(result)

        except (ValueError, IndexError):
            # 입력이 잘못되거나 비어있는 경우 반복을 중단합니다.
            break

# 메인 함수 실행
solve()