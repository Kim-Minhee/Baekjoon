# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    백준 14614번 Calculate! 문제 해결 함수
    A에 B를 C번 XOR한 결과를 계산합니다.
    XOR 연산은 두 번 수행하면 원래 값으로 돌아오는 성질이 있습니다.
    따라서 C가 짝수면 A, 홀수면 A ^ B 가 정답입니다.
    """
    try:
        # A, B, C 입력 (공백 구분)
        # C는 매우 큰 수일 수 있지만 Python은 큰 정수를 기본 지원하므로 int()로 변환 가능
        line = input().strip()
        if not line:
            return
            
        A, B, C = map(int, line.split())
        
        # C가 짝수인지 홀수인지 판단
        if C % 2 == 0:
            # 짝수 번 XOR하면 원래대로 돌아옴
            print(A)
        else:
            # 홀수 번 XOR하면 한 번 XOR한 것과 같음
            print(A ^ B)

    except ValueError:
        pass

if __name__ == "__main__":
    solve()