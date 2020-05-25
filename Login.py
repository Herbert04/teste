import os
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import desired_cap

class LoginAndroidTests(unittest.TestCase):

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

        # Preenchimento do email:testedasilva1@grr.la. Em suas respectivas posições no teclado!
        touch = TouchAction(self.driver)
        touch.tap(x=475, y=1240).perform()
        touch.tap(x=283, y=1253).perform()
        touch.tap(x=212, y=1398).perform()
        touch.tap(x=480, y=1251).perform()
        touch.tap(x=266, y=1248).perform()
        touch.tap(x=311, y=1378).perform()
        touch.tap(x=104, y=1396).perform()
        touch.tap(x=212, y=1391).perform()
        touch.tap(x=812, y=1242).perform()
        touch.tap(x=969, y=1386).perform()
        touch.tap(x=546, y=1553).perform()
        touch.tap(x=116, y=1391).perform()
        touch.press(x=73, y=1247).move_to(x=63, y=1239).release().perform()
        touch.tap(x=218, y=1710).perform()
        touch.tap(x=534, y=1399).perform()
        touch.tap(x=379, y=1252).perform()
        touch.tap(x=372, y=1242).perform()
        touch.tap(x=862, y=1715).perform()
        touch.tap(x=964, y=1381).perform()
        touch.tap(x=111, y=1399).perform()

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
        self.driver.find_element_by_class_name("android.widget.Button").click()
        sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)