# Gemini 2.5 Pro
import sys

def solve_ranking_manipulation():
    """
    문제의 가중치를 조작하여 Dymówka의 최고 등수와
    그때의 최소 동점자 수를 계산합니다.
    """
    try:
        # 첫 줄에서 참가자 수(n)와 문제 수(m)를 읽어옵니다.
        n, m = map(int, sys.stdin.readline().split())
        
        # 모든 참가자의 점수를 2차원 리스트로 읽어옵니다.
        scores = []
        for _ in range(n):
            scores.append(list(map(int, sys.stdin.readline().split())))
            
    except (ValueError, IndexError):
        # 입력이 비었거나 형식이 잘못된 경우 종료합니다.
        return

    # Dymówka는 항상 첫 번째 참가자입니다.
    dymowka_scores = scores[0]

    # Dymówka와 동점(1등)이 될 참가자의 수를 셉니다.
    tied_at_first_place = 0
    
    # 모든 참가자를 순회합니다.
    for participant_scores in scores:
        is_tied = True
        
        # Dymówka가 푼 모든 문제를 현재 참가자도 풀었는지 확인합니다.
        for i in range(m):
            # 만약 Dymówka는 풀었는데(100), 현재 참가자는 풀지 못했다면(0),
            # 이 참가자는 동점이 될 수 없습니다.
            if dymowka_scores[i] == 100 and participant_scores[i] == 0:
                is_tied = False
                break
        
        # 모든 검사를 통과했다면, 이 참가자는 Dymówka와 동점입니다.
        if is_tied:
            tied_at_first_place += 1
            
    # 최고 등수는 항상 1등이며, 계산된 동점자 수를 함께 출력합니다.
    best_rank = 1
    print(best_rank, tied_at_first_place)

# 함수 실행
solve_ranking_manipulation()