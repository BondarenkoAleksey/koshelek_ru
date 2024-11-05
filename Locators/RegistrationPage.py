from selenium.webdriver.common.by import By


class RegistrationPageLocator:
    USERNAME = (By.CSS_SELECTOR, ".v-text-field__slot input")
    USERNAME_ERROR = (By.CSS_SELECTOR, '[data-pw="authorization-base-input-message"]')
    NEXT_BUTTON = (By.CSS_SELECTOR,'button[type="submit"]')
    EMAIL = (By.CSS_SELECTOR, '.v-input__control input#username')
    EMAIL_ERROR = (By.CSS_SELECTOR, '[data-wi="identificator"] [data-pw="authorization-base-input-message"]')
    PASSWORD = (By.CSS_SELECTOR, '.v-input__control input#new-password')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '[data-pw="auth-widget-password-input-message"]')
    REF_CODE = (By.CSS_SELECTOR, '[data-wi="referral"] input')
    REF_CODE_ERROR = (By.CSS_SELECTOR, '[data-wi="referral"] [data-pw="authorization-base-input-message"]')
