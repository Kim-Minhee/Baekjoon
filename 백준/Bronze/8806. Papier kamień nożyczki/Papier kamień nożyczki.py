# GPT 4o
T = int(input().strip())
for _ in range(T):
    X1, Y1, Z1 = map(float, input().split())  # Adam
    X2, Y2, Z2 = map(float, input().split())  # Gosia

    # Adam 승리 확률
    P_A = X1 * Y2 + Y1 * Z2 + Z1 * X2
    # Gosia 승리 확률
    P_G = X2 * Y1 + Y2 * Z1 + Z2 * X1

    if P_A > P_G:
        print("ADAM")
    elif P_G > P_A:
        print("GOSIA")
    else:
        print("=")