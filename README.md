# Automation Framework (Behave + Python + REST + Selenium) 

This framework supports **API, UI, and E2E testing** using **Behave (BDD)**. It is structured for modular, scalable automation with automatic logging, reporting, and tag-driven execution.

---

## Folder Structure

```
test-automation-framework/
│
├── tests/
│   ├── api/
│   │   ├── features/              # API feature files (Gherkin)
│   │   │   ├── create_users.feature
│   │   │   └── get_users.feature
│   │   │
│   │   ├── steps/                 # API step definitions
│   │   │
│   │   ├── endpoints/             # API endpoint definitions (paths only)
│   │   │
│   │   ├── environment.py         # API hooks (before_all, before_scenario)
│   │   └── behave.ini             # API Behave config
│   │
│   ├── ui/
│   │   ├── features/              # UI feature files
│   │   │   └── google_search.feature
│   │   │
│   │   ├── pages/                 # Page Objects
│   │   │
│   │   ├── steps/                 # UI step definitions
│   │   │
│   │   ├── environment.py         # UI hooks
│   │   └── behave.ini             # UI Behave config
│
├── data/
│   └── user_payload.json          # Test data (JSON-based, generic)
│
├── utils/
│   └── data_loader.py             # Generic utilities (JSON loaders, helpers)
│
├── logs/                          # Execution logs
│
├── venv/                          # Virtual environment (local only)
│
├── .env                           # Environment variables (BASE_URL, tokens)
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md
```

---

## Setup

1. Install Python 3.9+
2. Install dependencies:

```bash
cd tests
python3 -m venv venv
source venv/bin/activate
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
