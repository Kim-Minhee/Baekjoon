# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    n = int(input_data[0])
    s = input_data[1]

    # 내장 메서드 replace를 사용하여 'joi'를 'JOI'로 모두 치환합니다.
    result = s.replace('joi', 'JOI')

    # 결과 출력
    print(result)

if __name__ == "__main__":
    solve()