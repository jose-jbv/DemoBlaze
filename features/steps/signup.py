from behave import *
from selenium import webdriver


from features.pages.MainPage import MainPage
from features.pages.SignupPage import SignupPage

@given(u'I Access to the Store')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.main_page = MainPage(context.driver)
    context.main_page.open_browser()




@when(u'I enter a non-existing username {user}')
def step_impl(context, user):
    signup_link = context.main_page.nav_link_signup
    context.main_page.click_on_option(signup_link)
    context.signup_page = SignupPage(context.driver)
    input_user = context.signup_page.s_input_username
    context.main_page.wait_element_is_clickable(input_user)
    context.signup_page.signup_enter_username(user)


@when(u'I enter a valid password {pwd}')
def step_impl(context, pwd):
    context.signup_page.signup_enter_password(pwd)


@when(u'Click on the Signup Button')
def step_impl(context):
    context.signup_page.click_on_signup()


@then(u'User should be created')
def step_impl(context):
    context.main_page.wait_for_alert()
    context.signup_page.validate_message("Sign up successful.")


@when(u'I enter an existing username {user}')
def step_impl(context, user):
    signup_link = context.main_page.nav_link_signup
    context.main_page.click_on_option(signup_link)
    context.signup_page = SignupPage(context.driver)
    input_user = context.signup_page.s_input_username
    context.main_page.wait_element_is_clickable(input_user)
    context.signup_page.signup_enter_username(user)


@when(u'I enter a password {pwd}')
def step_impl(context, pwd):
    context.signup_page.signup_enter_password(pwd)


@then(u'Error Message should be displayed.')
def step_impl(context):
    context.main_page.wait_for_alert()
    context.signup_page.validate_message("This user already exist.")
