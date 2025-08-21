# GPT 5
import sys

for line in sys.stdin:
    p, a, b, c = map(int, line.split())
    if p == a == b == c == 0:
        break

    total = 0

    # Step 1: 두 바퀴(720도)
    total += 720
    # + p → a (cw)
    total += ((p - a) % 40) * 9

    # Step 2: 한 바퀴(360도)
    total += 360
    # + a → b (ccw)
    total += ((b - a) % 40) * 9

    # Step 3: b → c (cw)
    total += ((b - c) % 40) * 9

    print(total)