class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupnost=True) -> None:
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = dostupnost

    def pujc_auto(self):
        """
        pokud je vozidlo volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text 
        "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".
        """
        if self.dostupnost:
            self.dostupnost = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Vozidlo má registrační značku {self.registracni_znacka}, a je o typ vozidla {self.typ_vozidla}."

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

vozidlo_uzivatele = input("Jaké si přejete půjčit vozidlo (Peugeot nebo Škoda): ")

zvolene_vozidlo = None

if vozidlo_uzivatele.lower() == "peugeot":
    zvolene_vozidlo = auto1
elif vozidlo_uzivatele.lower() == "škoda":
    zvolene_vozidlo = auto2
else:
    print("Zvolená značka není v naší evidenci.")

if zvolene_vozidlo is not None:
    print(zvolene_vozidlo.get_info())
    print(zvolene_vozidlo.pujc_auto())



