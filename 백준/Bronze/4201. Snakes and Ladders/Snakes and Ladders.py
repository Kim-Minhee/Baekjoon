# Gemini 2.5 Pro
import sys

def solve_snakes_and_ladders():
    """
    뱀과 사다리 게임의 진행을 시뮬레이션하여 각 플레이어의 최종 위치를 계산합니다.
    """
    try:
        # 첫 줄에서 플레이어 수, 뱀/사다리 수, 주사위 굴림 횟수를 읽어옵니다.
        num_players, num_teleports, num_rolls = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        return

    # 각 플레이어의 위치를 저장하는 리스트, 모두 1에서 시작합니다.
    player_positions = [1] * num_players

    # 뱀과 사다리 정보를 저장하는 딕셔너리 (시작점 -> 도착점)
    teleports = {}
    for _ in range(num_teleports):
        start, end = map(int, sys.stdin.readline().split())
        teleports[start] = end

    # 게임 종료 여부를 추적하는 플래그
    game_over = False
    
    # 주어진 횟수만큼 주사위 굴림을 처리합니다.
    for i in range(num_rolls):
        die_roll = int(sys.stdin.readline())

        # 게임이 이미 끝났다면, 이후의 주사위 굴림은 무시합니다.
        if game_over:
            continue

        # 현재 차례인 플레이어의 인덱스를 계산합니다 (0-기반).
        current_player_index = i % num_players
        
        # 현재 플레이어의 위치를 가져옵니다.
        current_pos = player_positions[current_player_index]
        
        # 주사위 눈금만큼 이동한 새로운 위치를 계산합니다.
        new_pos = current_pos + die_roll

        # 100을 초과하면 100으로 위치를 고정합니다.
        if new_pos >= 100:
            new_pos = 100
        
        # 이동한 위치에 뱀이나 사다리가 있는지 확인하고, 있다면 최종 위치를 업데이트합니다.
        if new_pos in teleports:
            new_pos = teleports[new_pos]

        # 플레이어의 위치를 최종적으로 업데이트합니다.
        player_positions[current_player_index] = new_pos

        # 승리 조건을 확인합니다.
        if new_pos == 100:
            game_over = True

    # 모든 플레이어의 최종 위치를 출력합니다.
    for i in range(num_players):
        player_num = i + 1
        final_pos = player_positions[i]
        print(f"Position of player {player_num} is {final_pos}.")

# 함수 실행
solve_snakes_and_ladders()