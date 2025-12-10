# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    Reverse Words 문제 해결 함수
    문장의 단어 순서를 뒤집습니다. (예: "this is test" -> "test is this")
    파이썬의 강력한 문자열 처리 기능을 활용하여 간결하게 해결합니다.
    """
    try:
        # 첫 줄: 테스트 케이스의 개수 N
        line = input().strip()
        if not line:
            return
        N = int(line)

        for i in range(1, N + 1):
            # 문장 입력 (양쪽 공백 제거)
            line = input().strip()

            # 1. split(): 공백을 기준으로 문자열을 잘라 리스트로 만듭니다.
            #    예: "this is a test" -> ['this', 'is', 'a', 'test']
            words = line.split()

            # 2. [::-1]: 리스트 슬라이싱을 사용하여 순서를 뒤집습니다.
            #    예: ['test', 'a', 'is', 'this']
            reversed_words = words[::-1]

            # 3. " ".join(): 리스트의 단어들을 공백으로 연결하여 하나의 문자열로 만듭니다.
            result = " ".join(reversed_words)

            # 결과 출력
            print(f"Case #{i}: {result}")

    except ValueError:
        pass

if __name__ == "__main__":
    solve()