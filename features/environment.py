import allure
from allure_commons.types import AttachmentType


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="screen"
                      ,attachment_type=AttachmentType.PNG)