def diff_time(start_time, finish_time):
    min1 = int(start_time.split(':')[0])*60+int(start_time.split(':')[1])
    min2 = int(finish_time.split(':')[0])*60+int(finish_time.split(':')[1])
    return min2-min1

while True:
    N = int(input())
    if N==0: break
    
    total_time, night_time, over_2h = 0, 0, False
    for _ in range(N):
        SUNRISE_TIME, SUNSET_TIME, START_TIME, FINISH_TIME = input().split()
        
        driving_time = diff_time(START_TIME, FINISH_TIME)
        total_time += driving_time
        
        night_driving_time1 = diff_time(START_TIME, SUNRISE_TIME)
        night_driving_time2 = diff_time(SUNSET_TIME, FINISH_TIME)
        if night_driving_time1>=driving_time//2 or night_driving_time2>=driving_time//2:
            night_time += driving_time
        
        if driving_time>120:
            over_2h = True

    if total_time>=50*60 and night_time>=10*60 and not over_2h:
        print('PASS')
    else:
        print('NON')