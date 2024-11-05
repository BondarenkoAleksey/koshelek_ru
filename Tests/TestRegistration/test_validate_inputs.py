import allure
import time

from Pages.RegistrationPage import RegistrationPage
from TestData.TestData import URL

# TODO: "рефакторить - добавить pytest parametrized, разбить на более мелкие"


@allure.epic("UI тесты")
@allure.feature("Регистрация")
@allure.story("Проверка полей ввода")
def test_check_registration_form(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open(URL)
    time.sleep(10)
    assert driver.title == 'Кошелёк.ру - криптовалютная экосистема в кошельке', \
        "Некорректный заголовок или не та страница"

    # Проверка поля "Имя пользователя"
    registration_page.type_text_to_username(text='')
    registration_page.click_next_button()
    registration_page.validate_error_text(error_text="Поле не заполнено", field="username")

    registration_page.type_text_to_username(text='Привет')
    registration_page.validate_error_text(error_text="Введены недопустимые символы: ", field="username")

    registration_page.type_text_to_username(text='1Привет')
    registration_page.validate_error_text(error_text="Введены недопустимые символы: ", field="username")

    # FIXME: проверить требования к полю Имя пользователя. Падает!
    # registration_page.type_text_to_username(text='1SuperUser')
    # registration_page.click_username_next_button()
    # registration_page.validate_error_text_username(
    #     error_text="Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", field="username")

    registration_page.type_text_to_username(text='1ван')
    registration_page.click_next_button()
    # FIXME: проверить требования к полю Имя пользователя. После нажатия показывается другой текст ошибки!
    #  После - при необходимости, скорректировать ожидаемый текст ошибки
    registration_page.validate_error_text(
        error_text="Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", field="username")

    registration_page.type_text_to_username(text='Zzz123456789012345678901234567890')
    registration_page.validate_error_text(error_text="Превышен лимит символов: 32 максимум", field="username")

    registration_page.type_text_to_username(text='1ABCDEFGH')
    registration_page.click_next_button()
    registration_page.validate_error_text(
        error_text="Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", field="username")

    registration_page.type_text_to_username(text='qwerty123')
    registration_page.type_text_to_email(text='')
    time.sleep(1)
    registration_page.validate_error_text(error_text="Имя пользователя уже занято", field="username")
    time.sleep(1)
    registration_page.validate_error_text(error_text="Поле не заполнено", field="email")

    # Проверка поля "Email"
    registration_page.type_text_to_username(text='Super_User_123_45')
    registration_page.type_text_to_email(text="@")
    registration_page.click_next_button()
    registration_page.validate_error_text(error_text="Формат e-mail: username@test.ru", field="email")

    registration_page.type_text_to_email(text="username.test.ru")
    registration_page.click_next_button()
    registration_page.validate_error_text(error_text="Формат e-mail: username@test.ru", field="email")

    registration_page.type_text_to_email(text="@test.ru")
    registration_page.click_next_button()
    registration_page.validate_error_text(error_text="Формат e-mail: username@test.ru", field="email")

    registration_page.type_text_to_email(text="test@test.ru_")
    registration_page.click_next_button()
    registration_page.validate_error_text(error_text="Формат e-mail: username@test.ru", field="email")

    registration_page.type_text_to_email(text="test@te@st.ru")
    registration_page.click_next_button()
    registration_page.validate_error_text(error_text="Формат e-mail: username@test.ru", field="email")

    # TODO: "Уточнить ограничение по максимальным символам в поле email (должно быть) и создать проверку"

    # Проверка поля "Пароль"

    registration_page.click_next_button()
    registration_page.type_password(text='')
    registration_page.type_text_to_email(text="test@test.ru")
    registration_page.validate_error_text(error_text="Поле не заполнено", field="password")

    registration_page.type_password(text='1234')
    registration_page.type_text_to_email(text="test@test.ru")
    registration_page.validate_error_text(error_text="Пароль должен содержать минимум 8 символов", field="password")

    registration_page.type_password(text='12345678')
    registration_page.type_text_to_email(text="test_1@test.ru")
    registration_page.validate_error_text(
        error_text="Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры", field="password")

    registration_page.type_password(text='PASSWORD')
    registration_page.type_text_to_email(text="test_12@test.ru")
    registration_page.validate_error_text(
        error_text="Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры", field="password")

    registration_page.type_password(text='password1')
    registration_page.type_text_to_email(text="test_123@test.ru")
    registration_page.validate_error_text(
        error_text="Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры", field="password")

    registration_page.type_password(text='Passwordpasswordpasswordpasswordpasswordpasswordpasswordpasswor65')
    registration_page.validate_error_text(
        error_text="Превышен лимит символов: 64 максимум", field="password")

    # TODO: "Уточнить ограничение по вводу символов в пароле
    #  (символы вводятся, по тексту ошибки вводятся только заглавные буквы и цифры"

    registration_page.type_password(text='Passw123456')
    registration_page.type_ref_code(text='1')
    registration_page.validate_error_text(
        error_text="Неверный формат ссылки", field="ref_code")

    registration_page.type_ref_code(text='12')
    registration_page.validate_error_text(
        error_text="Неверный формат ссылки", field="ref_code")

    registration_page.type_ref_code(text='123')
    registration_page.validate_error_text(
        error_text="Неверный формат ссылки", field="ref_code")
