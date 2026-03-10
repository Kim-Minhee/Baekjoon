# Gemini 3 Pro
import sys

def solve():
    # 5장의 카드를 입력받음
    cards = sys.stdin.readline().split()
    
    # 각 카드의 첫 번째 글자(숫자/알파벳)만 추출
    ranks = [card[0] for card in cards]
    
    # 각 글자가 리스트에 몇 개씩 있는지 세고, 그중 최댓값을 출력
    max_strength = max(ranks.count(r) for r in ranks)
    
    print(max_strength)

if __name__ == '__main__':
    solve()