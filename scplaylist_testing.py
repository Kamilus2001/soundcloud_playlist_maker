from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

location = 'D:/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(location)
driver.get('https://soundcloud.com/signin')
links = []
start_link = "https://soundcloud.com/misko2007/three-of-swords"
links.append(start_link)
check = 0
try:
    x = input("Napisz 'y' jesli sie zalogowales i stworzyles playliste juz: ")
    if x == "y":
        driver.get("https://soundcloud.com/misko2007/three-of-swords")
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='announcement__ack sc-button sc-button-medium']"))).click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='sc-button-more sc-button sc-button-medium sc-button-responsive']"))).click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='sc-button-addtoset moreActions__button sc-button-medium']"))).click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='textfield__input sc-input sc-input-medium']")))
        element.send_keys('test')
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
             "//button[@class='addToPlaylistButton sc-button sc-button-medium sc-button-responsive']"))).click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
             "//button[@class='modal__closeButton']"))).click()
        elem2 = driver.find_elements_by_xpath("//a[@class='soundTitle__title sc-link-dark']")
        links.append(elem2[1].get_attribute("href"))
        next = elem2[1].get_attribute("href")
        while True:
            try:
                    driver.get(next)
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//button[@class='sc-button-more sc-button sc-button-medium sc-button-responsive']"))).click()
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//button[@class='sc-button-addtoset moreActions__button sc-button-medium']"))).click()
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//input[@class='textfield__input sc-input sc-input-medium']")))
                    element.send_keys('test')
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH,
                         "//button[@class='addToPlaylistButton sc-button sc-button-medium sc-button-responsive']"))).click()
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH,
                         "//button[@class='modal__closeButton']"))).click()
                    elem2 = driver.find_elements_by_xpath("//a[@class='soundTitle__title sc-link-dark']")
                    check = 0
                    while check == 0:
                        check = 1
                        next = elem2[randint(0, 2)].get_attribute("href")
                        for i in range(0, len(links)):
                            if next == links[i]:
                                check = 0
                    links.append(next)
            except Exception:
                pass
except Exception as e:
    pass
#while True:
    #try:
        #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='soundTitle__title sc-link-dark']"))).get_attribute("href")
        #elem2 = driver.find_elements_by_xpath("//a[@class='soundTitle__title sc-link-dark']")
        #for e in elem2:
         #   print(e.get_attribute("href"))
    #except Exception as e:
    #        pass