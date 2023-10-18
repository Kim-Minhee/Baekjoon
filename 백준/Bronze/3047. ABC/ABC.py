num = list(map(int, input().split()))
num.sort()
num_d = {'A':num[0], 'B':num[1], 'C':num[2]}
alp = input()
print(num_d[alp[0]], num_d[alp[1]], num_d[alp[2]])