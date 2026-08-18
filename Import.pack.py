import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
WebDriverWait(driver, 3)

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

driver.find_element(By.ID, "email").send_keys("langosta@gmail.com")
driver.find_element(By.ID, "password").send_keys("cacota")

time.sleep(10)

driver.find_element(By.CLASS_NAME, "auth-form__button").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

assert driver.current_url == "https://around-v1.nm.tripleten-services.com/"
print ("Pruebas exitosas")
# ACCEDER A LOS ATRIBUTOS

#<div class="profile__image" style="background-image": url("https://example.com/files/profile-pic.png");>...</div>



driver.quit() # cerrar ventana
