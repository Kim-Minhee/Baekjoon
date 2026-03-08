# Gemini 3 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    # a: 양 1마리 사료, b: 염소 1마리 사료, n: 전체 마릿수, w: 전체 사료 양
    try:
        line = input().split()
        if not line: return
        a, b, n, w = map(int, line)
    except ValueError:
        return

    answers = []
    
    # 양(sheep)은 최소 1마리, 최대 n-1마리 가능
    for sheep in range(1, n):
        goats = n - sheep # 염소의 수는 전체 - 양의 수
        
        # 사료의 총합이 w와 일치하는지 확인
        if a * sheep + b * goats == w:
            answers.append((sheep, goats))
            
            # 해가 2개 이상이 되는 순간 더 탐색할 필요 없이 중단하여 효율성 극대화
            if len(answers) > 1:
                break
                
    # 해가 정확히 1개일 때만 결과 출력
    if len(answers) == 1:
        print(f"{answers[0][0]} {answers[0][1]}")
    else:
        # 해가 없거나(0개) 2개 이상인 경우
        print("-1")

if __name__ == '__main__':
    solve()