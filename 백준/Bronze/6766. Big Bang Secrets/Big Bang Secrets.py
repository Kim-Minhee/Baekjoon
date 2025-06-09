# Gemini 2.5 Pro
UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 상수로 외부에 선언

def decoding(alphabet, s):
    i = (UPPERS.index(alphabet) - s) % 26
    return UPPERS[i]

K, W = int(input()), input()

r = ''.join(decoding(w, 3*(i+1)+K) for i, w in enumerate(W))
print(r)