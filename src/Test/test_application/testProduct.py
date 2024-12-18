import time
from selenium.webdriver.common.by import By
from src.Test.BaseTest import BaseTest
from src.BasePage.login import Login
from src.pkg.pdf import GeneratePdf
from datetime import datetime
from constants import Constants
from src.pkg.helper import Helper
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testProduct(productData, productTags, driver, pdf):
    time.sleep(2)
    helper = Helper(driver)
    print(1)
    productName = productData.get("productName")
    print(2)
    years = productData.get("years")
    print(3)
    isYear = productData.get("isYear")
    print(4)
    isVacc = productData.get("isVacc")
    print(5)
    vaccine_string = productData.get("vaccinestring")
    isTagStart = productData.get("isTagStart")
    for i in range(len(productTags)):
        time.sleep(2)
        tag = []
        tag = productTags[i]
        tagLines = tag.get("lines")
        tag_name=tag.get("TagModel")
        pdf.insert_Tag_name(tag_name)
        if isYear == 1:
            print("In year")
            yearElement, yearXpath = helper.findMatSelectWithName("year")
            if yearElement is None:
                pdf.insertTitleError("Year Field Not Found.")
                helper.redirect(i, len(productTags), pdf)
                continue
            helper.scrollToCenterWithElement(yearElement)
            yearElement.click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//mat-option"))
            )
            
            if tag.get("isYear") == 1:
                optionElement, optionXpath = helper.findMatOption(" "+years[0]+" ")
                if optionElement is None:
                    pdf.insertTitleError("Year Field Option: "+years[0]+" not found")
                    helper.redirect(i, len(productTags), pdf)
                    continue
                helper.click((By.XPATH, optionXpath))
                time.sleep(1)
                print(6)
                pdf.insert_year(years[0])
                print(7)
            else:
                optionElement, optionXpath = helper.findMatOption("No year")
                if optionElement is None:
                    pdf.insertTitleError("Year Field Option: No Year not found")
                    helper.redirect(i, len(productTags), pdf)
                    continue
                helper.click((By.XPATH, optionXpath))
                print(8)
                pdf.insert_year("No year")
                print(9)
        time.sleep(2)
        if isVacc == 1:
            print("in header")
            vaccElement, vaccXpath = helper.findMatSelectWithName("vaccine")
            if vaccElement is None:
                    pdf.insertTitleError("Header Field not found")
                    helper.redirect(i, len(productTags), pdf)
                    continue
            helper.scrollToCenterWithElement(vaccElement)
            vaccElement.click()
            if tag.get("isVacc") == 1:
                optionElement, optionXpath = helper.findMatOption(" "+vaccine_string[0]+" ")
                if optionElement is None:
                    pdf.insertTitleError("Header Field Option: "+vaccine_string[0]+" not found")
                    helper.redirect(i, len(productTags), pdf)
                    continue
                helper.click((By.XPATH, optionXpath))
                print(10)
                pdf.insert_vaccine(vaccine_string[0])
                print(11)
            else:
                optionElement, optionXpath = helper.findMatOption("No Header")
                if optionElement is None:
                    helper.redirect(i, len(productTags), pdf)
                    pdf.insertTitleError("Header Field Option: No Header not found")
                    continue
                helper.click((By.XPATH, optionXpath))
                print(12)
                pdf.insert_vaccine("No Header")
                print(13)
        time.sleep(2)
        if isTagStart == 1:
            tagStartElement, tagStartXpath = helper.findInputWithName("tagstartnumber")
            if tagStartElement is None:
                    pdf.insertTitleError("Tag Start number field not found")
                    helper.redirect(i, len(productTags), pdf)
                    continue
            helper.scrollToCenterWithElement(tagStartElement)
            if tag.get("isTagStartNo") == 1:
                tag_start_no= helper.generateTagStartNumber(int(tag.get("tagstagnumberlength")))
                helper.insertDataIntoElement(tagStartElement,tag_start_no)
                pdf.insertTagStartNumber(tag_start_no)
                print(14)
        time.sleep(2)

        for lineIndex in range(len(tagLines)):
            if tagLines[lineIndex].get("linecharcount") > 0:
                lineElement, lineXpath = None, None
                lineElement, lineXpath = helper.findInputWithName("text"+str(lineIndex+1))
                if lineElement is None:
                    helper.redirect(i, len(productTags), pdf)
                    pdf.insertTitleError("Line "+str(lineIndex+1) + " not found")
                    continue
                helper.scrollToCenterWithElement(lineElement)
                line_string=helper.generateRandomString(tagLines[lineIndex].get("linecharcount"))
                helper.insertDataIntoElement(lineElement,line_string)
                pdf.insertLine("line "+str(lineIndex+1)+" Characters: "+line_string)
                print(15)
                time.sleep(1)
                
        print("in 1")
        reviewButtonElement, reviewButtonXpath = helper.find_element_by_text("Review")
        if reviewButtonElement is None:
            pdf.insertTitleError("Review Button in Product Demo is not found")
            helper.redirect(i, len(productTags), pdf)
            continue
        print("in 2")
        helper.scrollToCenterWithElement(reviewButtonElement)
        print("in 3")
        time.sleep(2)
        reviewButtonElement.click()
        print("in 4")
        tagModel = tag.get("TagModel")
        print(type(tagModel))
        time.sleep(3)
        layoutTextElement, layoutTextXpath = helper.chooseLayoutFindXpath(tagModel)
        print("Layout Element: ", layoutTextElement)
        if layoutTextElement is None:
            pdf.insertTitleError("Layout Not Found")
            helper.redirect(i, len(productTags), pdf)
            continue
        print(len(tagModel))
        # print()
        print("layout: ", layoutTextXpath)
        time.sleep(5)
        layoutTextElement.click()
        continueElement, continueXpath = helper.find_element_by_text("Continue")
        if continueElement is None:
            pdf.insertTitleError("In Layout Screen Continue Button not found")
            helper.redirect(i, len(productTags), pdf)
            continue
        continueElement.click()
        time.sleep(4)
        addressRadio, addressXpath = helper.findAddressRadioButton()
        if addressRadio is None:
            pdf.insertTitleError("In Place order screen radio button for address not found")
            helper.redirectToTag(i, len(productTags), pdf)
            continue
        time.sleep(2)
        addressRadio.click()
        time.sleep(1)
        placeOrderButtonElement, placeOrderXpath = helper.find_element_by_text("Place Order")
        if placeOrderButtonElement is None:
            pdf.insertTitleError("In place order screen place order button not found.")
            helper.redirect(i, len(productTags), pdf)
            continue
        placeOrderButtonElement.click()
        time.sleep(5)
        homeButtonElement, homeButtonXpath = helper.find_element_by_text("Home")
        if homeButtonElement is None:
            pdf.insertTitleError("Home Button not found")
            helper.redirect(i, len(productTags), pdf)
            continue
        homeButtonElement.click()
        time.sleep(5)
        time.sleep(3)
        pdf.drawLine()
        if len(productTags) - 1 != i:
            productTitleElement, productTitleXpath = helper.find_element_by_text(productName)
            if productTitleElement is None:
                print("Product Title isn't in the list")
                pdf.insertTitleError("Product not found")
                continue
            # productTitleElement.click()
            helper.scrollToCenterWithElement(productTitleElement)
            helper.click((By.XPATH, productTitleXpath))
            time.sleep(2)