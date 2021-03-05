from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By

import time

def main():
    operator = []

    file = open('operators.txt', 'r')

    for row in file:
        operator.append(row.strip("\n"))

    createImages(operator)

def createImages(all):
    for person in all:
        browserandCreate(person)


def browserandCreate(people):

    #take screenshot
    options = Options()
    options.headless = True
    assert options.headless
    driver = webdriver.Chrome(options=options)

    driver.get('https://aceship.github.io/AN-EN-Tags/akhrelite.html')
    inputElement = driver.find_element_by_id('opname')


    inputElement.send_keys(people)
    inputElement.send_keys(Keys.ENTER)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'requiremats-box')))
    element = driver.find_element_by_class_name('requiremats-box')
    location = element.location
    size = element.size
    time.sleep(1)
    driver.save_screenshot('elite1.png')

    # crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+141
    im = Image.open('elite1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(people + ' elite1.png')

    clickElite = driver.find_element_by_id('eliteDropBtn')
    clickElite.click()
    time.sleep(1)
    clickElite = driver.find_element_by_link_text('Elite 2')
    clickElite.click()
    element = driver.find_element_by_class_name('requiremats-box')
    location = element.location
    size = element.size
    driver.save_screenshot("pelite2.png")

    # crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+141
    im = Image.open('pelite2.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(people + ' elite2.png')

    driver.quit()

main()
