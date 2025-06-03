clock = {'A':12, '2':11, '3':10, '4':9, '5':8, '6':7, '7':6, '8':5, '9':4, 'T':3, 'J':2, 'Q':1, 'K':0}

cards = [[] for _ in range(13)]
while True:
  I = input()
  if I=='#':
    break

  card = list(I.split())
  for i in range(13):
    cards[i].append(card[i])
    
  if len(cards[0])==4:
    current_index = 0
    current_card = cards[current_index][0]
    visited = [current_card]
    while True:
      try:
        cards[current_index].remove(current_card)
        current_index = clock[current_card[0]]
        current_card = cards[current_index][0]
        visited.append(current_card)
      except:
        break
      
    print(f'{len(visited):02},{current_card}')
    cards = [[] for _ in range(13)]