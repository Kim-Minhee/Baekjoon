# Gemini
N, P = map(int, input().split())

result_str = str(N**P)

for i in range(0, len(result_str), 70):
    print(result_str[i:i+70])