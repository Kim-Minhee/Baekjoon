# GPT 4o
n = input().lstrip('0')  # 0으로 시작하는 경우 제거

# n이 0이면 2⁰ = 1
if n == '':
    print(1)
else:
    last_digit_cycle = [6, 2, 4, 8]  # index: n % 4
    n_mod_4 = int(n[-2:]) % 4  # n의 마지막 두 자리만 보고 % 4 계산
    print(last_digit_cycle[n_mod_4])