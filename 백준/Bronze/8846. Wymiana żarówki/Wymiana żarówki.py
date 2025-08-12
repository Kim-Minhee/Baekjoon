# GPT 4o
MOD = 500000009

def mod_exp(base, exp, mod):
    result = 1
    cur = base % mod
    e = exp
    while e > 0:
        if e & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        e >>= 1
    return result

def mod_inv(a, mod):
    # 페르마의 소정리: mod가 소수일 때, a^(mod-2) mod mod가 역원
    return mod_exp(a, mod-2, mod)

A = int(input())

pow_4_A = mod_exp(4, A, MOD)
inv_3 = mod_inv(3, MOD)

answer = (pow_4_A - 1) * inv_3 % MOD

print(answer)