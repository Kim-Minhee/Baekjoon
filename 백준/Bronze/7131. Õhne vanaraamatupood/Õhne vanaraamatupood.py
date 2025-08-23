# GPT 4o
from decimal import Decimal, ROUND_HALF_UP, getcontext

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    it = iter(data)

    getcontext().prec = 50  # 여유 있는 정밀도

    N = int(next(it))
    P0 = Decimal(next(it))
    T = int(next(it))

    robots = []
    for _ in range(N):
        S = int(next(it))              # 첫 제안일
        I = int(next(it))              # 갱신 주기
        M = Decimal(next(it))          # 비율 마진 (예: 0.032 = 3.2%)
        robots.append((S, I, M))

    # 전날 말 기준 게시 가격(센트까지 반올림된 값), None은 아직 미게시
    prices = [None] * N
    prices[0] = P0.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # 로봇 1, day 0 게시

    def average_of_active(state):
        active = [p for p in state if p is not None]
        return (sum(active) / len(active)) if active else Decimal("0")

    # day = 1 .. T-1  (T일의 변경은 고려하지 않음!)
    for day in range(1, T):
        prev = prices[:]                              # 전날 말 스냅샷
        base_avg = average_of_active(prev)            # 전날 말 평균 (한 번만 계산)

        new_prices = prev[:]
        for i, (S, I, M) in enumerate(robots):
            if day < S:
                continue
            # S, S+I, S+2I, ... 아침에 갱신 (전날 말 평균 사용)
            if day == S or (day > S and (day - S) % I == 0):
                # 새 가격 = 평균 * (1 + 마진비율), 센트 반올림(0.5 올림)
                new_price = (base_avg * (Decimal("1") + M)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                new_prices[i] = new_price

        prices = new_prices

    # T일 아침 가격 출력
    for p in prices:
        # 모든 로봇은 T 전에 게시되었을 수도, 아닐 수도 있지만
        # 입력 제약(S1=0, S_i < T)상 T일 아침엔 모두 게시되어 있음
        print(f"{p:.2f}")

if __name__ == "__main__":
    solve()