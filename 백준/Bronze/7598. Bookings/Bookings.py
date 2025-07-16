# GPT 4o
while True:
    line = input()
    if line == "# 0":
        break

    flight, booked = line.split()
    booked = int(booked)

    while True:
        tx = input()
        if tx == "X 0":
            break

        action, number = tx.split()
        number = int(number)

        if action == "B":
            if booked + number <= 68:
                booked += number
        elif action == "C":
            if number <= booked:
                booked -= number

    print(f"{flight} {booked}")