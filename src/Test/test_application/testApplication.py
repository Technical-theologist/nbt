import time
from selenium.webdriver.common.by import By
from src.Test.BaseTest import BaseTest
from src.BasePage.login import Login
from src.pkg.pdf import GeneratePdf
from datetime import datetime
from constants import Constants
from src.pkg.helper import Helper
from src.Test.test_application.testProduct import testProduct
from src.pkg.requests import fetchProducts, fetchTagModelsWithProductId

class Test_Application(BaseTest):
    
    def test_initialization(self):
        helper = Helper(self.driver)
        time.sleep(2)
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format as YYYY-MM-DD_HH-MM-SS
        filename = f"report_{current_time}.pdf" 
        pdf = GeneratePdf(filename)
        try:
            print("Login")
            login = Login(self.driver, pdf)
            loginResult = login.login()
            pdf.insertLoginTest(Constants.loginEmail, Constants.loginPassword, loginResult)
            assert loginResult, "Login Failed"
            if not loginResult:
                raise Exception("Login Failed")
            time.sleep(2)
            pdf.drawLine()
            successData, errCode = fetchProducts()
            if errCode != 200:
                pdf.insertTitleError("500 Internal Error")
                raise Exception("500 Internal Error")
            for i in range(len(successData)):
                productData = successData[i]
                productId = productData.get("productId")
                productName = productData.get("productName")
                if (productName == "Style 147" or productName == "Style 153" or productName == "Style 198" or
                    productName == "Style 228" or productName=="Style 227" or productName=="Style 226" or
                     productName=="Style 71" or productName=="Style 60" or productName=="Style 90"):
                    continue
                print(productName)
                pdf.insert_product_name(productName)
                productTitleElement, productTitleXpath = helper.find_element_by_text(productName)
                if productTitleElement is None:
                    pdf.insertTitleError(productName=": Tag Not Found")
                    pdf.drawLine()
                    print("in product not found")
                    continue
                else:
                    print(productTitleXpath)
                    print("product Found")
                tagsData, errorCode = fetchTagModelsWithProductId(productId=productId)
                print(productId)
                helper.scrollToCenterWithElement(productTitleElement)
                helper.click((By.XPATH, productTitleXpath))
                time.sleep(2)

                pdf.drawLine()
                testProduct(productData, tagsData, self.driver, pdf)
        except Exception  as e:
            print(e)
        finally:
            print("in finally")
            pdf.save()