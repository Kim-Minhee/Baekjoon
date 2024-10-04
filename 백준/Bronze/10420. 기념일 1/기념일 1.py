import datetime

# 입력
N = int(input())

# 풀이
date = datetime.date(2014, 4, 2)
plus_date = date+datetime.timedelta(days=N-1)

# 출력
print(plus_date)