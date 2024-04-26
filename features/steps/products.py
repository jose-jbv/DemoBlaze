from behave import *

from features.pages.ProductsPage import ProductsPage
from features.pages.SignupPage import SignupPage


@when(u'User search for a product {product}')
def step_impl(context, product):
    context.products_page = ProductsPage(context.driver)
    context.products_page.search_product(product)


@then(u'Product page is displayed {product}')
def step_impl(context, product):
    context.products_page.product_info(product)


@when(u'Product page is displayed {product}')
def step_impl(context, product):
    context.products_page.product_info(product)

@when(u'User add the product to the cart')
def step_impl(context):
    context.products_page.add_cart()


@when(u'Product is added to the cart')
def step_impl(context):
    message = "Product added"
    context.main_page.wait_for_alert()
    context.signup_page = SignupPage(context.driver)
    context.signup_page.validate_message(message)

@when(u'User review his cart')
def step_impl(context):
    context.driver.switch_to.alert.accept()
    context.main_page.click_on_option(context.main_page.nav_link_cart)

@then(u'Product {product} is visible in his cart')
def step_impl(context, product):
    context.products_page.review_cart(product)
