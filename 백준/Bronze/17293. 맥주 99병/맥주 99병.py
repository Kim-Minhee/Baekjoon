# Gemini 3.1 Pro
import sys

# 병의 개수에 따른 올바른 문자열을 반환하는 함수
def get_bottle_str(count):
    if count > 1:
        return f"{count} bottles"
    elif count == 1:
        return "1 bottle"
    else:
        return "no more bottles"

def solve():
    # 입력값 N 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # N부터 1까지 역순으로 반복
    for k in range(n, 0, -1):
        curr_str = get_bottle_str(k)
        next_str = get_bottle_str(k - 1)
        
        # 현재 절 출력
        print(f"{curr_str} of beer on the wall, {curr_str} of beer.")
        print(f"Take one down and pass it around, {next_str} of beer on the wall.")
        
        # 각 절 사이에는 빈 줄 출력
        print()
        
    # 반복문이 모두 끝나고 마지막 가사 출력
    # (문장 시작이므로 대문자 'No' 사용)
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, {get_bottle_str(n)} of beer on the wall.")

if __name__ == '__main__':
    solve()