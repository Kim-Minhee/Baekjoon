# Gemini 3 Pro
import sys

def solve():
    # 입력받기: 첫 번째 값은 명령어(E/D), 두 번째 값은 메시지
    input_data = sys.stdin.readline().strip().split()
    if not input_data:
        return
    
    command = input_data[0]
    message = input_data[1]
    
    if command == 'E':  # 인코딩 (압축하기)
        encoded_result = []
        current_char = message[0]
        count = 1
        
        # 두 번째 문자부터 끝까지 확인
        for i in range(1, len(message)):
            if message[i] == current_char:
                count += 1
            else:
                # 문자가 달라지면 지금까지 센 문자와 개수를 저장
                encoded_result.append(current_char + str(count))
                current_char = message[i]
                count = 1
        
        # 마지막으로 세고 있던 문자와 개수 저장
        encoded_result.append(current_char + str(count))
        print("".join(encoded_result))
        
    elif command == 'D':  # 디코딩 (압축 풀기)
        decoded_result = []
        
        # 압축된 문자열은 항상 '문자+숫자' 쌍으로 이루어져 있으므로 2칸씩 건너뛰며 반복
        for i in range(0, len(message), 2):
            char = message[i]
            count = int(message[i+1])
            # 해당 문자를 숫자만큼 반복해서 리스트에 추가
            decoded_result.append(char * count)
            
        print("".join(decoded_result))

if __name__ == '__main__':
    solve()