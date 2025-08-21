def rounding(is_clockwise, depart, arrive):
    if is_clockwise:
        return (depart - arrive + 40) % 40
    else:
        return (arrive - depart + 40) % 40

one_tick = 360//40

while True:
    S0, S1, S2, S3 = map(int, input().split())
    if S0 + S1 + S2 + S3 == 0:
        break

    r = 3 * 40 * one_tick
    r += rounding(True, S0, S1) * one_tick
    r += rounding(False, S1, S2) * one_tick
    r += rounding(True, S2, S3) * one_tick

    print(r)