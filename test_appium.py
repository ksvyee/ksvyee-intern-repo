from appium import webdriver
from appium.options.windows import WindowsOptions

options = WindowsOptions()
options.app = "notepad.exe"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

text_area = driver.find_element("class name", "RichEditD2DPT")
text_area.send_keys("Hello, World!")
