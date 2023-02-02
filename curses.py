
def convert_currency(BD,amount, chat_id, to_rub=False,currency=""):
    if not to_rub:
        return amount / BD.get_currencies()[currency]
    else:

        return amount * BD.get_currencies()[currency]


def formatted_currency(BD,amount, chat_id,currency):
    if currency != "RUB":
        return f'{convert_currency(BD,amount, chat_id,currency=currency):.2f} {currency.upper()}'
    else:
        return f'{convert_currency(BD,amount, chat_id,True,currency=currency):.2f} {currency.upper()}'