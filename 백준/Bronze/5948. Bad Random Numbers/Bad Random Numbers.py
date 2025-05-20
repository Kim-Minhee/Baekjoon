# Claude
def random_num(num):
    num_str = str(num).zfill(4)

    middle = int(num_str[-3:-1])
    
    return middle * middle

N = int(input())

nums = []
i = 0
while True:
    nums.append(N)
    
    N = random_num(N)
    
    i += 1
    
    if N in nums:
        print(i)
        break