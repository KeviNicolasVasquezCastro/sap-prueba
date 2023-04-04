from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# configuración de Chrome para abrir en modo incógnito
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# crea una instancia de WebDriver de Chrome con la configuración personalizada
driver = webdriver.Chrome(chrome_options=chrome_options)


# maximizar la ventana de Chrome.
driver.maximize_window()

driver.get('https://my361486.crm.ondemand.com/sap/ap/ui/clogin?saml2=disabled&app.component=/SAP_UI_CT/Main/root.uiccwoc&rootWindow=X&redirectUrl=/sap/public/byd/runtime')

# ingresar usuario y contraseña.
usuario = driver.find_element(By.XPATH, "//*[@id='USERNAME_FIELD-inner']").send_keys("kvasquez")

contraseña = driver.find_element(By.XPATH, "//*[@id='PASSWORD_FIELD-inner']").send_keys("Colombia2026-")

# darle click al boton de iniciar sesion.

boton = driver.find_element(By.XPATH, "//*[@id='LOGIN_LINK']").click()

time.sleep(7)

# darle click al boton de servicio.

botonservicio = driver.find_element(By.XPATH, "//*[@id='__toolbar8']").click()

time.sleep(0.5)

# darle click al boton de tickets.

botonticket = driver.find_element(By.XPATH, "//*[@id='__link26']").click()

time.sleep(4)

# darle click al boton de +.

botonmas = driver.find_element(By.XPATH, "//*[@id='buttonMyhsQOk2saslFBU5NpnmTW_130-img']").click()

time.sleep(6)

# introducir cliente.

input_element = driver.find_element(By.XPATH, "//*[@id='objectvalueselectorI7pYpVvFLKch84EsXeFzk0_602-inputField']")
span_element = input_element.find_element(By.TAG_NAME, "span").click()

time.sleep(2)

botonfiltro = driver.find_element(By.XPATH, "//*[@id='findformpaneFindFormPane_ID_683']").click()

time.sleep(2)

codigounico = "024351041"

cu = driver.find_element(By.XPATH, "//*[@id='inputfieldfacaf9767aaad205e608005c2cab9a21_709-inner']")

cu.send_keys(codigounico)

cu.send_keys(Keys.ENTER)

time.sleep(2)

codigounico = driver.find_element(By.XPATH, "//*[@id='statictextooAT7P0BV46hbJtiB49eWG_660-listdefintionG3ws9fm8F4M0zWzfo_shp1G_654-0']").click()

time.sleep(3)

# añadir producto.
producto = driver.find_element(By.XPATH, "//*[@id='navigationitemnLj_abWLka6LtpHd3eUlqG_160']").click()

time.sleep(1)

añadir = driver.find_element(By.XPATH, "//*[@id='buttonMJfG64VVQaE_2afTRvvUWG_784']").click()

time.sleep(1)

usuario = driver.find_element(By.XPATH, "//*[@id='objectvalueselectorne2Z4Bo6Lq25JpFbxu5XpW_852-inputField-inner']").send_keys("50100049")



time.sleep(10)

# Cierra la ventana de Chrome.
driver.quit()