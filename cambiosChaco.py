if __name__ == "__main__":
    # se importa la libreria para recoger los datos de la pagina
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd

    url = 'https://www.cambioschaco.com.py/'
    page = requests.get(url)
    # Se carga el contenido del html
    url = 'https://www.cambioschaco.com.py/'
    page = requests.get(url)

    # contenido de la pagina y html parse para que interprete como html
    soup = BeautifulSoup(page.content, 'html.parser')

    error = soup.find(text='502 Bad Gateway')

    if error:
        print(error)
    else:
        
        # Nombre de las monedas, Compras y Ventas
        coinName = soup.find_all('a')
        purchase = soup.find_all('span', class_='purchase')
        sale = soup.find_all('span', class_='sale')
        monedas = list()
        compras = list()
        ventas = list()
        count = 0
        # Se saca los datos de las etiquetas <a>
        for i in coinName:
            # se filtra los datos de los nombres de las monedas en la lista
            if count > 14 and count < 37:
                # se guarda los valores en una lista
                monedas.append(i.text)
                count += 1
                # Se guarda los datos de las compras
            
            count2 = 0
            for j in purchase:
                # se filtra la cantidad de valores
                if count2 < 22:
                    compras.append(j.text)
                else:
                    break
                count2 += 1
            # Se guarda los datos de las ventas
            count3 = 0
            for h in sale:
                # se filtra la cantidad de valores
                if count3 < 22:
                    ventas.append(h.text)
                else:
                    break
                count3 += 1
            # se crea un diccionario para tener una vista de tabla de los valores
            # se utiliza la libreria panda para generar el diccionario
            df = pd.DataFrame(
                {
                    'Monedas': monedas,
                    'Compras': compras,
                    'Ventas': ventas
                },
                index=list(range(1, 23))
            )
            print(df)
            print("Dolar:\nCompra:", compras[0], "\nVenta:", ventas[0])
            
