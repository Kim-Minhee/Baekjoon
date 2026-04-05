# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    # n이 짝수이면 자르는 횟수(n-1)가 홀수이므로 선공인 Alice가 무조건 승리합니다.
    if n % 2 == 0:
        print("Alice")
        # Alice가 이길 운명이라면 어떻게 잘라도 이기므로,
        # 조건(1 <= 출력 <= n-1)을 만족하는 가장 만만한 수인 1을 출력합니다.
        print(1)

    # n이 홀수이면 자르는 횟수(n-1)가 짝수이므로 후공인 Bob이 무조건 승리합니다.
    else:
        print("Bob")

if __name__ == '__main__':
    solve()