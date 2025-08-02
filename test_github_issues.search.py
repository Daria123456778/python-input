from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_github_issue_search():
    # Настройка драйвера
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    try:
        # 1. Открываем страницу issues в репозитории vscode
        driver.get("https://github.com/microsoft/vscode/issues")
        time.sleep(2)  # Подождать, чтобы страница точно загрузилась

        # 2. Находим строку поиска и очищаем её
        search_box = driver.find_element(By.CSS_SELECTOR, "input.js-issues-search")
        search_box.clear()

        # 3. Вводим фильтр in:title bug
        search_box.send_keys("in:title bug")
        time.sleep(1)

        # 4. Нажимаем Enter для поиска
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)  # Ждем, чтобы визуально увидеть результат

        # На этом этапе можно глазами убедиться, что отображаются задачи с "bug" в заголовке

    finally:
        # 5. Останавливаем автотест
        print("Проверь глазами результаты поиска — отображаются только задачи со словом 'bug' в заголовке?")
        time.sleep(10)  # Оставляем браузер открытым на 10 сек, чтобы посмотреть вручную
        driver.quit()

if __name__ == "__main__":
    test_github_issue_search()