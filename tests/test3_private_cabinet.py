from locators import Locators
from urls import Urls

class TestPrivateCabinet:
    def test_into_private_cabinet(self, driver):
        """Переход авторизованного пользователя в личный кабинет по кнопке "Личный кабинет" на главной"""
        driver.get(Urls.LOGIN)
        driver.find_element(*Locators.LOGIN).send_keys("vladislav_klimenko_12@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("3882723qQ")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(5)
        driver.find_element(*Locators.PRIVATE_CAB_BUTTON).click()
        assert driver.find_element(*Locators.LOGOUT_BUTTON)

    def test_into_constructor_from_cabinet(self, driver):
        """Переход из личного кабинета в раздел "Конструктор" на главной"""
        driver.get(Urls.LOGIN)
        driver.find_element(*Locators.LOGIN).send_keys("vladislav_klimenko_12@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("3882723qQ")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(5)
        driver.find_element(*Locators.PRIVATE_CAB_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*Locators.PUSH_ORDER_BUTTON)

    def test_into_logo_from_cabinet(self, driver):
        """Переход из личного кабинета на главную через кнопку с логотипом"""
        driver.get(Urls.LOGIN)
        driver.find_element(*Locators.LOGIN).send_keys("vladislav_klimenko_12@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("3882723qQ")
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.implicitly_wait(5)
        driver.find_element(*Locators.PRIVATE_CAB_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        assert driver.find_element(*Locators.PUSH_ORDER_BUTTON)

        def test_logout(self, driver):
            """Выход из личного кабинета"""
            driver.get(Urls.LOGIN)
            driver.find_element(*Locators.LOGIN).send_keys("vladislav_klimenko_12@yandex.ru")
            driver.find_element(*Locators.PASSWORD).send_keys("3882723qQ")
            driver.find_element(*Locators.ENTER_BUTTON).click()
            driver.implicitly_wait(5)
            driver.find_element(*Locators.PRIVATE_CAB_BUTTON).click()
            driver.find_element(*Locators.LOGOUT_BUTTON).click()
            assert driver.find_element(*Locators.FIELD_ENTER).text == 'Вход'