# Gemini 3 Pro
import sys

def solve():
    """
    병행 5도(Parallel Fifths)를 감지하는 프로그램
    조건:
    1. 두 시점 연속으로 음정 차이(%) 12가 7이어야 함.
    2. 두 성부 모두 음의 높이가 변해야 함 (머물러 있으면 안 됨).
    """
    # 모든 입력을 한 번에 읽어서 공백 기준으로 분리합니다. (가장 빠른 입력 방식)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # iterator를 생성하여 순차적으로 데이터를 가져옵니다.
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    # N이 2보다 작으면 연속된 두 쌍을 비교할 수 없으므로 바로 POLE 출력
    if N < 2:
        print("POLE")
        return

    # 병행 5도 발견 여부를 체크하는 플래그
    found_parallel_fifths = False
    
    # 첫 번째 노트 쌍 초기화
    try:
        prev_A = int(next(iterator))
        prev_B = int(next(iterator))
    except StopIteration:
        return
        
    # 첫 번째 쌍의 음정 계산 (A가 항상 B보다 크거나 같으므로 단순 뺄셈)
    prev_diff = (prev_A - prev_B) % 12

    # 1번째 인덱스부터 N-1번째 인덱스까지 반복 (실제로는 2번째 줄부터 읽음)
    # i는 '현재 확인 중인 쌍의 시작 인덱스'를 의미합니다.
    for i in range(1, N):
        try:
            curr_A = int(next(iterator))
            curr_B = int(next(iterator))
        except StopIteration:
            break

        curr_diff = (curr_A - curr_B) % 12

        # 로직 검사:
        # 1. 이전 화음이 5도(나머지 7)이고, 현재 화음도 5도(나머지 7)인가?
        if prev_diff == 7 and curr_diff == 7:
            # 2. 두 성부 모두 음이 움직였는가? (제자리 걸음이 아닌가?)
            if prev_A != curr_A and prev_B != curr_B:
                # 병행 5도 발견! 시작 인덱스 i 출력
                print(i)
                found_parallel_fifths = True

        # 현재 상태를 다음 반복을 위해 '이전 상태'로 업데이트
        prev_A = curr_A
        prev_B = curr_B
        prev_diff = curr_diff

    # 하나도 발견되지 않았다면 POLE 출력
    if not found_parallel_fifths:
        print("POLE")

if __name__ == "__main__":
    solve()