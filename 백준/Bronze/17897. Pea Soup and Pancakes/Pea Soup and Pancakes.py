# Gemini 3.1 Pro
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline
    
    # 첫 줄: 식당의 수 n
    first_line = input()
    if not first_line:
        return
    n = int(first_line.strip())
    
    # n개의 식당 정보를 순서대로 확인
    for _ in range(n):
        # 해당 식당의 메뉴 개수 k
        k = int(input().strip())
        # 식당 이름
        restaurant_name = input().strip()
        
        # k개의 메뉴를 set에 저장
        menu = set()
        for _ in range(k):
            menu.add(input().strip())
            
        # 완두콩 수프와 팬케이크가 모두 메뉴에 있는지 확인
        if 'pea soup' in menu and 'pancakes' in menu:
            print(restaurant_name)
            return  # 찾았다면 함수를 즉시 종료하여 이후 식당은 탐색하지 않음
            
    # 모든 식당을 다 확인했는데도 조건을 만족하는 곳이 없다면
    print("Anywhere is fine I guess")

if __name__ == '__main__':
    solve()