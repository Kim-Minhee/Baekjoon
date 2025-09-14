# GPT 5
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

# 충분한 정밀도 설정
getcontext().prec = 50

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

it = iter(data)
T = int(next(it))
out_lines = []

for _ in range(T):
    N = int(next(it))
    scores = [int(next(it)) for _ in range(N)]
    total = sum(scores)

    # 평균을 Decimal로 계산한 뒤 소수점 3자리, ROUND_HALF_UP로 반올림
    avg = (Decimal(total) / Decimal(N)).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)

    # 평균보다 큰 사람 수 (정수 비교로 정확히 판단)
    above = sum(1 for x in scores if x * N > total)

    # 백분율 계산 및 반올림
    perc = (Decimal(above) * Decimal(100) / Decimal(N)).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)

    out_lines.append(f"{avg} {perc}%")

sys.stdout.write("\n".join(out_lines))