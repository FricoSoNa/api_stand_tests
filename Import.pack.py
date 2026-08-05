from selenium import webdriver

driver = webdriver.Chrome()
"driver.maximize_window()" # Modo de pantalla completa

"assert driver.current_url == 'https://www.google.com/'" # obtener url de un sitio
"assert google.com' in driver.current_url" # comprobar solo unaparte del url



driver.get('https://www.google.com/')

"chrome_options = webdriver.ChromeOptions()"
"chrome_options.add_argument('--headless') # Ejecuta el navegador desde la terminal sin una interfaz gráfica"
"chrome_options.add_argument('--window-size=640,480') # Ajusta el tamaño de la ventana a 640 x 480 pixeles"
"driver = webdriver.Chrome(options=chrome_options) # Crea un controlador y pasa la configuración de los ajustes establecidos"

driver.quit()
