from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

searchterm = 'vgen'
url = "https://www.google.com/search?q="+searchterm+"&tbm=isch&source=lnms&sa=X&ved=0ahUKEwifn8HF7I3tAhWSOnAKHfaDC3gQ_AUICygB&biw=1920&bih=937&dpr=1"
driver = webdriver.Chrome()
driver.get(url)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_class_name("mye4qd").click()
        except:
            break
    last_height = new_height

# 결과 더보기 버튼 클릭


if not os.path.exists("out"):
    os.makedirs("out")
images = driver.find_elements_by_class_name("rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_class_name("n3VNCb").get_attribute("src")
        # imgUrl = driver.find_element_by_class_name("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "out/test" + str(count) + ".jpg")
        count = count + 1
    except:
        count = count + 1
        pass

driver.close()
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()