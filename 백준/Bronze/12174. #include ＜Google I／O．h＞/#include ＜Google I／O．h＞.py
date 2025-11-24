# GPT 5
import sys
input = sys.stdin.readline

T = int(input().strip())

for tc in range(1, T + 1):
    B = int(input().strip())
    s = input().strip()

    result = []
    for i in range(B):
        byte = s[8*i:8*i+8]
        # I → 1, O → 0
        bits = byte.replace('I', '1').replace('O', '0')
        # 2진수를 정수로 변환 후 아스키 문자로 변환
        result.append(chr(int(bits, 2)))
    
    print(f"Case #{tc}: {''.join(result)}")