# GPT 5
import sys
input = sys.stdin.readline

problems = {}

while True:
    line = input().strip()
    if line == "-1":
        break
    time_str, problem, result = line.split()
    time = int(time_str)

    if problem not in problems:
        problems[problem] = {"solved": False, "wrong": 0, "time": 0}

    if problems[problem]["solved"]:
        continue  # 이미 해결된 문제는 무시

    if result == "right":
        problems[problem]["solved"] = True
        problems[problem]["time"] = time
    else:
        problems[problem]["wrong"] += 1

# 결과 계산
solved_count = 0
penalty = 0

for info in problems.values():
    if info["solved"]:
        solved_count += 1
        penalty += info["time"] + info["wrong"] * 20

print(solved_count, penalty)