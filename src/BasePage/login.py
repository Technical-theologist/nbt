from src.pkg.helper import Helper
from selenium.webdriver.common.by import By
import time
from constants import Constants

class Login():
    def __init__(self, driver, pdf):
        self.driver = driver
        self.pdf = pdf
        self.helper = Helper(self.driver)
    
    def login(self):
        try:
            myAccountElement, xpath = self.helper.find_element_by_text( "My Account")
            if myAccountElement is None:
                self.pdf.insertErrorMessage("My Account Element not found")
                raise Exception("My Account element not found")
            self.helper.hover((By.XPATH,xpath))
            loginElement, loginXPATH = self.helper.find_element_by_text( "Login")
            if loginElement is None:
                self.pdf.insertErrorMessage("Login Element not found")
                raise Exception("Login Element not found")
            self.helper.click((By.XPATH, loginXPATH))
            time.sleep(2)
            emailFieldElement, emailFieldXpath = self.helper.find_element_by_placeholder("Email")
            if emailFieldElement is None:
                self.pdf.insertErrorMessage("Email Field Element not found")
                raise Exception("Email Field element not found")
            self.helper.click((By.XPATH, emailFieldXpath))
            time.sleep(0.5)
            assert emailFieldElement is not None, "Field not found"
            emailFieldElement.send_keys(Constants.loginEmail)

            passwordFieldElement, passwordFieldXpath = self.helper.find_element_by_placeholder("Enter your password")
            if passwordFieldElement is None:
                self.pdf.insertErrorMessage("Password Field Element not found")
                raise Exception("Password Field Element not found")
            self.helper.click((By.XPATH, passwordFieldXpath))
            time.sleep(0.5)
            assert passwordFieldElement is not None, "Field not found"
            passwordFieldElement.send_keys(Constants.loginPassword)
            loginButtonElemenet, loginButtonXpath = self.helper.find_button_by_text("Login")
            if loginButtonElemenet is None:
                self.pdf.insertErrorMessage("Login Button Element not found")
                raise Exception("Login Button Element not found")
            self.helper.click((By.XPATH, loginButtonXpath))
            time.sleep(2)
            result = self.helper.checkSuccessfulLogin()
            return result
        except Exception as e:
            print(e)
