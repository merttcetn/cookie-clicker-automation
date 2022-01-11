from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Program Files (x86)\chromedriver.exe"  # Path of the selenium driver
s = Service(executable_path=PATH)
driver = webdriver.Chrome(service=s)  # Every selenium file needs above lines (For my computer :D)

driver.get("https://orteil.dashnet.org/cookieclicker/")  # URL of the game

driver.implicitly_wait(5)

the_cookie = driver.find_element(By.ID, "bigCookie")
cookie_counter = driver.find_element(By.ID, "cookies")

items_to_buy = [driver.find_element(By.ID, "productPrice1"), driver.find_element(By.ID, "productPrice0")]  # Items can be modified


for i in range(1000):
    actions = ActionChains(driver)
    actions.click(the_cookie)
    actions.perform()

    count = int(cookie_counter.text.split(" ")[0])

    for item_to_buy in items_to_buy:
        price = int(item_to_buy.text)

        buy_action = ActionChains(driver)  # Action buffer
        buy_action.click(item_to_buy)  # click to buy

        if count >= price:
            buy_action.perform()  # Buy the upgrade!
