import time
from appium import webdriver
from appium.options.windows import WindowsOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_RETRIES = 3
TEST_RUNS = 5

# Page Object Model (POM) for Notepad
class NotepadPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_text_area(self):
        """Wait for and return the text area element."""
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "RichEditD2DPT")))

    def enter_text(self, text):
        """Enter text into the Notepad text area."""
        text_area = self.get_text_area()
        text_area.send_keys(text)

# Helper function for retries
def retry_operation(operation, retries=MAX_RETRIES, delay=2):
    """Retries a given operation with a specified number of attempts."""
    for attempt in range(retries):
        try:
            return operation()
        except Exception as e:
            print(f"Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    raise Exception("Operation failed after maximum retries")

# Setup driver function
def setup_driver():
    """Initialize the Appium driver for Notepad."""
    options = WindowsOptions()
    options.app = "notepad.exe"
    return webdriver.Remote("http://127.0.0.1:4723", options=options)

# Main test function
def run_test():
    """Run the Notepad automation test."""
    driver = setup_driver()
    notepad = NotepadPage(driver)

    try:
        retry_operation(lambda: notepad.enter_text("Hello, World!"))
        print("Test passed!")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()

for i in range(TEST_RUNS):
    print(f"\nRunning Test #{i+1}")
    run_test()
