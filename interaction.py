from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

def wiki_search():
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

    all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")

    search_bar = driver.find_element(By.NAME, value="search")
    search_bar.send_keys("Python", Keys.ENTER)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname_bar = driver.find_element(By.NAME, value="fName")
fname_bar.send_keys("Fotis", Keys.TAB, "Fotiadis", Keys.TAB, "fotis.fotiadis.85@gmail.com", Keys.TAB, Keys.ENTER)




# driver.quit()