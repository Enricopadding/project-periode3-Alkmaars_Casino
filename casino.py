class CurrencySystem:
    exchange_rates = {
        "EUR": 1.0,    # Basisvaluta
        "USD": 1.08,   # 1 EUR = 1.08 USD (voorbeeldkoers)
        "GBP": 0.85    # 1 EUR = 0.85 GBP (voorbeeldkoers)
    }

    def __init__(self, saldo, currency="EUR"):
        self.saldo = saldo
        self.currency = currency

    def convert_to_currency(self, amount, target_currency):
        if target_currency not in self.exchange_rates:
            raise ValueError("Ongeldige valuta.")
        return amount * (self.exchange_rates[target_currency] / self.exchange_rates[self.currency])

def kies_valuta():
    while True:
        currency = input("Kies je valuta (EUR, USD, GBP): ").upper()
        if currency in CurrencySystem.exchange_rates:
            return currency
        print("Ongeldige valuta. Kies uit EUR, USD of GBP.")

start_saldo = 500
valuta = kies_valuta()
currency_system = CurrencySystem(start_saldo, valuta)
