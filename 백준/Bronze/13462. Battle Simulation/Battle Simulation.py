# Gemini 3 Pro
import sys
from collections import deque

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    몬스터의 공격 패턴에 맞춰 메카닉의 반격 커맨드를 생성합니다.
    - 기본 반격: R->S, B->K, L->H
    - 콤보 반격: 연속된 3개의 공격이 R, B, L 조합일 경우 -> C
    
    큐(Queue)를 사용하여 3개의 공격을 모으고 콤보 여부를 판단하는 그리디(Greedy) 방식을 사용합니다.
    """
    try:
        # 몬스터 공격 패턴 입력
        attacks = input().strip()
        if not attacks:
            return

        # 반격 매핑 테이블
        counter_map = {'R': 'S', 'B': 'K', 'L': 'H'}
        
        # 콤보 판별을 위한 기준 집합
        combo_target = {'R', 'B', 'L'}
        
        result = []
        # 효율적인 삽입/삭제를 위해 deque 사용
        buffer = deque()
        
        for move in attacks:
            buffer.append(move)
            
            # 버퍼에 3개가 모였을 때 콤보 확인
            if len(buffer) == 3:
                # set으로 변환하여 순서 상관없이 구성 요소가 {R, B, L}인지 확인
                if set(buffer) == combo_target:
                    # 콤보 성립! 'C'를 추가하고 버퍼를 비움 (3개 모두 소모됨)
                    result.append('C')
                    buffer.clear()
                else:
                    # 콤보 실패. 가장 오래된(맨 앞) 공격은 단독 반격 처리
                    oldest_move = buffer.popleft()
                    result.append(counter_map[oldest_move])
        
        # 모든 순회가 끝나고 버퍼에 남은 공격들 처리
        while buffer:
            move = buffer.popleft()
            result.append(counter_map[move])
            
        print("".join(result))

    except Exception:
        pass

if __name__ == "__main__":
    solve()