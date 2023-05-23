class Url:
    # FRVR website
    FRVR_WEBSITE = "https://frvr.com/"
    FRVR_SUPPORT = "https://frvr.com/tutorials/"
    FRVR_LEGAL = "https://frvr.com/legal/"
    FACEBOOK = "https://www.facebook.com/frvrgames"
    TWITTER_WEBSITE = "https://twitter.com/"


class Selector:
    TRENDING_GAMES_DIV_PARENT_XPATH = "/html/body/main/div[3]/div[2]"
    FACEBOOK_LOGIN_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[5]/div/div"
    FRVR_LEGAL_TITLE_XPATH = "/html/body/main/div/div/div/content/inner/a[1]/h1"
    FRVR_TROUBLESHOOTING_XPATH = "/html/body/main/div/main/ul/li[1]/a"
    FRVR_SEARCH_BAR_XPATH = "/html/body/main/div[1]/div[1]/div/div[2]/div/div/input"
    FRVR_PRIVACY_POPUP_BUTTON_ID = "onetrust-accept-btn-handler"
    ACCEPT_PRIVACY_BUTTON_IN_GAME_ID = "gdpr-button"
    TWITTER_DIV_XPATH = "/html/body/div/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span/span/span"
    BY_XPATH = "XPATH"
    BY_ID = "ID"


class Template:
    # Templates used for the automation
    LETS_GO = "images/letsGo.png"
    MENU = "images/menu.png"
    MENU_2 = "images/menu2.png"
    MENU_3 = "images/menu3.png"
    MENU_4 = "images/menu4.png"
    MENU_5 = "images/menu5.png"
    SHARE_BUTTON = "images/share.png"
    FEEDBACK_BUTTON = "images/feedback.png"
    LEGAL_BUTTON = "images/legal.png"
    FRVR_GAMES = "images/frvrgames.png"
    FACEBOOK_BUTTON = "images/facebook.png"
    CLOSE_MENU = "images/closeMenu.png"


class Message:
    # Strings used for printed messages
    NO_MENU = "The following Game doesnt have a Menu:"
    NO_LEGAL = "The following Game doesnt have a Legal Button: "
    FOUND_MENU = "Found menu and clicked: "
    FOUND_CLOSE_MENU = "Found close menu button and clicked: "
    FOUND_BUTTON_SHARE = "Found share menu button and clicked: "
    FOUND_BUTTON_FEEDBACK = "Found Feedback menu button and clicked: "
    FOUND_BUTTON_FACEBOOK = "Found FACEBOOK button and clicked: "
    FOUND_BUTTON_PRIVACY = "Found Privacy menu button and clicked: "
    FOUND_BUTTON_FRVR_GAMES = "Found FRVR GAMES button and clicked: "
    SHARE_URL_REACHED = "Share button URL: "
    PRIVACY_URL_REACHED = "Privacy button URL: "
    FEEDBACK_URL_REACHED = "Send Feedback button URL: "
    FRVR_GAMES_URL_REACHED = "FRVR GAMES button URL: "
    FACEBOOK_URL_REACHED = "Facebook button URL: "
