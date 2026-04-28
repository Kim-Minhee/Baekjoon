# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 한 번에 모두 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    words = input_data[2:]
    
    # 출제된 문제 중 가장 마지막(가장 큰) 알파벳을 구합니다.
    # 예: m이 3이면 'C', m이 15면 'O'가 됩니다.
    max_char = chr(ord('A') + m - 1)
    
    valid_count = 0
    
    for word in words:
        # 조건 1: 중복된 알파벳이 없는지 확인
        # (set으로 만들었을 때의 길이와 원래 문자열의 길이가 같으면 중복이 없는 것입니다.)
        if len(set(word)) != len(word):
            continue
            
        # 조건 2: 단어에 포함된 모든 알파벳이 사용 가능한 범위 내에 있는지 확인
        # 입력되는 단어가 모두 대문자임이 보장되므로, 
        # 단어에서 가장 큰(알파벳 순서가 늦은) 글자만 max_char와 비교하면 끝납니다!
        if max(word) <= max_char:
            valid_count += 1
            
    print(valid_count)

if __name__ == "__main__":
    solve()