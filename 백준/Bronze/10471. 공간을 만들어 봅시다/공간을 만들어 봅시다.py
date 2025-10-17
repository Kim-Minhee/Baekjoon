# Gemini 2.5 Pro
import sys

def solve():
    """
    주어진 파티션 위치를 이용해 만들 수 있는 모든 방의 폭을 계산합니다.
    """
    try:
        # 전체 폭 W와 파티션의 개수 P를 읽습니다.
        w, p = map(int, sys.stdin.readline().split())

        # P개의 파티션 위치를 리스트로 읽어옵니다.
        # 입력에 파티션이 없을 수도 있으므로 예외 처리를 합니다.
        line = sys.stdin.readline()
        if line.strip():
            partitions = list(map(int, line.split()))
        else:
            partitions = []

        # 1. 모든 잠재적 칸막이 위치를 하나의 리스트에 모읍니다.
        #    (왼쪽 벽, 오른쪽 벽, 모든 파티션)
        all_locations = [0, w] + partitions

        # 3. 가능한 모든 폭을 중복 없이 저장하기 위해 set을 사용합니다.
        possible_widths = set()

        # 2. 모든 위치 쌍의 차이를 계산하여 가능한 방의 폭을 찾습니다.
        for i in range(len(all_locations)):
            for j in range(i + 1, len(all_locations)):
                width = abs(all_locations[i] - all_locations[j])
                possible_widths.add(width)

        # 4. 결과를 오름차순으로 정렬하여 출력합니다.
        sorted_widths = sorted(list(possible_widths))

        # * 연산자는 리스트의 각 요소를 공백으로 구분하여 출력해줍니다.
        print(*sorted_widths)

    except (ValueError, IndexError):
        # 입력이 비어있는 경우를 대비한 예외 처리입니다.
        pass

# 메인 함수 실행
solve()