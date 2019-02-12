from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Users\Bunmi-Pc\PycharmProjects\Loopmi\chromedriver_win32\chromedriver.exe")

url = "https://www.compendiumdev.co.uk/"
#use this command to navigate to the page url
driver.get(url)

#use this commmand to maximise window
driver.maximize_window()

#use this command to click on an element on the webpage
automation = driver.find_element_by_xpath("//*[@id='cssmenu']/ul/li[2]/a")
automation.click()

#Use this command to execute a click
automation = driver.find_element_by_link_text("Selenium WebDriver With Java")
automation.click()

#use this to validate that a text is prsent
automation = driver.find_element_by_tag_name('h1')
assert automation.tag_name == 'Selenium WebDriver with Java - Online Training Course'
print(automation.text)

#Use this command to get a screenshot
driver.get_screenshot_as_file("automation.png")

#to specify number of seconds to wait after execution
time.sleep(3)

#close the browser
driver.quit()