# GPT 4o
def calculate_games(points):
    score_a = 0
    score_b = 0
    games_a = 0
    games_b = 0

    for p in points:
        if p == 'A':
            score_a += 1
        elif p == 'B':
            score_b += 1

        # 게임이 끝나는 조건: 4점 이상 + 상대보다 2점 이상 앞섬
        if score_a >= 4 and score_a - score_b >= 2:
            games_a += 1
            score_a = 0
            score_b = 0
        elif score_b >= 4 and score_b - score_a >= 2:
            games_b += 1
            score_a = 0
            score_b = 0

    return games_a, games_b

while True:
    line = input().strip()
    if line == '#':
        break
    a_games, b_games = calculate_games(line)
    print(f"A {a_games} B {b_games}")