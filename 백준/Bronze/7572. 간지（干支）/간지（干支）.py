# 입력
N = int(input())-4

# 풀이
gan = '0123456789'
ji = 'ABCDEFGHIJKL'
r = ji[N%12]+gan[N%10]

# 출력
print(r)