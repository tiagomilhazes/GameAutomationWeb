import time
import cv2 as cv
import numpy as np
import pyautogui
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import Template, Url, Message, Selector

import constants as c


def find_and_click(image_path):
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    cv.imwrite("screenshot.png", screenshot)
    screenshot = cv.imread("screenshot.png", cv.COLOR_BGR2GRAY)
    template = cv.imread(image_path, cv.COLOR_BGR2GRAY)
    result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # print('Best Match top left position: %s' % str(max_loc))
    # print('Best match confidence: %s' % max_val)

    threshold = 0.5
    if max_val >= threshold:
        # print('Found!!')
        template_w = template.shape[1]
        template_h = template.shape[0]
        top_left = max_loc
        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
        cv.rectangle(screenshot, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
        # calculate center coordinates
        center_x = int((top_left[0] + bottom_right[0]) / 2)
        center_y = int((top_left[1] + bottom_right[1]) / 2)
        center = (center_x, center_y)
        # print('Center of rectangle: %s' % str(center))

        #cv.imshow('Result', screenshot)
        #cv.waitKey()
        pyautogui.click(center_x, center_y)
        pyautogui.sleep(1)

        return True
    else:
        return False


def check_if_tab_is_open_and_loaded(url, driver, selector):
    try:
        #Check if the URL is equal to the current URL on the Tab
        tabs = driver.window_handles
        for tab in tabs:
            if url in driver.current_url:
                wait = WebDriverWait(driver, 10)
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, selector)))
                    return True
                except TimeoutException:
                    #workaround for a popup issue in FRVR Website
                    try:
                        if url == Url.FRVR_WEBSITE:
                            wait.until(EC.presence_of_element_located((By.XPATH, Selector.FRVR_SEARCH_BAR_XPATH)))
                            return True
                    except TimeoutException:
                        return False
        return True
    except Exception as e:
        return f"NOK - {str(e)}"


def get_all_urls():
    pyautogui.FAILSAFE = False
    # create a new Chrome browser instance
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    # browser.maximize_window()
    browser.set_window_size(1024, 900)
    browser.get(Url.FRVR_WEBSITE)
    time.sleep(3)
    accept_privacy(browser)
    time.sleep(2)

    links = []
    parent_div = browser.find_element(By.XPATH, Selector.TRENDING_GAMES_DIV_PARENT_XPATH)

    for i in range(1, 8 + 1):
        xpath = "/html/body/main/div[3]/div[2]/div[" + str(i) + "]"
        element = browser.find_element(By.XPATH, xpath)
        link = element.find_element(By.TAG_NAME, "a")
        href = link.get_attribute("href")
        links.append(href)
    # print the links
    print(links)
    browser.quit()
    return links


# def initialize_and_navigate(url):
# pyautogui.FAILSAFE = False
# create a new Chrome browser instance
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.set_window_size(1024, 900)
# navigate to frvr website
# browser.get(url)
# return browser


def accept_privacy(browser):
    try:
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, Selector.FRVR_PRIVACY_POPUP_BUTTON_ID))
        )
        button.click()
        pyautogui.sleep(2)
    except:
        pass


def accept_privacy_in_game(browser):
    try:
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, Selector.ACCEPT_PRIVACY_BUTTON_IN_GAME_ID))
        )
        button.click()
        pyautogui.sleep(2)
    except:
        pass
