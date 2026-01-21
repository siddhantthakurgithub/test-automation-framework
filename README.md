Automation Framework (Behave + Python + Requests + Selenium)

BDD-based framework for API and UI testing with:
	•	API automation (GET/POST)
	•	UI automation (Selenium WebDriver)
	•	Tag-driven execution (@api, @ui, @smoke)
	•	Environment config via .env
	•	Automatic logging and reporting
	•	Setup/cleanup fixtures

⸻

Folder Structure

Tests/
api/
    |-- features/
    │   |-- environment.py
    │   |-- steps/
    │   │   |-- test_1_steps.py
    │   │   |-- test_2_steps.py
    │   |-- test_1.feature
    │   |-- test_2.feature
    |-- logs/
    |-- reports/
ui/
    |-- features/
    │   |-- environment.py
    │   |-- steps/
    │   │   |-- test_1_steps.py
    │   │   |-- test_2_steps.py
    │   |-- test_1.feature
    │   |-- test_2.feature
    |-- logs/
    |-- reports/
e2e/
    |-- features/
    │   |-- environment.py
    │   |-- steps/
    │   │   |-- test_1_steps.py
    │   │   |-- test_2_steps.py
    │   |-- test_1.feature
    │   |-- test_2.feature
    |-- logs/
    |-- reports/


⸻

Setup

Install dependencies:

pip install -r requirements.txt

requirements.txt:

behave==1.2.6
requests==2.31.0
selenium==4.15.0
webdriver-manager==5.5.0
python-dotenv==1.0.0

.env file:

BASE_URL=https://jsonplaceholder.typicode.com
TOKEN=


⸻

How to Run

# Run all tests
behave

# Run only API tests
behave --tags=@api

# Run specific scenario
behave --tags=@create_user


⸻

Logging & Reporting
	•	Logs: logs/test.log
	•	Screenshots for UI failures: logs/
	•	JSON report: reports/report.json (via behave.ini)
⸻

Hooks & Fixtures
	•	before_all / after_all: global setup/cleanup
	•	before_scenario / after_scenario: scenario-level fixtures
	•	after_step: auto logging + screenshot capture
	•	context.setup_data: temporary storage for scenario-specific data

⸻

Key Features
	•	BDD approach using Behave
	•	Automatic logging and reporting
	•	Tag-driven execution
