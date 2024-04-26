from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    pp_add_cart = "//a[contains(text(), 'Add to cart')]"

    def search_product(self, product):
        search_product = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '" + product + "')]")))
        search_product.click()

    def product_info(self, product):
        product_info = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='tbodyid']//h2[text()='" + product + "']")))
        assert product_info.text.__eq__(product)


    def add_cart(self):
        self.driver.find_element(By.XPATH, self.pp_add_cart).click()


    def review_cart(self, product):
        search_product = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), '" + product + "')]")))
        assert search_product.text.__eq__(product)

