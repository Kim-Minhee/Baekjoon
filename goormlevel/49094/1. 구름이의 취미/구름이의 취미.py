# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N = int(input())

# 시간초과
# s = 0
# for i in range(1, N+1):
# 	s += i**3
# print(s%(10**9+7))

# 수학공식 이용
# https://mathbang.net/628#gsc.tab=0
r = (N*(N+1)//2)**2
r %= 1000000007
print(r)