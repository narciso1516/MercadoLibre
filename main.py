from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Configura el navegador Chrome con el WebDriver correcto
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)

    try:
        # Paso 1: Acceder a Mercado Libre
        driver.get("https://www.mercadolibre.com")

        # Paso 2: Seleccionar México como país
        mexico_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/mexico')]")))
        mexico_button.click()

        # Paso 3: Buscar "playstation 5"
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "as_word")))
        search_box.send_keys("playstation 5")
        search_box.submit()

        # Paso 4: Filtrar por condición "Nuevos"
        new_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Nuevo')]")))
        new_filter.click()

        # Paso 5: Filtrar por ubicación "CDMX"
        location_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Distrito Federal')]")))
        location_filter.click()

        # Paso 6: Ordenar por "Mayor a Menor Precio"
        sort_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown')]")))
        sort_dropdown.click()
        high_to_low_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mayor precio')]")))
        high_to_low_option.click()

        # Paso 7: Obtener los nombres y precios de los primeros 5 productos
        products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='ui-search-layout__item']")))[:5]
        
        print("Los primeros 5 productos son:")
        for product in products:
            name = product.find_element(By.XPATH, ".//h2").text
            price = product.find_element(By.XPATH, ".//span[@class='price-tag-fraction']").text
            print(f"Producto: {name} - Precio: ${price}")

    finally:
        # Cierra el navegador
        driver.quit()

if __name__ == "__main__":
    main()
