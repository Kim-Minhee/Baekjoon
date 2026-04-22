# Gemini 3.1 Pro
import sys

def solve():
    # 입력받은 문자열의 양옆 공백 및 줄바꿈 제거
    target = sys.stdin.readline().strip()
    if not target:
        return

    total_time = 0
    current = 'A'  # 처음 화살표는 'A'를 가리킵니다.

    for char in target:
        # 아스키코드 값을 이용해 두 문자 사이의 절대적 거리를 구합니다.
        diff = abs(ord(char) - ord(current))

        # 정방향 거리와 역방향 거리(26 - diff) 중 더 짧은(최솟값) 거리를 더합니다.
        total_time += min(diff, 26 - diff)

        # 문자를 출력했으므로 현재 위치를 갱신합니다.
        current = char

    print(total_time)

if __name__ == "__main__":
    solve()