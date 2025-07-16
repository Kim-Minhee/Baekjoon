# Gemini 2.5 Pro
import sys

def solve_air_nz_booking():
    """
    Air NZ 항공편의 예약 및 취소 거래를 시뮬레이션합니다.
    """
    MAX_SEATS = 68

    # '#'가 입력될 때까지 여러 항공편 시나리오를 처리합니다.
    while True:
        try:
            # 첫 줄에서 항공편 번호와 초기 예약 좌석 수를 읽어옵니다.
            line = sys.stdin.readline().split()
            if not line: break # 입력이 끝나면 종료

            flight_number = line[0]
            # 두 번째 요소가 없을 경우를 대비하여 예외 처리
            if len(line) < 2: continue
            
            initial_seats_str = line[1]
        except IndexError:
            break

        # 전체 입력 종료 조건 확인
        if flight_number == '#' and initial_seats_str == '0':
            break
        
        current_booked_seats = int(initial_seats_str)

        # 'X 0'이 입력될 때까지 해당 항공편의 거래를 처리합니다.
        while True:
            try:
                trans_line = sys.stdin.readline().split()
                if not trans_line: continue

                trans_type = trans_line[0]
                # 두 번째 요소가 없을 경우를 대비하여 예외 처리
                if len(trans_line) < 2: continue
                
                num_seats_str = trans_line[1]
            except IndexError:
                continue
            
            # 현재 시나리오의 거래 종료 조건 확인
            if trans_type == 'X' and num_seats_str == '0':
                break
            
            num_seats = int(num_seats_str)

            # 예약('B') 거래 처리
            if trans_type == 'B':
                # 유효성 검사: 예약 후 총 좌석이 68석을 넘지 않는지 확인
                if current_booked_seats + num_seats <= MAX_SEATS:
                    current_booked_seats += num_seats
            
            # 취소('C') 거래 처리
            elif trans_type == 'C':
                # 유효성 검사: 취소할 좌석 수가 현재 예약된 좌석 수보다 많지 않은지 확인
                if num_seats <= current_booked_seats:
                    current_booked_seats -= num_seats
        
        # 최종 결과를 형식에 맞춰 출력합니다.
        print(f"{flight_number} {current_booked_seats}")

# 함수 실행
solve_air_nz_booking()