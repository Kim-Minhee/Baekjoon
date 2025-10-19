while True:
    try:
        S = input().strip().lower()
        print('yes' if 'problem' in S else 'no')
    except:
        break