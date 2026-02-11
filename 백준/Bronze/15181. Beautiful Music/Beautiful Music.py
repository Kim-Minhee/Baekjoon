import sys
input = sys.stdin.readline

bits = {'A':'CEG', 'B':'DFA', 'C':'EGB', 'D':'FAC', 'E':'GBD', 'F':'ACE', 'G':'BDF'}

while True:
    B = input().strip()
    if B == '#':
        break
    if len(B) == 1:
        print('That music is beautiful.')
    else:
        is_beautiful = True
        for i in range(len(B) - 1):
            if B[i + 1] not in bits[B[i]]:
                is_beautiful = False
                break
        if is_beautiful:
            print('That music is beautiful.')
        else:
            print('Ouch! That hurts my ears.')