from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from utils import tomar_captura


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    print(" Iniciando prueba de LOGIN EXITOSO...")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

 
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"
    print(" Login exitoso confirmado.")
    tomar_captura(driver, "login_exitoso")

  
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    print(f" {len(productos)} productos mostrados.")
    tomar_captura(driver, "productos_mostrados")

 
    print(" Realizando logout...")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)
    print(" Logout exitoso.")
    tomar_captura(driver, "logout_exitoso")

except Exception as e:
    print(f" Error durante la prueba de login exitoso: {e}")
    tomar_captura(driver, "error_login_exitoso")

finally:
    driver.quit()
    print(" Prueba finalizada.")
