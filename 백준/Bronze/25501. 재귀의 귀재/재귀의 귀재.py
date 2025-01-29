def recursion(string, left, right, i):
    if left>=right: return 1, i
    elif string[left]!=string[right]: return 0, i
    else: return recursion(string, left+1, right-1, i+1)

def isPalindrome(string, i):
    return recursion(string, 0, len(string)-1, i)

for _ in range(int(input())):
  S = input()
  r1, r2 = isPalindrome(S, 1)
  print(r1, r2)