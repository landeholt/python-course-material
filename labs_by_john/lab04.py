# DD1315    John Landeholt
# Lab 4     I-17

def arithmetric(a_1, d):
    sum = 0
    for i,n in enumerate(d,0): sum += a_1 + n * i
    return sum

def geometric(g_1, q):
    sum = 0
    for i,n in enumerate(q,0): sum += g_1 * n ** i
    return sum

if __name__ == "__main__":
    # Låter användaren ansätta variblernas värde
    print("värde för a_1:")
    a_1 = int(input("> "))
    print("värde för g_1:")
    g_1 = int(input("> "))
    print("värde för n:")
    n   = int(input("> "))
    d   = []
    q   = []

    # Ansätter de variationer som d och q har
    print(f"Ange {n}st värden för d och q")
    for _ in range(n):
        value = int(input("> "))
        d.append(value)
        q.append(value)
    print(arithmetric(a_1, d))
    print(geometric(g_1, q))