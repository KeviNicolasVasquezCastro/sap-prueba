from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


# maximizar la ventana de Chrome.
driver.maximize_window()

driver.get('https://my361486.crm.ondemand.com/sap/ap/ui/clogin?saml2=disabled&app.component=/SAP_UI_CT/Main/root.uiccwoc&rootWindow=X&redirectUrl=/sap/public/byd/runtime')

# ingresar usuario y contraseña.
usuario = driver.find_element(By.XPATH, "//*[@id='USERNAME_FIELD-inner']").send_keys("kvasquez")

contraseña = driver.find_element(By.XPATH, "//*[@id='PASSWORD_FIELD-inner']").send_keys("Colombia2028-")

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

time.sleep(7)

# ingresar cliente.

input_element = driver.find_element(By.XPATH, "//*[@id='objectvalueselectorI7pYpVvFLKch84EsXeFzk0_623-inputField-inner']")
span_element = input_element.find_element(By.XPATH, "//*[@id='objectvalueselectorI7pYpVvFLKch84EsXeFzk0_623-inputField-vhi']").click()

time.sleep(4)

botonfiltro = driver.find_element(By.XPATH, "//*[@id='findformpaneFindFormPane_ID_709-inner']").click()

time.sleep(2)

codigounico = "024351041"

cu = driver.find_element(By.XPATH, "//*[@id='inputfieldfacaf9767aaad205e608005c2cab9a21_735-inner']")

cu.send_keys(codigounico)

cu.send_keys(Keys.ENTER)

time.sleep(2)

codigounico = driver.find_element(By.XPATH, "//*[@id='__item225-listdefintionG3ws9fm8F4M0zWzfo_shp1G_680-0']").click()

time.sleep(3)

# ingresar asunto.

asunto = driver.find_element(By.XPATH, "//*[@id='inputfieldDJJuNyNvsqsbod89NjRCeW_624-inner']").send_keys("Ticket de prueba")

time.sleep(2)

# añadir producto.

producto = driver.find_element(By.XPATH, "//*[@id='objectvalueselectorKiq0_swnrw4A3HKbxwwRcvW_364-inputField-inner']")

producto.send_keys("PASARELAS EXTERNAS")

time.sleep(3)

# ingresar terminal.

terminalaingresar = "00004451"

terminal = driver.find_element(By.XPATH, "//*[@id='inputfield9e99b202ed0583b774ac9a8bf282547c_368-inner']")

terminal.send_keys(terminalaingresar)

time.sleep(3)

# Encontrar el elemento en el que deseas pegar el texto
descripcion = driver.find_element(By.XPATH, "//*[@id='__area0']").click()

time.sleep(3)

# Encontrar el iframe
iframe_xpath = "//*[@id='__area3-content'/table/tbody/tr[2]/td/iframe"
iframe = driver.find_element(By.XPATH, iframe_xpath)
iframe.send_keys("descripcion")

time.sleep(10)

# Cierra la ventana de Chrome.
driver.quit()
