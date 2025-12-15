import sys
input = sys.stdin.readline

trans = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6', 'h':'[-]', 'i':'|',
         'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\\/[]', 'n':'[]\\[]', 'o':'0', 'p':'|D', 'q':'(,)',
         'r':'|Z', 's':'$', 't':"']['", 'u':'|_|', 'v':'\\/', 'w':'\\/\\/', 'x':'}{', 'y':'`/', 'z':'2'}

S = input().lower()
r = []
for s in S:
    if s in trans:
        s = trans[s]
    r.append(s)
print(''.join(r))