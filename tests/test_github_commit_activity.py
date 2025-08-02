import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


def test_hover_on_commit_graph():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.implicitly_wait(10)

        # Найди столбец графика (bar), например, первый
        bar = driver.find_element(By.CSS_SELECTOR, '.js-graph-bar')

        # Наведи мышь на этот столбец
        ActionChains(driver).move_to_element(bar).perform()

        # Дождись отображения тултипа
        tooltip = driver.find_element(By.CLASS_NAME, 'CommitActivityGraph-tooltips')
        assert tooltip.is_displayed()
    finally:
        driver.quit()
