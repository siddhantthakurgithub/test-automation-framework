import logging
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = Options()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    # Load .env file
    load_dotenv()  # loads from root .env by default
    context.base_url = os.getenv("BASE_URL_UI")


def after_step(context, step):
    """Automatically log every step result"""
    if step.status == "failed":
        logging.error(f"Step failed: {step.name}")
        # If API response exists, log it
        if hasattr(context, "response"):
            logging.error(f"Response body: {context.response.text}")
        # If UI driver exists, take screenshot
        if hasattr(context, "driver"):
            screenshot_file = f"logs/{step.name.replace(' ', '_')}.png"
            context.driver.save_screenshot(screenshot_file)
            logging.info(f"Screenshot saved: {screenshot_file}")
    else:
        logging.info(f"Step passed: {step.name}")

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()