import time
import logging
from appium import webdriver
from appium.options.windows import WindowsOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
MAX_RETRIES = 3
TEST_RUNS = 3

# Logging Setup
logging.basicConfig(filename="test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Page Object Model (POM) for Calculator WebView
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_converter(self):
        """Navigate to the Converter section in Calculator."""
        menu_button = self.wait.until(EC.element_to_be_clickable((By.NAME, "Open Navigation")))
        menu_button.click()
        converter_option = self.wait.until(EC.element_to_be_clickable((By.NAME, "Currency")))
        converter_option.click()
        logging.info("Navigated to Currency Converter")

    def switch_to_webview(self):
        """Switch to WebView context inside Calculator."""
        for attempt in range(MAX_RETRIES):
            try:
                contexts = self.driver.contexts  # Get available contexts
                webview_context = next(ctx for ctx in contexts if "WEBVIEW" in ctx)
                self.driver.switch_to.context(webview_context)
                logging.info("Switched to WebView context")
                return
            except Exception as e:
                logging.warning(f"Retrying WebView switch ({attempt+1}/{MAX_RETRIES}): {e}")
                time.sleep(2)
        raise Exception("Failed to switch to WebView")

    def get_conversion_rate(self):
        """Extracts the currency conversion rate from WebView."""
        self.switch_to_webview()
        rate_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.exchange-rate")))
        rate_text = rate_element.text
        logging.info(f"Extracted conversion rate: {rate_text}")
        return rate_text

    def capture_screenshot(self, filename="screenshot.png"):
        """Capture a screenshot for debugging."""
        self.driver.get_screenshot_as_file(filename)
        logging.info(f"Screenshot saved: {filename}")

# Helper function for retries
def retry_operation(operation, retries=MAX_RETRIES, delay=2):
    """Retries a given operation multiple times before failing."""
    for attempt in range(retries):
        try:
            return operation()
        except Exception as e:
            logging.warning(f"Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    raise Exception("Operation failed after maximum retries")

# Setup driver function
def setup_driver():
    """Initialize the Appium driver for Windows Calculator."""
    options = WindowsOptions()
    options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"  # Windows Calculator UWP ID
    return webdriver.Remote("http://127.0.0.1:4723", options=options)

# Main test function
def run_test():
    """Run the Calculator WebView automation test."""
    logging.info("Starting test execution")
    driver = setup_driver()
    calculator = CalculatorPage(driver)

    try:
        calculator.open_converter()
        conversion_rate = retry_operation(calculator.get_conversion_rate)
        print(f"Conversion Rate: {conversion_rate}")
        logging.info("Test passed!")
    except Exception as e:
        logging.error(f"Test failed: {e}")
        calculator.capture_screenshot("failure_screenshot.png")
    finally:
        driver.quit()
        logging.info("Driver closed.")

# Execute tests multiple times
for i in range(TEST_RUNS):
    print(f"\nRunning Test #{i+1}")
    logging.info(f"Running Test #{i+1}")
    run_test()
