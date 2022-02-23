# se importa la libreria para recoger los datos de la pagina
from bs4 import BeautifulSoup
import requests
import pandas as pd


def filter_list(list: list) -> list:
    """
    Recibe una lista, filtra los textos dentro de la etiqueta al final retorna la lista tratada.
    """
    list_filtered = []
    for item in list:
        item = item.text
        list_filtered.append(item)

    return list_filtered


def main() -> None:
    url = 'https://www.cambioschaco.com.py/'
    page = requests.get(url).content

    status = requests.get(url).status_code

    if status != 200:
        print('Page error')
    else:
        soup = BeautifulSoup(page, 'html.parser')

        # Se filtra la tabla por nombres, compra y ventas
        table_coins = soup.find(id='main-exchange-content')
        all_coins_names = table_coins.find_all('a')
        all_coins_purchase = table_coins.find_all(class_='purchase')
        all_coins_sale = table_coins.find_all(class_='sale')

        coins_name = filter_list(all_coins_names)
        coins_purchase = filter_list(all_coins_purchase)
        coins_sale = filter_list(all_coins_sale)

        table = pd.DataFrame(
            {
                'Moneda': coins_name,
                'Compra': coins_purchase,
                'Venta': coins_sale
            }
        )
        print(table)

        # print(tableCoins)


if __name__ == "__main__":
    main()
