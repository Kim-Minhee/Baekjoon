# GPT
while True:
    S = input()
    if S == 'END':
        break

    letters = [ch for ch in S if ch.isalpha()]
    if len(set(letters))==len(letters):
        print(S)