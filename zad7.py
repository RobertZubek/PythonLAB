from dataclasses import dataclass, asdict
import json


@dataclass
class PersonalData:
    name: str
    surname: str
    address: str
    postal_code: str
    pesel: str

    def save_to_JSON(self, path: str):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(asdict(self), file,)

    @classmethod
    def read_from_JSON(cls, path: str):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return cls(**data)


if __name__ == "__main__":
    person = PersonalData(
        name="Robert",
        surname="Zubek",
        address="ul. Wizjonerow 5/97, Cracow",
        postal_code="31-356",
        pesel="12345678901"
    )

    path = "personal_data.json"
    person.save_to_JSON(path)
    print(f"Data saved to file: {path}")

    new_person = PersonalData.read_from_JSON(path)
    print("Read data:")
    print(f"Name: {new_person.name}")
    print(f"Surname: {new_person.surname}")
    print(f"Address: {new_person.address}")
    print(f"Postal code: {new_person.postal_code}")
    print(f"PESEL: {new_person.pesel}")
