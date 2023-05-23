import time
import pyautogui
import functions
from constants import Template, Url, Message, Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# get all links from trending dynamically since they are changing every refresh
links = functions.get_all_urls()
time.sleep(3)

for link in links:

    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # check for the privacy popup and click it
    try:
        functions.accept_privacy(browser)
    except:
        pass

    # check if there is a LETS GO Button and click it
    try:
        time.sleep(1)
        functions.find_and_click(Template.LETS_GO)
    except:
        pass

    print(link + " :")

    # Check if menu exists and click on it, the logic behind it is that if the response comes false every time and matches no template, there is no menu in the screen
    response = functions.find_and_click(Template.MENU)
    if response == False:
        response = functions.find_and_click(Template.MENU_2)
        if response == False:
            response = functions.find_and_click(Template.MENU_3)
            if response == False:
                response = functions.find_and_click(Template.MENU_4)
                if response == False:
                    response = functions.find_and_click(Template.MENU_5)
                if response == False:
                    print(Message.NO_MENU)
                    print(link)
                    continue

    # if the conditions before aren't met, the menu exists
    print(Message.FOUND_MENU + str(response))
    time.sleep(1)

    # check if share button exists and is clicked
    response = functions.find_and_click(Template.SHARE_BUTTON)
    print(Message.FOUND_BUTTON_SHARE + str(response))
    time.sleep(1)

    # check if the share button is redirecting to twitter
    response = functions.check_if_tab_is_open_and_loaded(Url.TWITTER_WEBSITE, browser, Selector.TWITTER_DIV_XPATH)
    print(Message.SHARE_URL_REACHED + str(response))
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[0])
    time.sleep(1)

    # check if Send Feedback button exists and is clicked
    response = functions.find_and_click(Template.FEEDBACK_BUTTON)
    print(Message.FOUND_BUTTON_FEEDBACK + str(response))
    time.sleep(1)

    # check if the Send Feedback button is redirecting to FRVR feedback page
    response = functions.check_if_tab_is_open_and_loaded(Url.FRVR_SUPPORT, browser, Selector.FRVR_TROUBLESHOOTING_XPATH)
    print(Message.FEEDBACK_URL_REACHED + str(response))
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[0])
    time.sleep(1)

    # check if Privacy button exists and is clicked
    response = functions.find_and_click(Template.LEGAL_BUTTON)
    print(Message.FOUND_BUTTON_PRIVACY + str(response))
    time.sleep(1)

    if response:
        # check if the Privacy button is redirecting to twitter
        response = functions.check_if_tab_is_open_and_loaded(Url.FRVR_LEGAL, browser, Selector.FRVR_LEGAL_TITLE_XPATH)
        print(Message.PRIVACY_URL_REACHED + str(response))
        window_handles = browser.window_handles
        browser.switch_to.window(window_handles[0])
        time.sleep(1)
    else:
        print(Message.NO_LEGAL+link)

    # click FRVR Games
    response = functions.find_and_click(Template.FRVR_GAMES)
    print(Message.FOUND_BUTTON_FRVR_GAMES + str(response))
    pyautogui.sleep(1)

    # check if the FRVR Games button is redirecting to FRVR
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[0])
    response = functions.check_if_tab_is_open_and_loaded(Url.FRVR_WEBSITE, browser, Selector.FRVR_PRIVACY_POPUP_BUTTON_ID)
    print(Message.FRVR_GAMES_URL_REACHED + str(response))
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[0])
    time.sleep(1)

    # click FACEBOOK
    response = functions.find_and_click(Template.FACEBOOK_BUTTON)
    print(Message.FOUND_BUTTON_FACEBOOK + str(response))
    pyautogui.sleep(1)
    time.sleep(1)

    # check if the FACEBOOK button is redirecting
    response = functions.check_if_tab_is_open_and_loaded(Url.FACEBOOK, browser, Selector.FACEBOOK_LOGIN_BUTTON_XPATH)
    print(Message.FACEBOOK_URL_REACHED + str(response))
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[0])
    time.sleep(1)

    # check if the close menu button is closing the menu, the logic is to re-test if any element from the menu is present
    pyautogui.sleep(2)
    response = functions.find_and_click(Template.CLOSE_MENU)
    if response == True:
        response = functions.find_and_click(Template.SHARE_BUTTON)
        if response == False:
            print(Message.FOUND_CLOSE_MENU+str(response))
        else:
            print(Message.FOUND_CLOSE_MENU+str(response))
    time.sleep(3)
    browser.quit()
