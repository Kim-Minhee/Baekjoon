# GPT 5
import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    k = int(input().strip())
    name = input().strip()
    
    has_pea = False
    has_pancakes = False
    
    for _ in range(k):
        menu = input().strip()
        if menu == "pea soup":
            has_pea = True
        if menu == "pancakes":
            has_pancakes = True
    
    if has_pea and has_pancakes:
        print(name)
        break
else:
    print("Anywhere is fine I guess")