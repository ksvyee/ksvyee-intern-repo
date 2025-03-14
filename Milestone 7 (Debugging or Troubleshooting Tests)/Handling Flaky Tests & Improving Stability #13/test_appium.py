import time
from appium import webdriver
from appium.options.windows import WindowsOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_RETRIES = 3
TEST_RUNS = 5

def run_test():
    options = WindowsOptions()
    options.app = "notepad.exe"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    wait = WebDriverWait(driver, 10)
    retries = 0

    while retries < MAX_RETRIES:
        try:
            text_area = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "RichEditD2DPT")))
            text_area.send_keys("Hello, World!")
            print("Test passed!")
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{MAX_RETRIES}: {e}")
            time.sleep(2)
    else:
        print("Test failed after maximum retries.")

    driver.quit()

for i in range(TEST_RUNS):
    print(f"\nRunning Test #{i+1}")
    run_test()
