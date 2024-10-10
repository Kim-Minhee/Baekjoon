# 입력
K = int(input())

# 풀이
k = int('0b'+'1'*K, 2)
s = k*(k+1)//2

# 출력
print(bin(s)[2:])