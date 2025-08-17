i = 1
while True:
    S = int(input())
    if S==0:
        break
    
    compressed = S / 2
    uuencoded = round(compressed * 1.5, 0)
    one_floppy = 62 * 30000
    floppies = int(uuencoded // one_floppy)
    if uuencoded % one_floppy != 0:
        floppies += 1

    if i>1:
        print()
    print(f'File #{i}')
    print(f'John needs {floppies} floppies.')

    i += 1 