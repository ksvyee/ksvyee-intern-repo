from appium import webdriver
from appium.options.windows import WindowsOptions

options = WindowsOptions()
options.app = "notepad.exe"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

text_area = driver.find_element("class name", "RichEditD2DPT")
text_area.send_keys("Hello, World!")

assert "Hello, World!" in text_area.text, "Text was not entered correctly!"

file_menu = driver.find_element("name", "File")
file_menu.click()

save_as = driver.find_element("name", "Save as")
save_as.click()

save_as_options = WindowsOptions()
save_as_options.app = "Root"
save_as_driver = webdriver.Remote("http://127.0.0.1:4723", options=save_as_options)

save_dialog = save_as_driver.find_element("name", "Save as")

assert save_dialog is not None, "Save As dialog did not open!"

file_name_input = save_as_driver.find_element("class name", "Edit")
file_name_input.clear()
file_name_input.send_keys("TestAutomation.txt")

assert file_name_input.get_attribute("Value.Value") == "TestAutomation.txt", "Filename input failed!"

save_button = save_as_driver.find_element("name", "Save")
save_button.click()

driver.quit()
