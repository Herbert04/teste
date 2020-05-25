import os
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
  "deviceName": "Nexus 5X API 28",
  "platformName": "Android",
  "app": "C:\\Users\\herbe\\Downloads\\app-release.apk",
  "appPackage": "br.com.simplificauto.napista",
  "appWaitActivity": "br.com.simplificauto.napista.MainActivity",
  "newCommandTimeout": "3600"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)

driver.implicitly_wait(40)
valor = driver.find_element_by_id('com.android.packageinstaller:id/current_page_text').get_attribute('text')
#while(driver.find_element_by_id('com.android.packageinstaller:id/dialog_container').get_attribute('enabled')):
#COLOCAR UM LAÇO DE REPETIÇÃO
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

#driver.implicitly_wait(40)
driver.find_element_by_xpath("//android.widget.Button[@text='Próximo']").click()
sleep(5)
#driver.implicitly_wait(40)
driver.find_element_by_xpath("//android.widget.Button[@text='Próximo']").click()
sleep(5)
#driver.implicitly_wait(40)
driver.find_element_by_xpath("//android.widget.Button[@text='Vamos começar']").click()

driver.implicitly_wait(40)
driver.find_element_by_xpath("//android.view.View[@text='Já tenho conta']").click()
sleep(5)
driver.find_element_by_xpath("//android.widget.EditText[@text='Seu e-mail']").click()
sleep(5)
        # Preenchimento do email:teste. Em suas respectivas posições no teclado!
touch = TouchAction(driver)
touch.tap(x=475, y=1240).perform()
touch.tap(x=212, y=1398).perform()
touch.tap(x=480, y=1251).perform()
driver.find_element_by_xpath("//android.widget.EditText[@text='Senha']").click()
sleep(5)
        # Preenchimento da senha: qee123. Em suas respectivas posições no teclado.
touch.tap(x=57, y=1235).perform()
touch.tap(x=271, y=1239).perform()
touch.tap(x=273, y=1237).perform()

for i in range(3):
    driver.find_element_by_class_name("android.widget.Button").click()
    sleep(3)

print(driver.find_element_by_xpath("//android.widget.Button[@text='Recuperar minha senha']").get_attribute('displayed'))
