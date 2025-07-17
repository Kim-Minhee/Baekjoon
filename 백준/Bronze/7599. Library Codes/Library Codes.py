while True:
    LIBRARY, F = input().split()
    if LIBRARY=='#' and F=='0': break
    f = int(F)

    books = []
    for i in range(int(input())):
        W, TEXT = input().split()
        text_width = len(TEXT)*f + 2
        if text_width<=int(W):
            books.append(('Book '+str(i+1), 'horizontal'))
        else:
            books.append(('Book '+str(i+1), 'vertical'))

    print(f'{LIBRARY} Library')
    for (book_num, displayed) in books:
        print(f'{book_num} {displayed}')