# Gemini 3 Pro
import sys

def solve():
    # 입력 N 받기
    n = int(sys.stdin.readline())

    line = 1
    # N이 현재 줄(line)의 개수보다 크다면
    # 그만큼 빼고 다음 줄로 넘어감
    while n > line:
        n -= line
        line += 1

    # 반복문이 끝나면:
    # line: N번째 분수가 속한 대각선 줄 번호
    # n: 그 줄에서 몇 번째인지 (인덱스)
    
    # 규칙: 분자 + 분모 = line + 1
    # 분자는 내림차순 (line -> 1), 분모는 오름차순 (1 -> line)
    numerator = line - n + 1
    denominator = n

    print(f"{numerator} {denominator}")

if __name__ == "__main__":
    solve()