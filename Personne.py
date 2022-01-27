class Personne:
    def __init__(self, nom: str, age: int) -> None:
        self.nom = nom
        self.age = age

    def get_name(self) -> str:
        return self.__nom

    def get_age(self) -> str:
        return self.age

