# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터 전체를 한 번에 읽고 공백/줄바꿈 기준으로 분리합니다.
    # 문제에서 문자열 내에 공백이 없다고 보장했으므로 아주 안전하고 빠른 방식입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    lines = input_data[1:]
    
    for line in lines:
        result = []
        current_char = line[0]
        count = 1
        
        # 두 번째 글자부터 끝까지 순회합니다.
        for i in range(1, len(line)):
            if line[i] == current_char:
                count += 1
            else:
                # 글자가 달라지는 순간, 지금까지의 카운트와 글자를 리스트에 저장합니다.
                result.append(f"{count} {current_char}")
                current_char = line[i]
                count = 1
                
        # 반복문이 끝난 후, 마지막으로 세고 있던 문자 그룹을 결과에 넣어줍니다.
        result.append(f"{count} {current_char}")
        
        # 리스트에 모인 문자열 조각들을 공백 한 칸을 두고 합쳐서 출력합니다.
        print(" ".join(result))

if __name__ == '__main__':
    solve()