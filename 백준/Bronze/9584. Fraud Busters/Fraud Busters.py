import sys
input = sys.stdin.readline

SC = input().strip()

db_code = []
for _ in range(int(input().strip())):
    DC = input().strip()
    is_possible = True
    for idx, chr in enumerate(SC):
        if chr != '*':
            if chr != DC[idx]:
                is_possible = False
                break
    if is_possible:
        db_code.append(DC)

print(len(db_code))
for code in db_code:
    print(code)