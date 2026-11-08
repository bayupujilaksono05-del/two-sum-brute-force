def two_sum_brute_force(angka, target):
    """
    Mencari semua pasangan angka yang jumlahnya sama dengan target.
    Setiap pasangan diperiksa satu per satu menggunakan dua perulangan.
    """
    pasangan = []

    for i in range(len(angka)):
        for j in range(i + 1, len(angka)):
            if angka[i] + angka[j] == target:
                pasangan.append((angka[i], angka[j]))

    return pasangan

angka = [2, 7, 11, 15, 3, 6]
target = 18

print("Daftar angka :", angka)
print("Target       :", target)

hasil = two_sum_brute_force(angka, target)

if hasil:
    print("\nPasangan angka yang jumlahnya sama dengan target:")
    for nomor, (a, b) in enumerate(hasil, start=1):
        print(f"{nomor}. {a} + {b} = {target}")
else:
    print("\nTidak ditemukan pasangan angka.")