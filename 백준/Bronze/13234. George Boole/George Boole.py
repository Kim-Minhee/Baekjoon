import sys
input = sys.stdin.readline

V1, OP, V2 = input().split()
if V1 == V2 == 'true':
    r = 'true'
elif V1 != V2 and OP == 'OR':
    r = 'true'
else:
    r = 'false'
print(r)