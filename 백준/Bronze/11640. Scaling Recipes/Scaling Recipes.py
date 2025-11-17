import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    R, P, D = map(int, input().split())
    recipes = []
    main_ing, main_wei = str(), float()
    for _ in range(R):
        ING, WEI, PER = input().split()
        recipes.append((ING, float(PER) * 0.01))
        if float(PER) == 100.0:
            main_ing = ING
            main_wei = D / P * float(WEI)

    print(f'Recipe # {t}')
    for ing, per in recipes:
        wei = main_wei * per
        print(f'{ing} {wei:.1f}')
    print('----------------------------------------')