# GPT 4o
T = int(input())  # 테스트 케이스 수

for t in range(T):
    num = input().strip()
    original = num

    while len(num) > 2:
        print(num)
        shortened = num[:-1]
        last_digit = int(num[-1])
        new_num = int(shortened) - last_digit
        num = str(new_num)

    print(num)
    if int(num) % 11 == 0:
        print(f'The number {original} is divisible by 11.')
    else:
        print(f'The number {original} is not divisible by 11.')

    if t != T - 1:
        print()  # 테스트 케이스 사이 빈 줄