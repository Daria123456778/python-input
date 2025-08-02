from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_github_advanced_search():
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    try:
        # 1. Открыть страницу поиска
        driver.get("https://github.com/search/advanced")
        time.sleep(2)

        # 2. Выбрать язык "Python"
        language_select = Select(driver.find_element(By.ID, "search_language"))
        language_select.select_by_visible_text("Python")
        time.sleep(1)

        # 3. Ввести >20000 в поле stars
        stars_input = driver.find_element(By.NAME, "stars")
        stars_input.clear()
        stars_input.send_keys(">20000")
        time.sleep(1)

        # 4. Ввести environment.yml в нужное поле
        filename_input = driver.find_element(By.NAME, "filename")
        filename_input.clear()
        filename_input.send_keys("environment.yml")
        time.sleep(1)

        # 5. Нажать на кнопку поиска
        search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
        search_button.click()
        time.sleep(8)  # Оставляем время на проверку результатов глазами

        # 6. (Пауза для визуальной проверки)
        print("Проверь глазами репозитории согласно выбранным критериям!")

    finally:
        time.sleep(10)  # Оставляем открытым окно на 10 сек
        driver.quit()

if __name__ == "__main__":
    test_github_advanced_search()
