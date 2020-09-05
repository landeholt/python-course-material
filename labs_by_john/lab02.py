# DD1315    John Landeholt
# Lab 2     I-17

# Låter användaren ansätta variblernas värde
print("värde för a_1:")
a_1 = int(input("> "))
print("värde för d:")
d   = int(input("> "))
print("värde för g_1:")
g_1 = int(input("> "))
print("värde för q:")
q   = int(input("> "))
print("värde för n:")
n   = int(input("> "))

if q == 1:
    print("Otillåtet att dividera med 0. Ange q > 1")
    print("värde för q:")
    q   = int(input("> "))

# Beräknar det n:te värdet där det går
a_n = a_1 + d * (n - 1)

# Beräknar summan i båda talföljderna
san = (n/2) * (a_1 + a_n)
sgn = g_1 * (q ** n - 1) / (q - 1)

# Jämför summorna
if san > sgn:   ans = "Den aritmetiska summan är störst"
elif san < sgn: ans = "Den geometriska summan är störst"
else:           ans = "Summorna är lika"

# Presenterar resultatet
if __name__ == "__main__":
    print(san)
    print(sgn)
    print(ans)