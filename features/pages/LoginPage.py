from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    l_input_username = 'loginusername'
    l_input_password = 'loginpassword'
    l_login_button = "//button[text()='Log in']"
    l_welcome = 'nameofuser'

    def login_enter_username(self, user):
        self.driver.find_element(By.ID, self.l_input_username).send_keys(user)


    def login_enter_password(self, pwd):
        password_input = self.driver.find_element(By.ID, self.l_input_password)
        password_input.send_keys(pwd)


    def click_on_button(self):
        self.driver.find_element(By.XPATH, self.l_login_button).click()
        login_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.l_login_button))
        )
        login_button.click()


    def validate_login(self, user):
        welcome = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.l_welcome)))
        assert welcome.text.__eq__("Welcome " + user)