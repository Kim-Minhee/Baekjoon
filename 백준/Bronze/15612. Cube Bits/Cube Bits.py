# Gemini 3 Pro
import sys

def solve():
    # 모든 입력을 한 번에 읽어서 공백/줄바꿈 기준으로 나눔
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    # 첫 번째 값은 데이터의 개수 n (사용하지 않아도 반복문으로 처리가능)
    # 실제 데이터는 두 번째 값(인덱스 1)부터 시작
    iterator = iter(input_data)
    next(iterator) # n 건너뛰기

    results = []

    for s in iterator:
        val = int(s)

        # 0일 경우 예외 처리
        if val == 0:
            results.append('0')
            continue

        # 3진수 변환
        digits = []
        while val > 0:
            # val % 3 (나머지)을 문자로 바꿔서 저장
            digits.append(str(val % 3))
            val //= 3 # 몫으로 갱신

        # 나머지들을 역순으로 뒤집어서 합침
        results.append("".join(digits[::-1]))

    # 결과를 한 번에 출력 (매번 print하는 것보다 훨씬 빠름)
    print('\n'.join(results))

if __name__ == "__main__":
    solve()