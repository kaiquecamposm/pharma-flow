# Pharma Flow 💊

## 📍 Overview

Pharma Flow is a Python application designed to manage clinical and production data in the pharmaceutical industry. It provides features for registering clinical data, tracking patient information, generating reports, detecting outliers, managing educational modules, and auditing actions. The project aims to streamline data management and analysis in pharmaceutical environments.

## ✨ Features

- Register Clinical Data: Record patient clinical measurements (e.g., blood pressure, heart rate).

- Outlier Detection: Detect statistical and rule-based outliers in clinical and production data.

- Patient & Lote Management: Archive and manage patient records and production batches (lotes).

- Educational Modules: Track user progress and generate certificates for completed modules.

- Sprint Reports: Generate periodic reports with regulatory and environmental indicators.

- Audit Logs: Keep detailed logs of actions performed in the system.

## 💻 Technologies Used

- Python 3.11+

- NumPy: Numerical operations

- Rich: Fancy console outputs

## 📦 Dependencies

```ipi
cffi==2.0.0
cryptography==45.0.7
markdown-it-py==4.0.0
mdurl==0.1.2
numpy==2.3.3
pycparser==2.23
Pygments==2.19.2
rich==14.1.0
```

## 👤 User Accounts

- Pre-registered user types are stored in:

```bash
src/core/shared/databases/users.json
```

- Default admin login:

```bash
Email: admin@admin.com
Password: admin
```

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/kaiquecamposm/pharma-flow.git
cd pharma-flow
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Linux/macOS:

```bash
source venv/bin/activate
```

- Windows (CMD):

```bash
venv\Scripts\activate
```
- Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

5. Run the application:

```bash
python src/app.py
```

## 📌 Requirements

- Functional Requirements (RF)
    - [x] Users must be able to register (researcher, manager, or auditor).
    - [x] Users must be able to authenticate.
    - [x] Users must be able to retrieve the profile of a logged-in user.
    - [x] Users must be able to record, store, and version clinical data.
    - [x] Users must be able to record, store, and version manufacturing data.
    - [x] Users must be able to consult audit trails of performed operations.
    - [x] Users must be able to apply patient stratification algorithms.
    - [x] Users must be able to detect outliers (values that do not fit the standard) in time series of clinical or manufacturing data.
    - [x] Users must be able to predict environmental failures in the production line.
    - [x] Users must be able to register and monitor environmental indicators (e.g., energy consumption per batch, volume of recovered solvents).
    - [x] Users must be able to generate sprint reports including regulatory and environmental indicators.
    - [x] Users must be able to access interactive educational modules on environmental best practices.
    - [x] Users must be able to issue completion certificates after full participation in trainings.
- Business Rules (RN)
    - [x] Users cannot register with a duplicate email.
    - [x] All system access must be logged with date, time, and user identity.
    - [x] Changes to clinical data cannot overwrite previous records, only create a new version.
    - [x] Environmental indicators must be registered per produced batch.
    - [x] Certificates for environmental modules can only be issued after 100% participation.
    - [x] The system must prevent permanent deletion of data, allowing only archiving.
    - [x] Environmental compliance checks must follow the PDCA cycle (Plan, Do, Check, Act).
- Non-Functional Requirements (RNF)
    - [x] Clinical and manufacturing data must be stored reliably and persistently.
    - [x] Each function must be accompanied by asymptotic complexity analysis (Big-O notation)
    - [ ] Unit test suite with coverage above 80%.
    - [x] The system must operate according to Agile Software Engineering principles, allowing iterative cycles and continuous inspection.
    - [x] The system must comply with GxP standards (GLP, GCP, GMP) and FDA 21 CFR Part 11 requirements.
    - [x] Performance must allow efficient processing of clinical and manufacturing data.
    - [x] Audit trails and logs must be maintained immutably.

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📝 License

This project is licensed under the [MIT License](./LICENSE).
