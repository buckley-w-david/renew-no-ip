import typing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_PAGE = "https://www.noip.com/login"

def renew(username: str, password: str, *, driver: typing.Optional['WebDriver'] = None) -> float:
    close_on_exit = driver is None
    if driver is None:
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        options.headless = False

        driver = webdriver.Firefox(options=options)

    driver.get(LOGIN_PAGE)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    username_field.send_keys(username)

    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)

    submit_button = driver.find_element_by_name('Login')
    submit_button.submit()
    WebDriverWait(driver, 10).until(
        EC.url_changes(LOGIN_PAGE)
    )

    driver.get('https://my.noip.com/#!/dynamic-dns')
    try:
        renew_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-labeled.btn-confirm"))
        )
        renew_button.click()
    finally:
        if close_on_exit:
            driver.close();
            driver.quit();

if __name__ == '__main__':
    import sys
    renew(sys.argv[1], sys.argv[2])
