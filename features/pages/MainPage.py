from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    nav_link_signup = "signin2"
    nav_link_login = "login2"
    nav_link_cart = "cartur"

    def open_browser(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def click_on_option(self, option):
        self.driver.find_element(By.ID, option).click()


    def wait_element_is_clickable(self, element):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.ID, element)))


    def wait_for_alert(self):
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
