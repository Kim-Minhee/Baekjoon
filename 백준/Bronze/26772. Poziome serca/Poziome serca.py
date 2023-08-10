n = int(input())
heart = [' @@@   @@@ ', '@   @ @   @', '@    @    @', '@         @', ' @       @ ', '  @     @  ', '   @   @   ', '    @ @    ', '     @     ']
for h in heart:
  print(h + (' ' + h)*(n-1))