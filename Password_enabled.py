import os
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import desired_cap

class Password_enabledAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_cap.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def test_login(self):
        # Definindo um valor fixo para aguardar a localização do elemento.
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
        self.driver.find_element_by_xpath(
            "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]/android.view.View").click()

        visivel = self.driver.find_element_by_xpath("hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]/android.view.View").get_attribute('password')

        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Senha']").click()
        sleep(5)

        # Preenchimento da senha: qee123. Em suas respectivas posições no teclado.
        touch = TouchAction(self.driver)
        touch.tap(x=57, y=1235).perform()
        touch.tap(x=271, y=1239).perform()

        if visivel == 'false':
            assert True
        else:
            assert False



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Password_enabledAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)