N = input()

roman_value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

total = 0
for i in range(0, len(N), 2):
    arabic = int(N[i])
    roman = N[i+1]
    value = arabic * roman_value[roman]
    
    if i + 3 < len(N) and roman_value[roman] < roman_value[N[i+3]]:
        total -= value
    else:
        total += value

print(total)