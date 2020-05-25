import os
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import desired_cap

class LoginRecoverAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_cap.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def test_login(self):
        # Definindo um valor fixo para aguardar a localização do elemento
        self.driver.implicitly_wait(40)

        for i in range(3):
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        for i in range(3):
            sleep(8)
            self.driver.find_element_by_class_name("android.widget.Button").click()

        self.driver.implicitly_wait(40)

        self.driver.find_element_by_xpath("//android.view.View[@text='Já tenho conta']").click()
        sleep(5)

        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Seu e-mail']").click()
        sleep(5)
        # A função SEND_KEYS foi substituida por  touch, pois, apresentava problema na hora de atualizar o valor do EditText.

        # Preenchimento do email:testedasilva1@grr.la.Em suas respectivas posições no teclado!
        touch = TouchAction(self.driver)
        touch.tap(x=475, y=1240).perform()
        touch.tap(x=283, y=1253).perform()
        touch.tap(x=212, y=1398).perform()
        touch.tap(x=480, y=1251).perform()
        touch.tap(x=266, y=1248).perform()

        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Senha']").click()
        sleep(5)
        # Preenchimento da senha: qee123. Em suas respectivas posições no teclado.
        touch.tap(x=57, y=1235).perform()
        touch.tap(x=271, y=1239).perform()
        touch.tap(x=273, y=1237).perform()
        touch.tap(x=57, y=1112).perform()
        touch.tap(x=166, y=1100).perform()
        touch.tap(x=271, y=1107).perform()

        # Acessar o app.
        # Na terceira tentativa de acesso com dados invalidos é esperado que o sistema exiba a opção de recuperar senha.
        for i in range(3):
            sleep(3)
            self.driver.find_element_by_class_name("android.widget.Button").click()

        result = self.driver.find_element_by_class_name("android.widget.Button").get_attribute('displayed')

        # Verifica se a opção de recuperar senha foi exibida.
        if result == 'true':
            assert True
        else:
            assert False

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginRecoverAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)