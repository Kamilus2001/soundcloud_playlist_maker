from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

class Playlist(object):
    def __init__(self, driverlocation, start_track, playlist):
        self.drv_loc = driverlocation
        self.st_trk = start_track
        self.playl = playlist
        self.links = []
        self.links.append(self.st_trk)
        self.driver = webdriver.Chrome(self.drv_loc)
        self.driver.get('https://soundcloud.com/signin')
    def start(self):
        try:
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                        "//button[@class='signinInitialStep_fbButton signinForm__cta sc-button sc-button-large sc-button-facebook']"))).click()
        except Exception:
            pass
    def go_to_song(self):
        try:
            self.driver.get(self.st_trk)
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='announcement__ack sc-button sc-button-medium']"))).click()
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (
                By.XPATH, "//button[@class='sc-button-more sc-button sc-button-medium sc-button-responsive']"))).click()
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='sc-button-addtoset moreActions__button sc-button-medium']"))).click()
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@class='textfield__input sc-input sc-input-medium']")))
            self.element.send_keys(self.playl)
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,
                 "//button[@class='addToPlaylistButton sc-button sc-button-medium sc-button-responsive']"))).click()
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,
                 "//button[@class='modal__closeButton']"))).click()
            elem2 = self.driver.find_elements_by_xpath("//a[@class='soundTitle__title sc-link-dark']")
            self.links.append(elem2[0].get_attribute("href"))
            self.st_trk = elem2[0].get_attribute("href")
        except Exception:
            pass

    def next_songs(self):
        try:
            while True:
                self.driver.get(self.st_trk)
                self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[@class='sc-button-more sc-button sc-button-medium sc-button-responsive']"))).click()
                self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='sc-button-addtoset moreActions__button sc-button-medium']"))).click()
                self.element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//input[@class='textfield__input sc-input sc-input-medium']")))
                self.element.send_keys(self.playl)
                self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//button[@class='addToPlaylistButton sc-button sc-button-medium sc-button-responsive']"))).click()
                self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH,
                     "//button[@class='modal__closeButton']"))).click()
                elem2 = self.driver.find_elements_by_xpath("//a[@class='soundTitle__title sc-link-dark']")
                check = 0
                while check == 0:
                    check = 1
                    self.st_trk = elem2[randint(0, 2)].get_attribute("href")
                    for i in range(0, len(self.links)):
                        if self.st_trk == self.links[i]:
                            print("jest")
                            check = 0
                self.links.append(self.st_trk)
        except Exception:
            pass