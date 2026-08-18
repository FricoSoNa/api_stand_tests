import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# PANTALLA COMPLETA
"driver.maximize_window()" # Modo de pantalla completa

driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es') #abrir página

wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("langosta@gmail.com")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("cacota")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".auth-form__button"))).click()

logout_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header__logout"))).text

assert logout_text.strip() == 'Cerrar sesión', f"Se esperaba 'Cerrar sesión', pero se obtuvo '[logout_text]'"

print ("Pruebas exitosas")

driver.quit() # cerrar ventana
