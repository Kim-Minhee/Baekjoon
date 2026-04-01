# GPT 5
import sys
input = sys.stdin.readline

T = input().rstrip()
known = "CHICKENS"

# key는 첫 글자만으로도 충분
key = ord(T[0]) ^ ord(known[0])

# 복호화
print(''.join(chr(ord(c) ^ key) for c in T))