# GPT
def time_to_min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

while True:
    N = int(input())
    if N == 0:
        break

    total_time = 0
    night_time = 0
    over_2h = False

    for _ in range(N):
        sr, ss, st, et = input().split()
        sunrise = time_to_min(sr)
        sunset = time_to_min(ss)
        start = time_to_min(st)
        end = time_to_min(et)

        driving_time = end - start
        total_time += driving_time

        if driving_time > 120:
            over_2h = True

        # 야간 시간 계산
        night1 = max(0, min(sunrise, end) - max(0, start))  # 자정~일출 전
        night2 = max(0, min(end, 1440) - max(sunset, start))  # 일몰 후~자정
        night_duration = night1 + night2

        if night_duration * 2 >= driving_time:
            night_time += driving_time

    if total_time >= 50 * 60 and night_time >= 10 * 60 and not over_2h:
        print('PASS')
    else:
        print('NON')