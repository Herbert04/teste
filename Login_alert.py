import os
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class LoginAlertAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            "deviceName": "Nexus 5X API 28",
            "platformName": "Android",
            "platformVersion": "9.0",
            "app": "C:\\Users\\herbe\\Downloads\\app-release.apk",
            "appPackage": "br.com.simplificauto.napista",
            "appWaitActivity": "br.com.simplificauto.napista.MainActivity",
            "newCommandTimeout": "3600"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)



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

        # Acessar o app.
        self.driver.find_element_by_class_name("android.widget.Button").click()

        # Armazenar o retorno da mensagem
        result = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View").text

        # Removendo a palavra 'Informativo' do alert.
        result = result.split('Informativo', 1)
        # A mensagem é acompanhada quebra de linha, com o replace essa quebra é removida
        menssagem = result[1].replace('\n', '')

        # self.assertEqual('Preencha os campos', menssagem)
        if 'Preencha os campos' == menssagem:
            assert True
        else:
            assert False


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAlertAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)