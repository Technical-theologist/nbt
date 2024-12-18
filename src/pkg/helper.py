import string
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from constants import Constants
class Helper():
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_text(self, text):
        # Find all elements containing the specified text
        print(f"//*[contains(text(), '{text}')]")
        elements = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}')]")
        for element in elements:
            # Construct XPath for each element containing the text
            tag_name = element.tag_name
            xpath = f"//{tag_name}[contains(text(), '{text}')]"
            
            # Confirm by checking the element's actual text
            if element.text.strip() == text.strip():
                return element, xpath  # Return both the element and its XPath

        return None, None  # Return None if the text isn't found
    
    def hover(self, locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()
    
    def wait_for_element(self, locator):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def wait_for_all_elements(self, locators, timeout=5):
        for locator in locators:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Element {locator} not found"
            )
        print("All elements are present on the page.")

    def find_element_by_placeholder(self, placeholder_text):
        try:
            # Find the element by the placeholder attribute
            element = self.driver.find_element(By.XPATH, f"//*[@placeholder='{placeholder_text}']")
            # Construct the XPath based on the placeholder attribute
            xpath = f"//*[@placeholder='{placeholder_text}']"
            return element, xpath
        except Exception as e:
            return None, None
    
    def find_button_by_text(self, button_text):
        try:
            # Find the button by its visible text
            button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
            # Return the button and its XPath
            xpath = f"//button[text()='{button_text}']"
            return button, xpath
        except Exception as e:
            return None, None
    
    def checkSuccessfulLogin(self):
        if self.driver.current_url == Constants.homeUrl:
            return True
        else: return False
    
    def scrollToCenterWithElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    def find_dropdown_by_placeholder(self, placeholder_text):
        try:
            # Find the mat-select element by its placeholder
            mat_select = self.driver.find_element(By.XPATH, f"//mat-select[@placeholder='{placeholder_text}']")
            # Construct the XPath (for logging purposes)
            xpath = f"//mat-select[@placeholder='{placeholder_text}']"
            return mat_select, xpath
        except Exception as e:
            return None, None
    
    def insertDataIntoElement(self, element, data):
        element.send_keys(data)
    
    def generateTagStartNumber(self, length):
        if length < 1:
            return 0
        # Set the range for an n-digit number
        start = 10**(length-1)
        end = 10**length - 1
        return random.randint(start, end)
    
    def generateRandomString(self, length):
        # Choose from letters (uppercase & lowercase) and digits
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    def find_mat_select_by_label(self, label_text):
        try:
            # Find the mat-select element by the associated mat-label text
            mat_select = self.driver.find_element(By.XPATH, f"//mat-label[text()='{label_text}']/following-sibling::mat-select")
            xpath = f"//mat-label[text()='{label_text}']/following-sibling::mat-select"
            return mat_select, xpath
        except Exception as e:
            return None, None
        
    def findMatSelectWithName(self, name):
        try:
            element = self.driver.find_element(By.XPATH, f"//mat-select[@name='{name}']")
            xpath = f"//mat-select[@name='{name}']"
            return element, xpath
        except Exception as e:
            return None, None
    def findMatOption(self, value):
        try:
            element = self.driver.find_element(By.XPATH, f"//div[@role='listbox']//span[text()='{value}']")
            xpath = f"//div[@role='listbox']//span[text()='{value}']"
            return element, xpath
        except Exception as e:
            return None, None
    
    def findInputWithName(self, name):
        try:
            element = self.driver.find_element(By.XPATH, f"//input[@name='{name}']")
            xpath = f"//input[@name='{name}']"
            return element, xpath
        except Exception as e:
            return None, None

    def findAddressRadioButton(self):
        try:
            # Find the first mat-radio-button on the page
            radio_button = self.driver.find_element(By.XPATH, "(//mat-radio-button)[1]")
            xpath = "(//mat-radio-button)[1]"
            return radio_button, xpath
        except Exception as e:
            return None, None
    
    def chooseLayoutFindXpath(self, text):
        try:
            element = self.driver.find_element(By.XPATH, f"//h1[text()=' {text} ']")
            xpath = f"//h1[text()=' {text} ']"
            return element, xpath
        except Exception as e:
            return None, None
    
    def redirectToTag(self, index, length, pdf):
        if index <= length-1:
            self.driver.back()
            time.sleep(2)
        else:
            homeButtonElement, homeButtonXpath = self.find_element_by_text("Home")
            if homeButtonElement is None:
                pdf.insertTitleError("Home Button not found")
            homeButtonElement.click()
            time.sleep(5)
    
    def redirect(self, index, length, pdf):
        if index <= length-1:
            self.driver.refresh()
            time.sleep(2)
        else:
            homeButtonElement, homeButtonXpath = self.find_element_by_text("Home")
            if homeButtonElement is None:
                pdf.insertTitleError("Home Button not found")
            homeButtonElement.click()
            time.sleep(5)