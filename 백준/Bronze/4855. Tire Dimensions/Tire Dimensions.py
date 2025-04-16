import math

while True:
  try:
    INFO = input().split()

    section_width = (int(INFO[1])/10) * (int(INFO[3])/100)
    overall_diameter = int(INFO[-1])*2.54 + 2*section_width
    r = math.pi * overall_diameter

    print(*INFO, end='')
    print(':', int(round(r, 0)))
  except:
    break