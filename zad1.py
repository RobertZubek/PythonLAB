def mnozenie_macierzy(macierz_a, macierz_b):
    if len(macierz_a[0]) != len(macierz_b):
        raise ValueError("Liczba kolumn w macierzy A musi być równa liczbie wierszy w macierzy B.")

    wynik = [[0 for k in range(len(macierz_b[0]))] for i in range(len(macierz_a))]

    for i in range(len(macierz_a)):  
        for j in range(len(macierz_b[0])): 
            for k in range(len(macierz_b)):
                wynik[i][j] += macierz_a[i][k] * macierz_b[k][j]

    return wynik

macierz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

macierz_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

wynik = mnozenie_macierzy(macierz_a, macierz_b)

print("Macierz A:")
for row in macierz_a:
    print(row)

print("\nMacierz B:")
for row in macierz_b:
    print(row)

print("\nMacierz wynikowa (A * B):")
for row in wynik:
    print(row)
