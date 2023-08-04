n = int(input())
letter = ['h', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
num = int()
if n%8!=0:
  num = n//8+1
else:
  num = n//8
let = letter[n%8]
print(let+str(num))