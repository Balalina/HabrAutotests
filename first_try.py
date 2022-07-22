from selenium.webdriver.chrome import webdriver
import time

driver = webdriver.WebDriver(executable_path="chromedriver.exe")

driver.get("http://habr.com")

time.sleep(5)

driver.quit()


