# GPT 5.1
import sys
input = sys.stdin.readline

# 음을 숫자로 매핑
note_map = {
    'A': 0, 'B': 1, 'C': 2,
    'D': 3, 'E': 4, 'F': 5, 'G': 6
}

while True:
    line = input().strip()
    
    if line == '#':
        break
    
    beautiful = True
    
    for i in range(len(line) - 1):
        cur = note_map[line[i]]
        nxt = note_map[line[i + 1]]
        
        diff = (nxt - cur) % 7
        
        if diff not in (2, 4, 6):
            beautiful = False
            break
    
    if beautiful:
        print("That music is beautiful.")
    else:
        print("Ouch! That hurts my ears.")