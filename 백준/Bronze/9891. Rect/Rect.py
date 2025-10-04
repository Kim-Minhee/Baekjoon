# Gemini 2.5 Pro
import sys

# 펜윅 트리(Fenwick Tree) 또는 바이너리 인덱스 트리(BIT) 구현
class FenwickTree:
    """ 펜윅 트리 자료구조 """
    def __init__(self, size):
        # 트리는 1-based 인덱스를 사용하므로, 실제 크기보다 1 크게 생성합니다.
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        """ index에 value를 더합니다. """
        # public 인터페이스는 0-based, 내부적으로는 1-based로 변환합니다.
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        """ 0부터 index까지의 누적 합을 구합니다. """
        # public 인터페이스는 0-based, 내부적으로는 1-based로 변환합니다.
        index += 1
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & -index
        return s

def solve():
    """ 메인 로직을 처리하는 함수 """
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print(0)
            return
    except (ValueError, IndexError):
        print(0)
        return

    rectangles = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        # (짧은 변, 긴 변) 형태로 표준화하여 저장
        rectangles.append((min(w, h), max(w, h)))

    # 짧은 변(s)은 내림차순, 긴 변(l)은 오름차순으로 정렬
    rectangles.sort(key=lambda x: (-x[0], x[1]))

    # 좌표의 최대값은 10000이므로, 펜윅 트리의 크기를 10001로 설정
    MAX_COORD = 10001
    bit = FenwickTree(MAX_COORD)

    incomparable_pairs = 0
    i = 0
    while i < n:
        # 같은 s값을 가지는 직사각형 블록을 찾습니다.
        j = i
        while j < n and rectangles[j][0] == rectangles[i][0]:
            j += 1

        # 1단계: 쿼리 (s값이 더 큰 직사각형들과 비교)
        # 현재 블록의 각 직사각형에 대해, 이전에 처리된 (s값이 더 큰) 직사각형들 중
        # l값이 더 작은 것들의 개수를 셉니다.
        for k in range(i, j):
            s_k, l_k = rectangles[k]
            if l_k > 0:
                # l_k보다 '작은' l값을 가진 것들의 개수를 쿼리
                count = bit.query(l_k - 1)
                incomparable_pairs += count

        # 2단계: 업데이트
        # 현재 블록의 모든 직사각형들의 l값을 펜윅 트리에 추가합니다.
        for k in range(i, j):
            s_k, l_k = rectangles[k]
            bit.update(l_k, 1)

        # 다음 블록으로 인덱스를 이동합니다.
        i = j

    print(incomparable_pairs)

# 메인 함수 실행
solve()