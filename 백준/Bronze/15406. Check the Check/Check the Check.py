# Gemini 3 Pro
import sys

def solve():
    # 빠른 입출력
    input = sys.stdin.readline

    actual_total = 0

    while True:
        line = input().strip()

        # 빈 줄 예외 처리 (만약의 경우를 대비)
        if not line:
            continue

        # "TOTAL"이 나오면 루프 종료
        if line == "TOTAL":
            # TOTAL 다음 줄은 웨이터가 계산한 총액
            waiter_total = int(input().strip())
            break

        # "TOTAL"이 아니라면 음식 이름이므로,
        # 바로 다음 줄에서 가격(p)과 수량(c)을 읽어옴
        p, c = map(int, input().split())

        # 실제 총액에 누적
        actual_total += p * c

    # 웨이터가 계산한 금액이 실제 금액보다 작거나 같으면 PAY, 크면 PROTEST
    if waiter_total <= actual_total:
        print("PAY")
    else:
        print("PROTEST")

if __name__ == '__main__':
    solve()