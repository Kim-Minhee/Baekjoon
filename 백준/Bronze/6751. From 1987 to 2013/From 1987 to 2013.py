# Gemini 2.5 Pro
Y = int(input())

while True:
    Y += 1
    # 연도를 문자열로 변환한 것의 길이와,
    # 그것을 set으로 변환한 것의 길이가 같으면 모든 숫자가 고유하다.
    if len(set(str(Y))) == len(str(Y)):
        print(Y)
        break