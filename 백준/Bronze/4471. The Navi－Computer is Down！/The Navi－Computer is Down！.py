for _ in range(int(input())):
  current = input()
  c_x, c_y, c_z = map(float, input().split())
  destination = input()
  d_x, d_y, d_z = map(float, input().split())

  r = ((d_x-c_x)**2 + (d_y-c_y)**2 + (d_z-c_z)**2)**(1/2)
  print(f'{current} to {destination}: {r:.2f}')