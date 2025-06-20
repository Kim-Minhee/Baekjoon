for _ in range(int(input())):
  W1, W2, W3 = input(), input(), input()
  chk = True
  if W1.startswith(W2) or W1.endswith(W2) or W1.startswith(W3) or W1.endswith(W3):
    chk = False
  elif W2.startswith(W1) or W2.endswith(W1) or W2.startswith(W3) or W2.endswith(W3):
    chk = False
  elif W3.startswith(W1) or W3.endswith(W1) or W3.startswith(W2) or W3.endswith(W2):
    chk = False

  if chk:
    print('Yes')
  else:
    print('No')