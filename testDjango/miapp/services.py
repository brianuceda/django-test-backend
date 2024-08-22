from django.http import JsonResponse
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch

def search_youtube(search):
    try:
        response = YoutubeSearch(search, max_results=1).to_json()
        response_dict = json.loads(response)
        return JsonResponse(response_dict)
    except Exception as e:
        return JsonResponse({'error': str(e)})

def search_birthday_by_separated_names(name, father_last_name, mother_last_name):
    # Configuración de Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Ejecuta en segundo plano
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # URL de la página a scrapear
        url = "https://el-dni.com/buscar-cumpleanios-por-nombres/"
        driver.get(url)

        # Esperar a que el formulario esté presente
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "search-cumple"))
        )

        # Llenar el formulario
        driver.find_element(By.ID, "nombres").send_keys(name)
        driver.find_element(By.ID, "ape_pat").send_keys(father_last_name)
        driver.find_element(By.ID, "ape_mat").send_keys(mother_last_name)

        # Hacer clic en el botón "BUSCAR"
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.mb-3").click()

        # Esperar a que el resultado de "numero2" esté presente
        WebDriverWait(driver, 60).until(
            lambda d: d.find_element(By.ID, "numero2").text.strip() != ""
        )

        # Obtener el valor de "numero2" que es el cumpleaños
        cumpleanios = driver.find_element(By.ID, "numero2").text.strip()

        # Retornar el resultado en un diccionario
        response = {
            "cumpleanos": cumpleanios
        }
    except Exception as e:
        print(f"Error occurred: {e}")
        response = {
            "cumpleanos": "Error 2"
        }
    finally:
        # Cerrar el navegador
        driver.quit()
        return JsonResponse(response)
    