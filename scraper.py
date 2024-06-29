# giladón para sacar palabras de por ahí

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.diccionarioargentino.com/terms"


response = requests.get(url)

# Configurar Selenium
chrome_options = Options()
chrome_options.add_argument(
    "--headless"
)  # Para que no se abra una ventana del navegador
service = Service(ChromeDriverManager().install())

# Hacer la solicitud con Selenium
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

lista = driver.find_element(By.CLASS_NAME, "terms")

a = lista.find_elements(By.CSS_SELECTOR, "a")
print(len(a))

dicc = {}
palabras = []
for idx, item in enumerate(a):
    palabras.append(item.text.replace(" ", ""))

dicc["palabras"] = palabras
df = pd.DataFrame(dicc)
df.to_csv("argentinas.csv", index=False)
