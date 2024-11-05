import time

import allure

from .BasePage import BasePage
from Locators.RegistrationPage import RegistrationPageLocator


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получить элемент поля ввода \"Имя пользователя\"")
    def get_username_input_field(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.USERNAME[1])
        return element

    @allure.step("Ввести текст в поле \"Имя пользователя\"")
    def type_text_to_username(self, text):
        self.type_text(text=text, element=self.get_username_input_field())

    @allure.step("Получить элемент ошибки валидации имени пользователя")
    def get_username_input_error(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.USERNAME_ERROR[1])
        if element:
            return element
        return None

    @allure.step("Получить элемент поля ввода \"Электронная почта\"")
    def get_email_input_field(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.EMAIL[1])
        return element

    @allure.step("Ввести текст в поле \"Электронная почта\"")
    def type_text_to_email(self, text):
        self.type_text(text=text, element=self.get_email_input_field())

    @allure.step("Получить элемент ошибки валидации email")
    def get_email_input_error(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.EMAIL_ERROR[1])
        if element:
            return element
        return None

    @allure.step("Получить элемент поля ввода \"Пароль\"")
    def get_password_input_field(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.PASSWORD[1])
        return element

    @allure.step("Ввести текст в поле \"Пароль\"")
    def type_password(self, text):
        self.type_text(text=text, element=self.get_password_input_field())

    @allure.step("Получить элемент ошибки валидации пароля")
    def get_password_input_error(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.PASSWORD_ERROR[1])
        if element:
            return element
        return None

    @allure.step("Получить элемент поля ввода \"Реферальный код\"")
    def get_ref_code_input_field(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.REF_CODE[1])
        return element

    @allure.step("Ввести текст в поле \"Реферальный код\"")
    def type_ref_code(self, text):
        self.type_text(text=text, element=self.get_ref_code_input_field())

    @allure.step("Получить элемент ошибки валидации реф. кода")
    def get_ref_code_input_error(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.REF_CODE_ERROR[1])
        if element:
            return element
        return None

    @allure.step("Получить элемент кнопку 'Далее'")
    def get_next_button(self):
        element = self.find_element_in_shadow_dom(shadow_host=self.find_shadow_host(),
                                                  css_selector=RegistrationPageLocator.NEXT_BUTTON[1])
        return element

    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_next_button(self):
        element = self.get_next_button()
        element.click()
        time.sleep(1)

    @allure.step("Проверить текст ошибки")
    def validate_error_text(self, error_text, field):
        if field == "username":
            text_error = self.get_username_input_error().text
        if field == "email":
            text_error = self.get_email_input_error().text
        if field == "password":
            text_error = self.get_password_input_error().text
        if field == "ref_code":
            text_error = self.get_ref_code_input_error().text
            print(text_error)
        if not text_error:
            assert False, "Ошибка валидации отсутствует"
        assert f"{error_text}" in text_error, f"""
        Ожидаемый текст ошибки - {error_text}
        Фактический текст ошибки - {text_error}"""
