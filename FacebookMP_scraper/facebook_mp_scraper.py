from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Global Data
EMAIL_CREDENTIALS = ""
PASSWORD_CREDENTIALS = ""
SEARCH_QUERIES = [
    "Realtor",
    "RealEstateAgent/Broker",
    "InsuranceBroker/Agent",
    "Lawyers",
    "Accountants"
]
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2  # block popups
})
PATH_TO_CHROMEDRIVER = r"C:\Users\light\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(service = Service(PATH_TO_CHROMEDRIVER), options=CHROME_OPTIONS)

BASE_FB_MARKETPLACE_LINK = r"https://www.facebook.com/marketplace/dc/search?query="

def login(FB_MARKETPLACE_LINK):
    # Open page
    driver.get(FB_MARKETPLACE_LINK)
    try:
        # Get Log-in Field Box
        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'login_popup_cta_form')),
            print("We got the login Form!")
        )
        # Types email field
        email_field = WebDriverWait(login_form, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')),
            print("We got the email field!")
        )
        email_field.send_keys(EMAIL_CREDENTIALS)
        # Types password field
        password_field = WebDriverWait(login_form, 10).until(
            EC.presence_of_element_located((By.NAME, 'pass')),
            print("We got the password field!")
        )
        password_field.send_keys(PASSWORD_CREDENTIALS)
        # Hits Login!
        login_button = WebDriverWait(login_form, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".x1ja2u2z.x78zum5.x2lah0s.x1n2onr6.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1fq8qgq")),
            print("We got the Login button!")
        )
        login_button.click()
    except Exception as e:
        if isinstance(e, selenium.common.exceptions.TimeoutException):
            return
        else:
            print(f"An error occurred: {e}")

for SEARCH_QUERY in SEARCH_QUERIES:
    login(BASE_FB_MARKETPLACE_LINK + SEARCH_QUERY)
