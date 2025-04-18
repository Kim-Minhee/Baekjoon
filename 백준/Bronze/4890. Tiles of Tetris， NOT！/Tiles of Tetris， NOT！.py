def gcd(a, b): # 최대공약수
  while b!=0:
    a, b = b, a%b
  return a

def lcm(a, b): # 최소공배수
  return a*b//gcd(a, b)

while True:
  W, H = map(int, input().split())
  if W==H==0: break

  wh_lcm = lcm(W, H)
  print((wh_lcm//W) * (wh_lcm//H))