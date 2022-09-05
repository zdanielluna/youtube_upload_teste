from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set browser
profile = webdriver.FirefoxProfile(
    r'C:\Users\dan_z\AppData\Roaming\Mozilla\Firefox\Profiles\rz0f1z17.default-release')
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

browser = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired, executable_path='C:\selenium_drivers\geckodriver.exe')

# go to youtube studio
browser.get('https://www.youtube.com/')
sleep(4)
browser.find_element_by_css_selector('#avatar-btn').click()
sleep(2)
browser.find_element_by_css_selector(
    '.style-scope:nth-child(1) > #items > .style-scope:nth-child(3) > #endpoint #label').click()

sleep(2)

# upload button
browser.find_element_by_css_selector('#upload-button').click()

sleep(2)

# send video
video_path = r'C:\Users\dan_z\Videos\fifacorte.mp4'
browser.find_element_by_css_selector('#content > input:nth-child(6)').send_keys(video_path)
browser.find_element_by_css_selector('#select-files-button').click()

sleep(4)

# set title
title_area = WebDriverWait(browser, 50).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#title-textarea > #container > #outer > #child-input #textbox")))
# title_area = browser.find_element_by_css_selector(
#     '#title-textarea > #container > #outer > #child-input #textbox')
title_area.clear()
title_area.send_keys('título teste')

sleep(0.25)

# set description
description_area = browser.find_element_by_css_selector(
    '#description-textarea > #container > #outer > #child-input #textbox')
description_area.clear()
description_area.send_keys('description teste')

sleep(0.25)

# set for kids
for_kids = '.ytkc-made-for-kids-select:nth-child(2) #offRadio'
not_for_kids = '#description-textarea > #container > #outer > #child-input #textbox'

browser.find_element_by_css_selector(for_kids).click()
browser.find_element_by_css_selector(not_for_kids).click()

# show more button
browser.find_element_by_css_selector('#toggle-button > .label').click()

sleep(0.25)

# set tags/keywords
tag_area = browser.find_element_by_id('text-input')
tag_area.clear()
tag_area.send_keys('tag teste, teste2, tag4')

sleep(0.25)

# next button
next_bt = browser.find_element_by_id('next-button')
next_bt.click()
sleep(0.25)
next_bt.click()
sleep(0.25)
next_bt.click()

# set thumb?

sleep(0.25)

# set category / realizar mapeamento de todas as categorias

sleep(0.25)

# set privacy status
private = '#private-radio-button #offRadio'
unlisted = '.style-scope:nth-child(13) #offRadio'
public = '.style-scope:nth-child(19) #offRadio'
browser.find_element_by_css_selector(private).click()

sleep(0.25)

# publish button
browser.find_element_by_id('done-button').click()
