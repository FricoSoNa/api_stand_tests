import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(40)
wait = WebDriverWait(driver, 40)
driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es') #abrir página

"driver.maximize_window()" # Modo de pantalla completa

driver.find_element(By.ID, "email").send_keys("langosta@gmail.com")
driver.find_element(By.ID, "password").send_keys("cacota")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card__image")))

element = driver.find_element(By.TAG_NAME, "footer")

driver.execute_script("arguments[0].scrollIntoView();",element)

assert 'Around' in element.text

driver.quit() # cerrar ventana
