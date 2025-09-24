import sys
input = sys.stdin.readline

def find1(num):
    a = int(num ** (1 / 3))
    n = a ** 3
    if n < num:
        while n <= num:
            a += 1
            n = a ** 3
        return a - 1
    if n >= num:
        while n > num:
            a -= 1
            n = a ** 3
        return a

def find2(num):
    a = int((6 * N) ** (1 / 3)) - 1
    n = (a * (a + 1) * (a + 2)) // 6
    if n < num:
        while n <= num:
            a += 1
            n = (a * (a + 1) * (a + 2)) // 6
        return a - 1
    if n >= num:
        while n > num:
            a -= 1
            n = (a * (a + 1) * (a + 2)) // 6
        return a

while True:
    N = int(input())
    if N == 0:
        break
    
    a, b = find1(N), find2(N)
    container1 = [i ** 3 for i in range(a + 1)]
    container2 = [(i * (i + 1) * (i + 2)) // 6 for i in range(b + 1)]

    c = 0
    for i in container1:
        for j in container2:
            k =  i + j
            if k <= N and k > c:
                c = k

    print(max(container1[-1], container2[-1], c))                