A, B, C = input().split()
X = int(input())

x_list = [int(A+B+C), int(A+C+B), int(B+A+C), int(B+C+A), int(C+A+B), int(C+B+A)]
x_list.sort()

print(x_list.index(X)+1)