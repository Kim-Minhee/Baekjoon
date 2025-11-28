# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline
# 출력을 빠르게 처리하기 위해 sys.stdout.write 사용
output = sys.stdout.write

def solve():
    """
    각 소가 착유기에서 보낸 총 시간을 계산합니다.
    - 모든 시간을 '분(minute)' 단위로 변환하여 정수 연산으로 처리합니다.
    - 리스트를 사용하여 O(1) 접근 속도로 각 소의 데이터를 관리합니다.
    - 시간 복잡도: O(Nlines)
    """
    try:
        # 첫 줄 입력: N(소의 수), Nlines(기록 라인 수)
        # map과 split을 사용하여 빠르게 파싱
        header = input().split()
        if not header:
            return
        N, Nlines = map(int, header)
        
        # 1번 소부터 N번 소까지의 데이터를 저장하기 위해 크기를 N+1로 설정
        # total_times[i]: i번 소의 총 착유 시간(분)
        total_times = [0] * (N + 1)
        
        # start_times[i]: i번 소의 현재 세션 시작 시간(분)
        start_times = [0] * (N + 1)
        
        for _ in range(Nlines):
            parts = input().split()
            # 입력 데이터가 부족한 경우 건너뜀 (안전 장치)
            if len(parts) < 4:
                continue

            cow_id = int(parts[0])
            keyword = parts[1]
            hh = int(parts[2])
            mm = int(parts[3])
            
            # 시간을 00:00 기준 '분'으로 변환
            current_minutes = hh * 60 + mm
            
            if keyword == 'START':
                # 시작 시간 기록
                start_times[cow_id] = current_minutes
            else:
                # STOP인 경우: (현재 시간 - 시작 시간)을 총 시간에 누적
                # 문제 조건상 START와 STOP은 항상 짝이 맞으므로 별도 검증 불필요
                total_times[cow_id] += current_minutes - start_times[cow_id]
        
        # 결과 출력 최적화
        # 반복적인 print 호출 대신, 결과 문자열을 리스트에 모아 join 후 한 번에 출력합니다.
        result = []
        for i in range(1, N + 1):
            total_m = total_times[i]
            # 몫(//)은 시간, 나머지(%)는 분
            result.append(f"{total_m // 60} {total_m % 60}")
            
        output('\n'.join(result) + '\n')

    except Exception:
        # 런타임 에러 방지
        pass

if __name__ == "__main__":
    solve()