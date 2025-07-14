# Gemini 2.5 Pro
import sys

def solve_untied_airlines():
    """
    항공편별 승객의 불편 점수를 계산하여 업그레이드 횟수를 결정합니다.
    """
    # 불편 사항 코드와 점수를 딕셔너리로 미리 정의합니다.
    SERVICE_POINTS = {
        'L': 120, 'S': 150, 'B': 150, 'N': 40,
        'C': 160, 'D': 100, 'R': 100, 'O': 100
    }

    # '#'가 입력될 때까지 여러 항공편을 처리합니다.
    while True:
        # 항공편 번호를 읽어옵니다.
        flight_number = sys.stdin.readline().strip()

        # 종료 조건: '#'이 입력되면 루프를 빠져나갑니다.
        if flight_number == '#':
            break

        # 현재 항공편의 승객별 점수를 저장할 딕셔너리를 초기화합니다.
        passenger_scores = {}

        # '00A'가 입력될 때까지 해당 항공편의 불편 사항을 처리합니다.
        while True:
            try:
                line = sys.stdin.readline().split()
                if not line: continue

                seat_number = line[0]
                # 현재 항공편의 입력 종료 조건 확인
                if seat_number == '00A':
                    break
                
                service_code = line[1]
            except (ValueError, IndexError):
                continue

            # 해당 코드의 점수를 가져옵니다. 코드가 없으면 0점 처리.
            points = SERVICE_POINTS.get(service_code, 0)

            # 해당 좌석 승객의 점수를 누적합니다.
            # .get(key, 0)은 키가 없으면 기본값 0을 반환하여 에러를 방지합니다.
            passenger_scores[seat_number] = passenger_scores.get(seat_number, 0) + points
        
        # 업그레이드 대상자 수를 계산합니다.
        upgrade_count = 0
        for score in passenger_scores.values():
            if score >= 200:
                upgrade_count += 1
        
        # 최종 결과를 형식에 맞춰 출력합니다.
        print(f"{flight_number} {upgrade_count}")

# 함수 실행
solve_untied_airlines()