# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 받습니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # 1자리 숫자는 이미 유효숫자가 1개이므로 그대로 출력합니다.
    if n <= 9:
        print(n)
        return
        
    # 숫자의 자릿수를 구하고, 기준이 될 단위(place)를 계산합니다.
    # 예: n이 149라면 L=3, place=100이 됩니다.
    L = len(str(n))
    place = 10 ** (L - 1)
    
    # 나머지를 구합니다. (예: 149 % 100 = 49)
    remainder = n % place
    
    # 나머지가 기준 단위의 절반(예: 50) 이상인지 확인합니다.
    if remainder >= place // 2:
        # 올림 (예: 149 -> 100의 자리에서 1을 더해 200)
        print((n // place + 1) * place)
    else:
        # 버림 (예: 149 -> 100)
        print((n // place) * place)

if __name__ == '__main__':
    solve()