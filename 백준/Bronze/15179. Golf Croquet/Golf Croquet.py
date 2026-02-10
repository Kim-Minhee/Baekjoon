# GPT 5.1
import sys
input = sys.stdin.readline

# 팀 이름 입력
team1 = input().rstrip()
team2 = input().rstrip()

# 스트로크 수
S = int(input().strip())

# 스트로크 기록
shots = input().strip()

# 점수
score1 = 0
score2 = 0

# 플레이어 순서: 0=blue, 1=red, 2=black, 3=yellow
# team1: blue(0), black(2)
# team2: red(1), yellow(3)

for i in range(S):
    shot = shots[i]
    player = i % 4

    # 현재 플레이어 팀
    if player in (0, 2):
        my_score, opp_score = score1, score2
        my_team = 1
    else:
        my_score, opp_score = score2, score1
        my_team = 2

    if shot == 'H':
        my_score += 1
    elif shot == 'D':
        my_score += 2
    elif shot == 'O':
        opp_score += 1

    # 점수 상한 7
    my_score = min(my_score, 7)
    opp_score = min(opp_score, 7)

    # 점수 반영
    if my_team == 1:
        score1, score2 = my_score, opp_score
    else:
        score2, score1 = my_score, opp_score

    # 누군가 이기면 즉시 종료
    if score1 == 7 or score2 == 7:
        break

# 결과 출력
print(f"{team1} {score1} {team2} {score2}.", end=" ")

if score1 == 7:
    print(f"{team1} has won.")
elif score2 == 7:
    print(f"{team2} has won.")
elif score1 > score2:
    print(f"{team1} is winning.")
elif score2 > score1:
    print(f"{team2} is winning.")
else:
    print("All square.")