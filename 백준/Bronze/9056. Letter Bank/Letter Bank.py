# GPT 5
T = int(input().strip())
for _ in range(T):
    alpha, beta = input().strip().split()
    
    set_alpha = set(alpha)
    set_beta = set(beta)
    
    if set_beta.issubset(set_alpha) and set_alpha.issubset(set_beta):
        print("YES")
    else:
        print("NO")