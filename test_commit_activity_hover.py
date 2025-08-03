from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Открытие страницы
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")

# Подождём, чтобы страница догрузилась
time.sleep(5)

# 2. Наведение мышки на один из столбцов графика (берём, к примеру, первый)
bar = driver.find_element(By.CSS_SELECTOR, "g.rects > rect")  # находим первый rect в svg графика

# Используем ActionChains для наведения мыши
hover = ActionChains(driver).move_to_element(bar)
hover.perform()

# 3. Проверка появления всплывающей подсказки
time.sleep(2)  # ждем появления тултипа

# Ищем элемент тултипа
tooltip = driver.find_elements(By.CSS_SELECTOR, ".commit-activity-tooltip, .d3-tip")
if tooltip and tooltip[0].is_displayed():
    print("✅ Мышка навелась корректно, тултип найден!")
else:
    print("❌ Тултип не найден, возможна ошибка.")

# Финализируем тест
driver.quit()
