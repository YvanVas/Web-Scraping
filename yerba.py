# Importar libreria de bs4 de web scraping
from bs4 import BeautifulSoup
import requests
# La funcion recibe el link de la pag. y lo interpreta como un html,
# busca la etiqueta 'span' y la clase donde se encuentra la información
# que queremos obtener, luego retorna un texto con el contenido cargado
def buscarPrecio(pagina):
    # Contenido de la pagina y html parse es para interpretar como html
    pageContent = BeautifulSoup(pagina.content, 'html.parser')
    # Descomponer la pagina y buscar la etiqueta de los precios
    x = pageContent.find('span', class_='productPrice')    
    # se extrae solo el texto que contiene el dato obtenido
    return x.text.replace("Gs    ","Gs ")
# Se carga el contenido del html
urlKurupi500 = 'https://www.stock.com.py/products/2644-yerba-mate-menta-y-boldo-kurupi-500gr.aspx'
pageKurupi500 = requests.get(urlKurupi500)
urlKurupi250 = 'https://www.stock.com.py/products/8236-yerba-mate-kurupi-x-250-grs.aspx'
pageKurupi250 = requests.get(urlKurupi250)
precioK500 = buscarPrecio(pageKurupi500)
precioK250 = buscarPrecio(pageKurupi250)
