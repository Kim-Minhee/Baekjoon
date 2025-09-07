# GPT 5
import sys

# 월 이름을 숫자로 매핑
months = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

for line in sys.stdin:
    line = line.strip()
    if line == "0 #":
        break

    day, month = line.split()
    day = int(day)
    month_num = months[month]

    # 특별 조건 먼저 확인
    if day == 4 and month == "August":
        print("Happy birthday")
    elif day == 29 and month == "February":
        print("Unlucky")
    else:
        # 기준 날짜: 2007년 8월 4일
        if (month_num < 8) or (month_num == 8 and day < 4):
            print("Yes")
        else:
            print("No")