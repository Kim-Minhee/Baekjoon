# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어와 공백을 기준으로 분리합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    M = int(input_data[1])
    
    cards = []
    idx = 2
    
    # N개의 카드 상태를 [보이는 면, 숨겨진 면] 형태로 배열에 저장합니다.
    for _ in range(N):
        cards.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2
        
    # M번의 명령(K)을 순서대로 처리합니다.
    for _ in range(M):
        K = int(input_data[idx])
        idx += 1
        
        # 모든 카드를 확인하며 조건에 맞으면 뒤집습니다.
        for card in cards:
            if card[0] <= K:
                card[0], card[1] = card[1], card[0]
                
    # 모든 명령이 종료된 후, 현재 보이고 있는 면(card[0])들의 합을 계산합니다.
    total_sum = sum(card[0] for card in cards)
    print(total_sum)

if __name__ == '__main__':
    solve()