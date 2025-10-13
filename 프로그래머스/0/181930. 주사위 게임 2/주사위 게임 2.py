def solution(a, b, c):
    if len(set([a, b, c])) == 3:
        return a + b + c
    elif len(set([a, b, c])) == 1:
        return 27 * a ** 6
    else:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)