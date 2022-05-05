from requests import get, utils
from datetime import date

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    content = response.split('<Valute ID=')
    d, m, y = content[0].split()[3].split('Date=')[1][1:-1].split('.')

    for i in content:
        if code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=', ')
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('eur'))
    print(currency_rates('usd'))
    print(currency_rates('gbp'))