# Gemini 3 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # N: 교실의 개수
    n = int(input_data[0])
    
    # A: 각 교실에 있는 학생 수 리스트
    a = [int(x) for x in input_data[1:n+1]]
    
    # Ayu의 출발 위치와 방향
    x1 = int(input_data[n+1])
    d1 = input_data[n+2]
    
    # Budi의 출발 위치와 방향
    x2 = int(input_data[n+3])
    d2 = input_data[n+4]
    
    # 1. Ayu가 지나간 교실들 구하기
    if d1 == "left":
        # 왼쪽으로 가면 1번 교실부터 출발한 교실(x1)까지
        ayu_rooms = a[0:x1]
    else: # "right"
        # 오른쪽으로 가면 출발한 교실(x1)부터 마지막 교실(N)까지
        ayu_rooms = a[x1-1:n]
        
    # Ayu가 본 전체 학생 수 (리스트의 합)
    ayu_total_students = sum(ayu_rooms)
    
    # 2. Budi가 지나간 교실들 구하기
    if d2 == "left":
        budi_rooms = a[0:x2]
    else: # "right"
        budi_rooms = a[x2-1:n]
        
    # Budi가 본 빈 교실(학생 수가 0인 교실)의 수
    budi_empty_rooms = budi_rooms.count(0)
    
    # 결과 출력 (공백으로 구분)
    print(f"{ayu_total_students} {budi_empty_rooms}")

if __name__ == '__main__':
    solve()