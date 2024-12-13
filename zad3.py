import heapq


def dijkstra(graf, start):

    odleglosci = {wierzcholek: float('inf') for wierzcholek in graf}
    odleglosci[start] = 0
    kolejka = [(0, start)]
    poprzednicy = {wierzcholek: None for wierzcholek in graf}

    while kolejka:
        aktualna_odleglosc, aktualny_wierzcholek = heapq.heappop(kolejka)

        if aktualna_odleglosc > odleglosci[aktualny_wierzcholek]:
            continue

        for sasiad, waga in graf[aktualny_wierzcholek]:
            droga = aktualna_odleglosc + waga

            if droga < odleglosci[sasiad]:
                odleglosci[sasiad] = droga
                poprzednicy[sasiad] = aktualny_wierzcholek
                heapq.heappush(kolejka, (droga, sasiad))

    return odleglosci, poprzednicy


def najkrotsza_sciezka(poprzednicy, start, cel):

    sciezka = []
    obecny = cel
    while obecny is not None:
        sciezka.append(obecny)
        obecny = poprzednicy[obecny]
    sciezka.reverse()
    if sciezka[0] == start:
        return sciezka
    else:
        return None


if __name__ == "__main__":
    graf = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start = 'A'
    cel = 'D'

    odleglosci, poprzednicy = dijkstra(graf, start)

    print(f"Najkrótsze odległości od węzła '{start}': {odleglosci}")
    print(f"Poprzednicy: {poprzednicy}")

    sciezka = najkrotsza_sciezka(poprzednicy, start, cel)
    if sciezka:
        print(f"Najkrótsza ścieżka z '{start}' do '{cel}': {' -> '.join(sciezka)}")
    else:
        print(f"Brak ścieżki z '{start}' do '{cel}'.")
