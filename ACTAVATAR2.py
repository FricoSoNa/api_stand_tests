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
driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es') #abrir página
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

"driver.maximize_window()" # Modo de pantalla completa

driver.find_element(By.ID, "email").send_keys("langosta@gmail.com")
driver.find_element(By.ID, "password").send_keys("cacota")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

driver.find_element(By.CSS_SELECTOR, ".profile__image").click()

avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Guardar']").click()

wait.until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), "style", avatar_url))
style = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute("style")
assert avatar_url in style

driver.quit() # cerrar ventana
