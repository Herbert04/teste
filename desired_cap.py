import os

def get_desired_capabilities():
    desired_cap = {
        "deviceName": "Nexus 5X API 28",
        "platformName": "Android",
        "platformVersion": "9.0",
        "app": "C:\\Users\\herbe\\Downloads\\app-release.apk",
        "appPackage": "br.com.simplificauto.napista",
        "appWaitActivity": "br.com.simplificauto.napista.MainActivity",
        "newCommandTimeout": "3600"
    }
    return desired_cap