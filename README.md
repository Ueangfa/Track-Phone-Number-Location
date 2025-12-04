# Track Phone Number Location
Python tool for phone number metadata lookup. Provides region, carrier, and time zone details, does not track real-time device location.

# Phone Number Info Lookup (Python)

Track **basic information** about a phone number using Python – such as country/region, carrier, and possible time zone(s) – using the `phonenumbers` library.

> ⚠️ This project **does not** track real-time GPS location. It only uses public numbering data. It is for learning and educational purposes.

---

## ✨ Features

- ✅ Validate phone numbers
- 🌍 Show country / region
- 📡 Show carrier (network) if available
- 🕒 Show possible time zone(s)
- 💻 Simple command-line interface

---

## 🛠 Tech Stack

- **Language:** Python 3
- **Library:** [`phonenumbers`](https://pypi.org/project/phonenumbers/)

---

## 📦 Installation

1. Clone the repository:
```
git clone https://github.com/<your-username>/phone-number-info-lookup.git
cd phone-number-info-lookup
```

2. (Optional)(Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
``` 
---

## ▶️ Usage
Run the script from the project folder:
```
main.py
```
Enter a phone number when prompted, for example:
```
+14155552671
```
Example output:
<img width="982" height="814" alt="2" src="https://github.com/user-attachments/assets/16845e9e-573a-4e0c-9381-d95b24e15380" />



