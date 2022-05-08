from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def main():
    email = "automatest79@gmail.com"
    password = "#automationTest79"
    driver.get("https:\\www.gmail.com")

    login(email , password)

    send_mail("goyalharshit79@gmail.com" , "Email Automation Test" , "Test successfull")

    driver.close()

def login(email , password):
    #enter email
    driver.find_element(by = By.XPATH , value = '//*[@id="identifierId"]').send_keys(email)
    driver.find_element(by = By.XPATH , value = '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(2)
    #enter password and login
    driver.find_element(by = By.XPATH , value = '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(by = By.XPATH , value = '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(15)
    #compose
    compose_btn = driver.find_element(by = By.XPATH , value = '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
    compose_btn.click()
    time.sleep(5)

def send_mail(rec,subject,body):
    #to field
    to_field = driver.find_element(by = By.CLASS_NAME , value = "agP.aFw")
    to_field.send_keys(rec)
    
    #subject field
    sub_field = driver.find_element(by = By.NAME , value = "subjectbox")
    sub_field.send_keys(subject)
    
    #body field
    body_field =driver.find_element(by = By.CSS_SELECTOR , value = ".Am.Al.editable.LW-avf.tS-tW")
    body_field.send_keys(body)

    #send button
    send_btn = driver.find_element(by = By.CLASS_NAME , value = "T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")
    send_btn.click()

    time.sleep(5)

if __name__ == "__main__":
    main()
