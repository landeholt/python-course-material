# DD1315    John Landeholt
# Lab 3     I-17

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

# Beräknar det n:te värdet för summorna
san = []
sgn = []
for i in range(n):
    a_i = a_1 + d[i] * (i)
    g_i = g_1 * q[i] ** (i)
    san.append(a_i)
    sgn.append(g_i)

if __name__ == "__main__":
    print(sum(san))
    print(sum(sgn))
    print(f"Ett sparkapital på {g_1} ger en avkastning på {sum(sgn) - g_1} under {n} månader.")


