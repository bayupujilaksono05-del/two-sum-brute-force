angka = list(map(int, input("Masukkan daftar angka (pisahkan dengan spasi): ").split()))
target = int(input("Masukkan angka target: "))

pasangan_ditemukan = False

print("\nHasil pencarian:")

for i in range(len(angka)):
    for j in range(i + 1, len(angka)):
        if angka[i] + angka[j] == target:
            print(f"{angka[i]} + {angka[j]} = {target}")
            pasangan_ditemukan = True

if not pasangan_ditemukan:
    print("Tidak ditemukan pasangan angka yang sesuai.")