# GPT 5
import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    d, m, y = map(int, line.split())
    if d == 0 and m == 0 and y == 0:
        break

    S = (d + m + y) % 25 + 1
    message = sys.stdin.readline().rstrip("\n")

    decrypted = []
    for c in message:
        if 'a' <= c <= 'z':
            shifted = (ord(c) - ord('a') - S) % 26 + ord('a')
            decrypted.append(chr(shifted))
        else:
            decrypted.append(c)

    print("".join(decrypted))