from selenium.webdriver.common.by import By


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    s_input_username = "sign-username"
    s_input_password = "sign-password"
    s_button_signup = "//button[text()='Sign up']"


    def signup_enter_username(self, user):
        self.driver.find_element(By.ID, self.s_input_username).send_keys(user)

    def signup_enter_password(self, pwd):
        self.driver.find_element(By.ID, self.s_input_password).send_keys(pwd)

    def click_on_signup(self):
        self.driver.find_element(By.XPATH, self.s_button_signup).click()


    def validate_message(self, message):
        alert = self.driver.switch_to.alert.text
        assert alert.__eq__(message)
