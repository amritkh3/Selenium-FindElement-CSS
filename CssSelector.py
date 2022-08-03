"""finding element using CSS selector Locator
1. import time  from python
2. import webdriver from selenium.
3.import chromedrivermanager.in order to import chromedrivermanager 
ask pip to installwebdriver_manager
4.install chromedrivermanager and assign it to the variale driver.
5.use get fumction to open the web page with the help of url.
ie.driver.get("url")
6.Go to theoptin you want to click and right click >> Inspect.
7.On inspecting the web element, it will show an input tag and attributes like class and id.

8.Use the id and these attributes to construct CSS which, in turn, will locate the first name field.
9.similarly for email
Go to the email tab and right click >> Inspect.
On inspecting the web element, it will show an input tag and attributes like class and id.
Use the id and these attributes to construct CSS which, in turn, will locate the first name field.
"""
import time#this is python time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager#if weddriver_manager is not found run
#pip install webdrive_manager
driver=webdriver.Chrome(ChromeDriverManager().install())# your entire selenium chrome package
from selenium.webdriver.common.by import By
driver. get("https://the-internet.herokuapp.com/")
time.sleep(3)#this will hold the time for 3 seconds
driver.refresh()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"a[href='/abtest']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"a[target='_blank']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[id='email']").send_keys("amrit_kh3@yahoo.com")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"select[class='language']").click()
time.sleep(3)
driver.quit()
