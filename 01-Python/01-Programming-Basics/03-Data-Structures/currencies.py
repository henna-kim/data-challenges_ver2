# pylint: disable=missing-docstring

RATES = {"USDEUR": 0.85,
         "GBPEUR": 1.13,
         "CHFEUR": 0.86,
         "EURGBP": 0.885}

def convert(amount, currency):
    currencies = amount[1] + currency
    if currencies in RATES:
        return round(RATES[currencies] * amount[0])
    return None
