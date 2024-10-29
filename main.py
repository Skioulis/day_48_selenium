from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_from_python():
    #finished some tasks and added it to a fuction to keep it. Continue with the exercise
    # Keeping chrome open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.python.org")

    # price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    # price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

    search_bar = driver.find_element(By.NAME, value='q')
    # print(search_bar.tag_name)

    documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    # print(documentation_link.text)

    report_bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    # print(report_bug_link.text)

    events_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

    events_titles = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

    # for title in events_titles:
    #     print(title.text)

    # for time in events_times:
    #     print(time.get_attribute("datetime").split('T')[0])





    events_dictionary = {
    i : {

    "time": events_times[i].get_attribute("datetime").split('T')[0],
    "name": events_titles[i].text
    }
    for i in range(len(events_times))

    }

    print(events_dictionary)


    #
    #
    # upcoming_events = events_section.find_elements(By.CSS_SELECTOR, 'ul.list-recent-events li')
    #
    # for event in upcoming_events:
    #         title = event.find_element(By.TAG_NAME, 'a').text
    #         date = event.find_element(By.CLASS_NAME, 'event-date').text
    #         print(f"{date}: {title}")


    # driver.close()
    driver.quit()

get_from_python()