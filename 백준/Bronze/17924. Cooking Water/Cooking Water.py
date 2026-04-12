# Gemini 3.1 Pro
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline

    n_str = input().strip()
    if not n_str:
        return
    n = int(n_str)

    # 겹치는 구간을 찾기 위한 초기값 설정
    # a의 최댓값을 찾기 위해 가장 작은 수 0으로 초기화
    # b의 최솟값을 찾기 위해 문제의 최댓값 1000으로 초기화
    max_a = 0
    min_b = 1000

    for _ in range(n):
        a, b = map(int, input().split())

        # 시작 시간 중 가장 늦은 시간 갱신
        if a > max_a:
            max_a = a

        # 끝나는 시간 중 가장 이른 시간 갱신
        if b < min_b:
            min_b = b

    # 공통으로 겹치는 구간이 존재하는지 판별
    if max_a <= min_b:
        print("gunilla has a point")
    else:
        print("edward is right")

if __name__ == '__main__':
    solve()