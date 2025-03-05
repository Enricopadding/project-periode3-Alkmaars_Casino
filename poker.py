def betting_round(saldo, pot, hand_rank, is_ai=False, aggression=5, last_bet=0):
    if is_ai:
        return ai_decision(saldo, pot, hand_rank, aggression, last_bet)
    
    while True:
        try:
            inzet = int(input(f"Je saldo: €{saldo}, Pot: €{pot}. Vorige inzet: €{last_bet}. Hoeveel wil je inzetten? (€0 om te checken, -1 om te folden): "))
            if inzet < -1 or inzet > saldo:
                print("Ongeldige inzet.")
                continue
            if inzet == -1:
                print("Je foldt deze ronde!")
                return saldo, pot, -1
            if inzet < last_bet and inzet != 0:
                print(f"Je moet minimaal €{last_bet} inzetten om te callen of meer om te raisen.")
                continue
            saldo -= inzet
            pot += inzet
            return saldo, pot, inzet
        except ValueError:
            print("Voer een geldig bedrag in.")
