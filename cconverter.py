# write your code here!
import requests
import json

currencies = {}
# adding usd and eur to cache dictionary
for i in ['usd', 'eur']:
    r = requests.get("http://www.floatrates.com/daily/" + i + ".json")
    currencies[i] = json.loads(r.text)

origin_currency = input().lower()


while True:
    target_currency = input().lower()
    if target_currency == "":
        exit()
    amount = float(input())
    print('Checking the cache... ')
    if target_currency in currencies.keys():
        print('Oh! It is in the cache!')
        exchanged = amount / currencies[target_currency][origin_currency]['rate']
        new_currency = target_currency.upper()
        print(f'You received {round(exchanged,2)} {new_currency}.')

    else:
        print('Sorry, but it is not in the cache!')
        r = requests.get("http://www.floatrates.com/daily/" + target_currency + ".json")
        fx = json.loads(r.text)
        exchanged = amount / fx[origin_currency]['rate']
        new_currency = target_currency.upper()
        print(f"You received {round(exchanged,2)} {new_currency}.")
        currencies[target_currency] = fx