import sys
input = sys.stdin.readline

N = int(input().strip())
k = N
while k > 1:
    print(f'{k} bottles of beer on the wall, {k} bottles of beer.')
    k -= 1
    if k != 1:
        print(f'Take one down and pass it around, {k} bottles of beer on the wall.')
    else:
        print(f'Take one down and pass it around, 1 bottle of beer on the wall.')
    print()

print('1 bottle of beer on the wall, 1 bottle of beer.')
print('Take one down and pass it around, no more bottles of beer on the wall.')
print()

print('No more bottles of beer on the wall, no more bottles of beer.')
if N > 1:
    print(f'Go to the store and buy some more, {N} bottles of beer on the wall.')
else:
    print(f'Go to the store and buy some more, 1 bottle of beer on the wall.')