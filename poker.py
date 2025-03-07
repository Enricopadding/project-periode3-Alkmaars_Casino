def kies_inzet(saldo):
    while True:
        try:
            inzet = float(input(f"Je hebt €{saldo:.2f}. Hoeveel wil je inzetten? €"))
            if inzet <= 0:
                print("Je inzet moet een positief bedrag zijn.")
            elif inzet > saldo:
                print("Je kunt niet meer inzetten dan je saldo.")
            else:
                return inzet
        except ValueError:
            print("Ongeldige invoer. Voer een numeriek bedrag in.")

saldo = 500
inzet = kies_inzet(saldo)
print(f"Je hebt €{inzet:.2f} ingezet.")
