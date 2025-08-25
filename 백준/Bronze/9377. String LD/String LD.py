# GPT 5
def main():
    import sys
    input = sys.stdin.readline

    while True:
        n = int(input().strip())
        if n == 0:  # 입력 종료
            break

        words = [input().strip() for _ in range(n)]
        steps = 0

        while True:
            # 다음 단계 단어 생성
            new_words = [w[1:] for w in words]

            # 조건 확인
            if "" in new_words:  # 빈 문자열 생성됨
                break
            if len(set(new_words)) < len(new_words):  # 중복 발생
                break

            # 아직 조건 성립X → 단계 추가
            steps += 1
            words = new_words

        print(steps)


if __name__ == "__main__":
    main()