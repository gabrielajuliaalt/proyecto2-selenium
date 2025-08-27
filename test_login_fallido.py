from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from utils import tomar_captura


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    print(" Iniciando prueba de LOGIN FALLIDO...")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)

  
    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    try:
        mensaje = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Username and password do not match" in mensaje
        print(" Mensaje de error mostrado correctamente.")
        tomar_captura(driver, "login_fallido_con_mensaje")

    except NoSuchElementException:
        print(" No se encontró el mensaje de error.")
        tomar_captura(driver, "login_fallido_sin_mensaje")

except Exception as e:
    print(f" Error durante la prueba de login fallido: {e}")
    tomar_captura(driver, "error_login_fallido")

finally:
    driver.quit()
    print(" Prueba finalizada.")
