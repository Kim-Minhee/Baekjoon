# GPT 5
import sys
input = sys.stdin.readline

line = input().rstrip()
mode, s = line[0], line[2:]

# Encode
if mode == 'E':
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    
    print(''.join(result))

# Decode
else:
    result = []
    
    for i in range(0, len(s), 2):
        char = s[i]
        count = int(s[i+1])
        result.append(char * count)
    
    print(''.join(result))