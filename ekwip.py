ekwipunek = {
    "miecz": {"ilosc": 1, "waga": 5, "wartosc": 30},
    "mikstura": {"ilosc": 3, "waga": 1, "wartosc": 10}
}

zloto = 50
maks_waga = 30

sklep = {
    "tarcza": {"waga": 8, "wartosc": 25},
    "luk": {"waga": 4, "wartosc": 20},
    "mikstura": {"waga": 1, "wartosc": 10},
    "miecz": {"waga": 5, "wartosc": 30}
}

def oblicz_wage():
    suma = 0
    for nazwa in ekwipunek:
        suma += ekwipunek[nazwa]["waga"] * ekwipunek[nazwa]["ilosc"]
    return suma

def pokaz_przedmioty():
    print("\n--- EKWIPUNEK ---")
    if len(ekwipunek) == 0:
        print("Ekwipunek jest pusty.")
    for nazwa in ekwipunek:
        print(nazwa,
              "| Ilosc:", ekwipunek[nazwa]["ilosc"],
              "| Waga:", ekwipunek[nazwa]["waga"],
              "| Wartosc:", ekwipunek[nazwa]["wartosc"])
    print("Zloto:", zloto)
    print("Waga:", oblicz_wage(), "/", maks_waga)

def dodaj_przedmiot():
    global zloto
    print("\n--- SKLEP ---")
    for nazwa in sklep:
        print(nazwa,
              "| Cena:", sklep[nazwa]["wartosc"],
              "| Waga:", sklep[nazwa]["waga"])
    wybor = input("\nCo chcesz kupic? ").lower()
    if wybor not in sklep:
        print("Nie ma takiego przedmiotu w sklepie.")
        return
    cena = sklep[wybor]["wartosc"]
    waga = sklep[wybor]["waga"]

    if zloto < cena:
        print("Nie masz wystarczajaco zlota!")
        return
    if oblicz_wage() + waga > maks_waga:
        print("Nie masz miejsca w ekwipunku!")
        return
    zloto -= cena
    if wybor in ekwipunek:
        ekwipunek[wybor]["ilosc"] += 1
    else:
        ekwipunek[wybor] = {
            "ilosc": 1,
            "waga": waga,
            "wartosc": cena
        }
    print("Kupiono:", wybor)

def uzyj_przedmiotu():
    wybor = input("\nJaki przedmiot chcesz uzyc? ").lower()
    if wybor in ekwipunek:
        ekwipunek[wybor]["ilosc"] -= 1
        if ekwipunek[wybor]["ilosc"] == 0:
            del ekwipunek[wybor]
        print("Uzyto przedmiotu:", wybor)
    else:
        print("Nie posiadasz takiego przedmiotu.")

def sprawdz_przedmiot():
    wybor = input("\nJakiego przedmiotu szukasz? ").lower()
    if wybor in ekwipunek:
        print("Posiadasz ten przedmiot.")
        print("Ilosc:", ekwipunek[wybor]["ilosc"])
        print("Waga:", ekwipunek[wybor]["waga"])
        print("Wartosc:", ekwipunek[wybor]["wartosc"])
    else:
        print("Nie posiadasz tego przedmiotu.")

def sprzedaj_przedmiot():
    global zloto
    wybor = input("\nCo chcesz sprzedac? ").lower()
    if wybor not in ekwipunek:
        print("Nie posiadasz takiego przedmiotu.")
        return
    cena = ekwipunek[wybor]["wartosc"] // 2
    zloto += cena
    ekwipunek[wybor]["ilosc"] -= 1
    if ekwipunek[wybor]["ilosc"] == 0:
        del ekwipunek[wybor]
    print("Sprzedano:", wybor)
    print("Otrzymano zlota:", cena)
  
while True:
    print("\n===== MENU =====")
    print("1. Pokaz przedmioty")
    print("2. Dodaj przedmiot (sklep)")
    print("3. Uzyj przedmiotu")
    print("4. Sprawdz przedmiot")
    print("5. Wyjdz")
    print("6. Sprzedaj przedmiot")
    wybor = input("Wybierz opcje: ")
    if wybor == "1":
        pokaz_przedmioty()
    elif wybor == "2":
        dodaj_przedmiot()
    elif wybor == "3":
        uzyj_przedmiotu()
    elif wybor == "4":
        sprawdz_przedmiot()
    elif wybor == "5":
        print("Koniec gry!")
        break
    elif wybor == "6":
        sprzedaj_przedmiot()
    else:
        print("Nieprawidlowa opcja!")
