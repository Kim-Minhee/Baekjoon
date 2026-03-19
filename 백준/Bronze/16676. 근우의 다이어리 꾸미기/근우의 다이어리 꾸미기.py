# Gemini 3 Pro
import sys

def solve():
    # 입력받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # 0 ~ 9까지는 무조건 1팩이 필요함
    if n < 10:
        print(1)
        return
        
    # N의 자릿수 구하기
    n_str = str(n)
    length = len(n_str)
    
    # 길이가 같은 111...1 형태의 수 만들기
    compare_num = int('1' * length)
    
    # N이 111...1 보다 크거나 같으면 자릿수만큼 팩이 필요
    if n >= compare_num:
        print(length)
    # N이 111...1 보다 작으면 (자릿수 - 1)만큼 팩이 필요
    else:
        print(length - 1)

if __name__ == '__main__':
    solve()