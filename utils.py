from datetime import datetime
import os


if not os.path.exists("evidencia"):
    os.makedirs("evidencia")

def tomar_captura(driver, nombre_base):
    """Toma una captura con timestamp en la carpeta evidencia."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"evidencia/{nombre_base}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f" Captura guardada: {filename}")
