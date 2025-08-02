from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_skillbox_filter():
    service = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # 1. Перейдем на сайт Skillbox с курсами программирования
        driver.get("https://skillbox.ru/code/")
        time.sleep(3)  # Ждем загрузки

        # 2. Кликаем по радио-баттону "Профессия" (обычно в разделе "Тип обучения на платформе")
        # Попробуем найти по тексту
        radio_label = driver.find_element(By.XPATH, "//label[contains(., 'Профессия')]")
        radio_label.click()
        time.sleep(2)

        # 3. Указываем длительность 6-12 месяцев (обычно реализовано ползунком)
        # Тут нужно найти ползунок, сдвинуть его мышкой
        slider = driver.find_element(By.XPATH, "//input[@type='range']")
        actions = ActionChains(driver)
        # Пробуем сделать движение вправо (чтобы задать диапазон 6-12)
        actions.click_and_hold(slider).move_by_offset(30, 0).release().perform()
        time.sleep(2)

        # 4. Выбираем любую тематику (чекбокс)
        # Выбираем первый доступный чекбокс
        checkbox = driver.find_element(By.XPATH, "//label[contains(@class, 'checkbox')][1]")
        checkbox.click()
        time.sleep(3)

        print("Проверьте глазами правильность отображения результатов (фильтр работает?)")
        time.sleep(10)  # Время на визуальную проверку

    finally:
        driver.quit()

if __name__ == "__main__":
    test_skillbox_filter()