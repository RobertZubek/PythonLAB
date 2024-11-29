import json


class DaneOsobowe:
    def __init__(self, imie, nazwisko, adres, kod_pocztowy, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.kod_pocztowy = kod_pocztowy
        self.pesel = pesel

    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "adres": self.adres,
            "kod_pocztowy": self.kod_pocztowy,
            "pesel": self.pesel,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["imie"],
            data["nazwisko"],
            data["adres"],
            data["kod_pocztowy"],
            data["pesel"],
        )

    def zapisz_do_json(self, sciezka):
        with open(sciezka, "w", encoding="utf-8") as plik:
            json.dump(self.to_dict(), plik)

    @classmethod
    def wczytaj_z_json(cls, sciezka):
        with open(sciezka, "r", encoding="utf-8") as plik:
            dane = json.load(plik)
        return cls.from_dict(dane)


if __name__ == "__main__":
    osoba = DaneOsobowe(
        "Robert", "Kowalski", "ul. Wizjonerow 5/97, Krakow", "31-356", "12345678901"
    )

    sciezka = "dane_osobowe.json"
    osoba.zapisz_do_json(sciezka)
    print(f"Dane zapisane do pliku: {sciezka}")

    nowa_osoba = DaneOsobowe.wczytaj_z_json(sciezka)
    print("Odczytane dane:")
    print(f"Imię: {nowa_osoba.imie}")
    print(f"Nazwisko: {nowa_osoba.nazwisko}")
    print(f"Adres: {nowa_osoba.adres}")
    print(f"Kod pocztowy: {nowa_osoba.kod_pocztowy}")
    print(f"PESEL: {nowa_osoba.pesel}")
