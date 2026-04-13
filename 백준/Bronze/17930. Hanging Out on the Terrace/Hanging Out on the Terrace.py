# Gemini 3.1 Pro
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline
    
    first_line = input().split()
    if not first_line:
        return
        
    L = int(first_line[0]) # 테라스 최대 수용 인원
    x = int(first_line[1]) # 이벤트의 수
    
    current_people = 0
    denied_count = 0
    
    for _ in range(x):
        action, p_str = input().split()
        p = int(p_str)
        
        if action == "leave":
            # 사람들이 떠나면 현재 인원에서 빼줍니다.
            current_people -= p
            
        elif action == "enter":
            # 들어오려는 그룹을 합쳤을 때 제한 인원을 초과하는지 확인합니다.
            if current_people + p > L:
                denied_count += 1  # 초과하면 탁구장으로 보내고 거부 횟수 +1
            else:
                current_people += p  # 초과하지 않으면 테라스에 입장!
                
    # 최종적으로 입장이 거부된 그룹의 수를 출력합니다.
    print(denied_count)

if __name__ == '__main__':
    solve()