from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# US
source = driver.find_element_by_xpath('//*[@id="box3"]')
destination = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# Norway
source = driver.find_element_by_xpath('//*[@id="box1"]')
destination = driver.find_element_by_xpath('//*[@id="box101"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# Sweden
source = driver.find_element_by_xpath('//*[@id="box2"]')
destination = driver.find_element_by_xpath('//*[@id="box102"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# South Korea
source = driver.find_element_by_xpath('//*[@id="box5"]')
destination = driver.find_element_by_xpath('//*[@id="box105"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# Italy
source = driver.find_element_by_xpath('//*[@id="box6"]')
destination = driver.find_element_by_xpath('//*[@id="box106"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# Spain
source = driver.find_element_by_xpath('//*[@id="box7"]')
destination = driver.find_element_by_xpath('//*[@id="box107"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
# Denmark
source = driver.find_element_by_xpath('//*[@id="box4"]')
destination = driver.find_element_by_xpath('//*[@id="box104"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()