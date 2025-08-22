P, G, R, O = int(input()), int(input()), int(input()), int(input())
TARGET = int(input())

cases = []
min_tickets = TARGET // P
for p in range(TARGET // P + 1):
    pink = p * P
    money_left_after_pink = TARGET - pink
    for g in range(money_left_after_pink // G + 1):
        green = g * G
        money_left_after_green = money_left_after_pink - green
        for r in range(money_left_after_green // R + 1):
            red = r * R
            money_left_after_red = money_left_after_green - red
            for o in range(money_left_after_red // O + 1):
                orange = o * O
                money = pink + green + red + orange
                if TARGET == money:
                    cases.append((p, g, r, o))
                    min_tickets = min(min_tickets, p + g + r + o)

num_cases = len(cases)
for i in range(num_cases):
    print(f'# of PINK is {cases[i][0]} # of GREEN is {cases[i][1]} # of RED is {cases[i][2]} # of ORANGE is {cases[i][3]}')
print(f'Total combinations is {num_cases}.')
print(f'Minimum number of tickets to print is {min_tickets}.')