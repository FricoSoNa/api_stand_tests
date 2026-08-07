import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

# PANTALLA COMPLETA
{
"driver.maximize_window()" # Modo de pantalla completa
}

driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es') #abrir página

{
"assert '/signin' in driver.current_url # comprobar solo una parte del url"

"assert driver.current_url == 'https://around-v1.nm.tripleten-services.com/signin?lng=es'" # obtener url de un sitio
}
# CHROME OPTIONS
{
"chrome_options = webdriver.ChromeOptions()"

"chrome_options.add_argument('--headless')" # Ejecuta el navegador desde la terminal sin una interfaz gráfica"

"chrome_options.add_argument('--window-size=640,480')" # Ajusta el tamaño de la ventana a 640 x 480 pixeles"

"driver = webdriver.Chrome(options=chrome_options)" # Crea un controlador y pasa la configuración de los ajustes establecidos"
}

time.sleep(10) # tiempo de espera para el siguiente

# CLASE BY
{
"By.CLASS_NAME" # por nombre de clase
"By.CSS_SELECTOR" # buscar por selector CSS
"By.ID" # buscar por atributo ID
"By.LINK_TEXT" # buscar por el texto del enlace
"By.PARTIAL_LINK_TEXT" # buscar por una parte del texto del enlace
"By.NAME" # buscar por el atributo name
"By.TAG_NAME" # buscar por la etiqueta HTML
"By.XPATH" # buscar por XPATH
}
tittle_element = driver.find_element(By.CSS_SELECTOR,".auth-form__title")
print("Login form tittle:", tittle_element.text)

# ACCEDER A LOS ATRIBUTOS

#<div class="profile__image" style="background-image": url("https://example.com/files/profile-pic.png");>...</div>



driver.quit() # cerrar ventana
