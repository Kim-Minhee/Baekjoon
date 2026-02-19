# Gemini 3 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    try:
        # 데이터 셋의 개수 P
        P_str = input().strip()
        if not P_str: return
        P = int(P_str)
        
        for _ in range(P):
            # K: 데이터 셋 번호, b: 진법, n: 변환할 숫자
            K, b, n = map(int, input().split())
            
            ssd_sum = 0
            
            # 진법 변환 및 자리수 제곱합 계산
            while n > 0:
                digit = n % b        # b진법에서의 한 자리 숫자 (나머지)
                ssd_sum += digit ** 2 # 그 숫자의 제곱을 누적
                n //= b              # 다음 자리를 구하기 위해 몫으로 갱신
                
            # 결과 출력
            print(f"{K} {ssd_sum}")
            
    except ValueError:
        pass

if __name__ == "__main__":
    solve()