from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def check_finance_rule():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Use LOCAL chromedriver (no internet needed)
    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://www.rbi.org.in")

        soup = BeautifulSoup(driver.page_source, "html.parser")

        title = soup.find("title")

        if title:
            return f"Finance rule source: {title.text}"
        else:
            return "Finance rule: RBI regulations apply"

    except Exception as e:
        return f"Scraping Error: {str(e)}"

    finally:
        driver.quit()
