def solution(arr):
    x = 0
    while True:
        new_arr = []
        for a in arr:
            if a >= 50 and a % 2 == 0:
                a //= 2
            elif a < 50 and a % 2 != 0:
                a *= 2
                a += 1
            new_arr.append(a)
        if new_arr == arr:
            return x
        x += 1
        arr = new_arr