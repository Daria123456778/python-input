from os import name
from tkinter.font import names

import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def open_google():
    # Автоматически загружаем ChromeDriver и создаем драйвер
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Открываем Google
    driver.get("https://www.google.com")

    # Ждем, пока пользователь закроет окно
    input("Нажмите Enter, чтобы закрыть браузер...")

    # Закрываем браузер
    driver.quit()


if name == "main":
    open_google()