import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/ui_test.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# -------------------------
# Hook: Before each scenario
# -------------------------
def before_scenario(context, scenario):
    print(f"\n[DEBUG] Running before_scenario for: {scenario.name}, tags: {scenario.tags}")
    if "ui" in scenario.tags:
        options = Options()
        options.add_argument("--start-maximized")
        # Uncomment the next line if you want headless mode
        # options.add_argument("--headless=new")

        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        logging.info(f"Browser launched for scenario: {scenario.name}")

# -------------------------
# Hook: After each scenario
# -------------------------
def after_scenario(context, scenario):
    # Quit browser if it exists
    if hasattr(context, "driver"):
        context.driver.quit()
        logging.info(f"Browser closed for scenario: {scenario.name}")

    # Clean context attributes
    for attr in list(context.__dict__.keys()):
        if not attr.startswith("_"):
            delattr(context, attr)

# -------------------------
# Hook: After each step
# -------------------------
def after_step(context, step):
    if step.status == "failed":
        logging.error(f"Step failed: {step.name}")
        if hasattr(context, "driver"):
            # Save screenshot
            screenshot_file = f"logs/{step.name.replace(' ', '_')}.png"
            context.driver.save_screenshot(screenshot_file)
            logging.info(f"Screenshot saved: {screenshot_file}")
    else:
        logging.info(f"Step passed: {step.name}")

# Optional: Print when environment.py is loaded
print("[DEBUG] environment.py loaded successfully!")