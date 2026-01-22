import os
import logging
from dotenv import load_dotenv

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/test.log",       # Log file
    level=logging.INFO,             # Log all info + errors
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def before_all(context):
    # Load .env file
    load_dotenv()  # loads from root .env by default

    context.base_url = os.getenv("BASE_URL_API")
    context.token = os.getenv("TOKEN")

    context.headers = {
        "Content-Type": "application/json"
    }

    if context.token:
        context.headers["Authorization"] = f"Bearer {context.token}"
        
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