import logging

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_shadow_host(self, timeout=20):
        """Найти элемент-хост Shadow DOM
        :param timeout: время ожидания
        :return: найденный элемент-хост Shadow DOM или None, если элемент-хост не найден
        """
        try:
            shadow_host = WebDriverWait(self.driver, timeout).until(
                lambda x: x.execute_script("""
                    let shadowHost = null;
                    document.querySelectorAll('*').forEach(element => {
                        if (element.shadowRoot) {
                            shadowHost = element;
                        }
                    });
                    return shadowHost;
                """)
            )
            return shadow_host
        except TimeoutException:
            print("Shadow host не был найден в течение", timeout, "секунд")
            return None

    def find_element_in_shadow_dom(self, shadow_host, css_selector):
        """Найти элемент в Shadow DOM
        :param shadow_host: элемент-хост Shadow DOM
        :param css_selector: CSS-селектор для поиска элемента внутри Shadow DOM
        :return: найденный элемент или None, если элемент не найден
        """
        logging.info(f"Получение элемента в Shadow DOM")
        try:
            element = self.driver.execute_script("""
                return arguments[0].shadowRoot.querySelector(arguments[1]);
            """, shadow_host, css_selector)
            return element
        except Exception as e:
            print(f"Ошибка при поиске элемента в Shadow DOM: {e}")
            return None

    def type_text(self, text, element):
        """Ввести текст в поле ввода"""
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.key_down(Keys.COMMAND)
            actions.send_keys("a")
            actions.key_up(Keys.COMMAND)
            actions.send_keys(text)
            actions.perform()
        except Exception as e:
            print(f"Ошибка при вводе текста в поле ввода: {e}")
