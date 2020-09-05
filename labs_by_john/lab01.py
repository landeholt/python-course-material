# DD1315    John Landeholt
# Lab 1     I-17

# Ansätter variblernas värde
a_1 = 5
d   = 2
g_1 = 5
q   = 2
n   = 10

# Beräknar det n:te värdet där det går
a_n = a_1 + d * (n - 1)

# Beräknar summan i båda talföljderna
san = (n/2) * (a_1 + a_n)
sgn = g_1 * (q ** n - 1) / (q - 1)

# Presenterar resultatet
if __name__ == "__main__":
    print(san)
    print(sgn)



