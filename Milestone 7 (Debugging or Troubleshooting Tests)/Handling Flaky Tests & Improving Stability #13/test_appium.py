from appium import webdriver
from appium.options.windows import WindowsOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = WindowsOptions()
options.app = "notepad.exe"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 30)
text_area = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "RichEditD2DPT")))

text_area.send_keys("Hello, World!")

driver.quit()
