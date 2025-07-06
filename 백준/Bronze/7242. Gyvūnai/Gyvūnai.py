# GPT 4o
def to_minutes(h, m):
    return h * 60 + m

def to_time(minutes):
    h = minutes // 60
    m = minutes % 60
    return h, m

N = int(input())
start_max = 9 * 60     # 하루 시작 시간: 09:00
end_min = 20 * 60 + 59 # 하루 종료 시간: 20:59

for _ in range(N):
    h1, m1, h2, m2 = map(int, input().split())
    start = to_minutes(h1, m1)
    end = to_minutes(h2, m2)
    start_max = max(start_max, start)
    end_min = min(end_min, end)

if start_max < end_min:
    h1, m1 = to_time(start_max)
    h2, m2 = to_time(end_min)
    print("TAIP")
    print(h1, m1, h2, m2)
else:
    print("NE")