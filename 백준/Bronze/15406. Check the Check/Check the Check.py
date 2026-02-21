import sys
input = sys.stdin.readline

total_price = 0
while True:
    D = input().strip()
    if D != 'TOTAL':
        P, C = map(int, input().split())
        total_price += P * C
    else:
        T = int(input().strip())
        if T <= total_price:
            print('PAY')
        else:
            print('PROTEST')
        break