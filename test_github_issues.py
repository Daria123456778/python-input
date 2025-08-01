from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_github_issue_search_by_author():
    service = Service ("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    try:
    # 1. Открываем страницу issues
        driver. get ("https://github.com/microsoft/vscode/issues")
        time sleep (2)
    # 2. Нажать на кнопку Author
        author_button =driver. find_element (By.XPATH, "//summary [contains.,'Author') ]")
        author_button. click()
        time.sleep (1)
    # 3. Ввести имя автора
        author_search =driver. find_element(By. CSS_SELECTOR, "inputlaria-label='Type or choose an option']")
        author_search. send_keys("bpasero" )
        time. sleep (2)
    # 4. Выбрать из выпавшего списка
        author_option=driver. find_element (By.XPATH, "//label[contains.,'bpasero') ]")
        author_option.click()
        time. sleep(5) # дайте время увидеть вкладку глазами
# На этом шаге можно глазами убедиться, что задачи только от автора bpasero
    finally:
        print ("Проверь глазами задачи - остались только от автора bpasero?")
        time.sleep (10) # Ждём, чтобы можно было проверить глазами
        driver.quit ()

if __name__ == "__main__":
    test_github_issue_search_by_author()
