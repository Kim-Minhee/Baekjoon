import sys
input = sys.stdin.readline

black = ['A1', 'A3', 'A5', 'A7', 'B2', 'B4', 'B6', 'B8',
         'C1', 'C3', 'C5', 'C7', 'D2', 'D4', 'D6', 'D8',
         'E1', 'E3', 'E5', 'E7', 'F2', 'F4', 'F6', 'F8',
         'G1', 'G3', 'G5', 'G7', 'H2', 'H4', 'H6', 'H8',
         '1', '3', '5', '7', '10', '12', '14', '16',
         '17', '19', '21', '23', '26', '28', '30', '32',
         '33', '35', '37', '39', '42', '44', '46', '48',
         '49', '51', '53', '55', '58', '60', '62', '64']

for _ in range(int(input().strip())):
    M1, M2 = input().split()
    if (M1 in black and M2 in black) or (M1 not in black and M2 not in black):
        print('YES')
    else:
        print('NO')