from behave import *
from selenium.webdriver.common.by import By

import time


from features.pages.MainPage import MainPage
from features.pages.LoginPage import LoginPage
from features.pages.OrderPage import OrderPage


from features.steps.products import *

@when(u'User {user} place the order for {product}')
def step_impl(context, user, product):
    context.main_page = MainPage(context.driver)
    context.main_page.click_on_option(context.main_page.nav_link_login)
    context.login_page = LoginPage(context.driver)

    context.main_page.wait_element_is_clickable(context.login_page.l_input_username)
    context.login_page.login_enter_username(user)
    context.login_page.login_enter_password("test123")
    context.login_page.click_on_button()

    time.sleep(2)
    context.products_page = ProductsPage(context.driver)

    context.driver.find_element(By.XPATH, "//a[contains(text(), '" + product + "')]").click()

    time.sleep(2)

    context.products_page.add_cart()
    time.sleep(2)
    context.main_page.wait_for_alert()
    context.signup_page = SignupPage(context.driver)
    context.driver.switch_to.alert.accept()
    context.main_page.click_on_option(context.main_page.nav_link_cart)
    context.products_page.review_cart(product)
    time.sleep(2)
    context.order_page = OrderPage(context.driver)
    context.order_page.place_order()




@when(u'Complete the information with values {name} {country} {city} {ccard} {month} {year}')
def step_impl(context, name,country , city , ccard , month , year):
    context.order_page.wait_for_modal()
    context.order_page.complete_form(name,country , city , ccard , month , year)


@when(u'clicks on purchase button')
def step_impl(context):
    context.order_page.click_purchase()


@then(u'Message that purchase has been made is displayed')
def step_impl(context):
    context.order_page.validate_order_completed()
