from behave import *


from features.pages.LoginPage import LoginPage
from features.pages.SignupPage import SignupPage



@when(u'I enter a registered user {user}')
def step_impl(context, user):
    login = context.main_page.nav_link_login
    context.main_page.click_on_option(login)
    context.login_page = LoginPage(context.driver)
    input_user = context.login_page.l_input_username
    context.main_page.wait_element_is_clickable(input_user)
    context.login_page.login_enter_username(user)



@when(u'Enter a valid password {pwd}')
def step_impl(context, pwd):
    context.login_page.login_enter_password(pwd)

@when(u'Click on the log in button')
def step_impl(context):
    context.login_page.click_on_button()


@then(u'User {user} is logged into the page')
def step_impl(context, user):
    context.login_page.validate_login(user)


@when(u'I enter invalid user {user}')
def step_impl(context, user):
    login = context.main_page.nav_link_login
    context.main_page.click_on_option(login)
    context.login_page = LoginPage(context.driver)
    input_user = context.login_page.l_input_username
    context.main_page.wait_element_is_clickable(input_user)
    context.login_page.login_enter_username(user)


@when(u'I enter a invalid password {pwd}')
def step_impl(context, pwd):
    context.login_page.login_enter_password(pwd)


@when(u'Click on the login button')
def step_impl(context):
    context.login_page.click_on_button()


@then(u'Error message is displayed')
def step_impl(context):
    error_message = "Wrong password."
    context.signup_page = SignupPage(context.driver)
    context.main_page.wait_for_alert()
    context.signup_page.validate_message(error_message)
