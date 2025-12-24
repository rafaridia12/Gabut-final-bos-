import math

while True:
    print("\n=== Teorema Pytagoras Kalkulator cocok untuk pemalas ===")
    print("1. Cari sisi a")
    print("2. Cari sisi b")
    print("3. Cari sisi miring c")
    print("4. Udah ga ada soal lagi 😹")

    choice = input("Pilihnya Pakai Angka ya wok 😹: ")

    if choice == "1":
        b = float(input("Masukan sisi b: "))
        c = float(input("Masukan Sisi miring c: "))
        a = math.sqrt(c**2 - b**2)
        print("Sisi a =", a)

    elif choice == "2":
        a = float(input("Masukan sisi a: "))
        c = float(input("Masukan sisi miring  c: "))
        b = math.sqrt(c**2 - a**2)
        print("Sisi b =", b)

    elif choice == "3":
        a = float(input("masukan siai a: "))
        b = float(input("Masukan sisi b: "))
        c = math.sqrt(a**2 + b**2)
        print("Sisi miring  c =", c)

    elif choice == "4":
        print("Makasih sudah memggunakan script Ku ya wok, pasti nilai nanti dapat nilat 100 😹")
        break

    else:
        print("lu nulis apa sih kocak 😹.")

