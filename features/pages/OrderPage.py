import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    op_placeorder_button = "//button[contains(text(), 'Place Order')]"
    op_placeorder_name = "//input[@id='name']"
    op_placeorder_country = "//input[@id='country']"
    op_placeorder_city = "//input[@id='city']"
    op_placeorder_card = "//input[@id='card']"
    op_placeorder_month = "//input[@id='month']"
    op_placeorder_year = "//input[@id='year']"
    op_placeorder_purchase = "//button[contains(text(), 'Purchase')]"
    op_placeorder_completed = "//h2[contains(text(), 'Thank you for your purchase!')]"


    def place_order(self):
        self.driver.find_element(By.XPATH, self.op_placeorder_button).click()


    def wait_for_modal(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "orderModalLabel")))


    def complete_form(self, user,country,city,card,month,year):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.op_placeorder_name)))
        self.driver.find_element(By.XPATH, self.op_placeorder_name).send_keys(user)
        self.driver.find_element(By.XPATH, self.op_placeorder_country).send_keys(country)
        self.driver.find_element(By.XPATH, self.op_placeorder_city).send_keys(city)
        self.driver.find_element(By.XPATH, self.op_placeorder_card).send_keys(card)
        self.driver.find_element(By.XPATH, self.op_placeorder_month).send_keys(month)
        self.driver.find_element(By.XPATH, self.op_placeorder_year).send_keys(year)


    def click_purchase(self):
        self.driver.find_element(By.XPATH, self.op_placeorder_purchase).click()


    def validate_order_completed(self):
        message = "Thank you for your purchase!"
        order_complete = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.op_placeorder_completed)))
        assert order_complete.text.__eq__(message)



