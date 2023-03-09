def countingSort(array):
    nilaiMaksimum = max(array)
    hitung = [0] * (nilaiMaksimum + 1)

    # Menghitung frekuensi kemunculan setiap nilai pada array
    for nilai in array:
        hitung[nilai] += 1

    # Menghitung kumulatif frekuensi kemunculan setiap nilai
    hasilPengurutan = []
    for i in range(len(hitung)):
        for j in range(hitung[i]):
            hasilPengurutan.append(i)

    return hasilPengurutan

#mengisi array dengan 10 nilai berupa angka
array = [5, 2, 7, 3, 9, 4, 1, 6, 8]
#menampilkan array sebelum diurutkan
print("Array sebelum diurutkan:", array)
#mengurutkan array
hasilPengurutan = countingSort(array)
#menampilkan hasilPengurutan pengurutan
print("Array setelah diurutkan:", hasilPengurutan)

