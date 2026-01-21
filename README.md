# Automation Framework (Behave + Python + REST + Selenium)

This framework supports **API, UI, and E2E testing** using **Behave (BDD)**. It is structured for modular, scalable automation with automatic logging, reporting, and tag-driven execution.

---

## Folder Structure

```
Tests/
├── api/
│   ├── features/
│   │   ├── environment.py         # Hooks: setup, cleanup, logging
│   │   ├── steps/
│   │   │   ├── test_1_steps.py
│   │   │   └── test_2_steps.py
│   │   ├── test_1.feature
│   │   └── test_2.feature
│   ├── logs/                       # Logs for API tests
│   └── reports/                    # Reports for API tests
├── ui/
│   ├── features/
│   │   ├── environment.py         # Hooks: setup, cleanup, logging, screenshots
│   │   ├── steps/
│   │   │   ├── test_1_steps.py
│   │   │   └── test_2_steps.py
│   │   ├── test_1.feature
│   │   └── test_2.feature
│   ├── pages/
│   │   └── google_page.py
│   ├── logs/                       # Logs for UI tests
│   └── reports/                    # Reports for UI tests
└── e2e/
    ├── features/
    │   ├── environment.py         # Hooks: setup, cleanup, logging
    │   ├── steps/
    │   │   ├── test_1_steps.py
    │   │   └── test_2_steps.py
    │   ├── test_1.feature
    │   └── test_2.feature
    ├── logs/                       # Logs for E2E tests
    └── reports/                    # Reports for E2E tests
```

---

## Setup

1. Install Python 3.9+
2. Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` example:

```
behave==1.2.6
requests==2.31.0
selenium==4.15.0
webdriver-manager==5.5.0
python-dotenv==1.0.0
```

3. Create a `.env` file:

```
BASE_URL=https://your-api-base-url.com
TOKEN=your_auth_token
```

---

## How to Run

```bash
# Run all API tests
behave Tests/api/features

# Run only UI tests
behave Tests/ui/features

# Run only E2E tests
behave Tests/e2e/features

# Run specific tagged scenario
behave --tags=@smoke
```

---

## Logging & Reporting

* Logs automatically saved in `logs/` folders
* Screenshots for UI failures saved in `logs/` folders
* Reports can be generated in JSON format via `behave.ini` in each module

---

## Hooks & Fixtures

* **Global hooks**: `before_all`, `after_all` for setup/cleanup
* **Step hooks**: `after_step` for automatic logging, API response logging, and UI screenshot capture
* **Context fixtures**: `context.setup_data` can store temporary data per scenario

---

## Key Features

* BDD approach with Behave
* Modular structure: API, UI, E2E separated
* Environment configuration via `.env`
* Automatic logging and reporting
* Tag-driven execution for selective tests
* Scenario-level setup/cleanup fixtures
* Ready for CI/CD integration

---
