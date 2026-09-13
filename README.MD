# SubTrack – Subscription Management System
 
## Overview
Most people lose track of how many subscriptions they're actually paying for until the bank statement shows up. SubTrack is a command-line tool built in Python to fix that — it lets you add, view, and remove subscriptions, and works out your total monthly and yearly spend whenever you ask for it. All the data is stored locally in a JSON file, so it's still there the next time you open the app. There's no database and no external libraries involved, just Python's built-in `json` and `os` modules.
 
## Features
- Add a subscription with its cost, billing cycle (monthly/yearly), category, and renewal date
- View all your current subscriptions in one place
- Delete a subscription once you've cancelled it
- Check your total monthly and yearly subscription spend on demand
- Data is saved to a local JSON file and loaded back in automatically the next time you run the program
## Built With
- Python 3.x
- `json` and `os` (standard library only — no third-party packages)
- Git & GitHub for version control
## Project Structure
```
SubTrack/
├── main.py                        # entry point and menu loop
├── services/
│   └── subscription_manager.py    # core logic: add/view/delete subscriptions, totals, persistence
├── subscriptions.json             # local data store (created automatically on first run)
└── README.md
```
*(Data file name assumed above — update it if `subscription_manager.py` actually writes to a different filename.)*
 
## Installation & Setup
 
### Prerequisites
- Python 3.8 or later ([download here](https://www.python.org/downloads/))
- Git ([download here](https://git-scm.com/downloads))
Check your Python version with:
```bash
python --version
```
 
### Steps
1. Clone the repository
```bash
   git clone https://github.com/<your-username>/SubTrack.git
```
2. Move into the project folder
```bash
   cd SubTrack
```
3. Run the program
```bash
   python main.py
```
   On some systems (mainly Linux/macOS) you may need `python3` instead of `python`.
 
No `pip install` step is needed — SubTrack only relies on Python's standard library.
 
## Usage
When the program starts, you'll see a menu:
```
1. View Subscriptions
2. Add Subscription
3. Delete Subscription
4. View Financial Summary
5. Exit
```
Enter the number next to the option you want and follow the prompts. When adding a subscription, you'll be asked for its name, cost, billing cycle (monthly or yearly), category, and renewal date (in DD-MM-YYYY format). Every change is saved automatically, so you can close the program and pick up right where you left off next time.
 
## Testing
There's no separate automated test suite yet — for now, verify the program works correctly with a quick manual pass:
 
1. Run `python main.py` and add a subscription with valid details — confirm it shows up under "View Subscriptions."
2. Try entering a non-numeric cost (e.g. `abc`) — confirm the program shows an error instead of crashing.
3. Delete the subscription you just added — confirm it no longer appears in the list.
4. Add two or three subscriptions with different cycles and confirm "View Financial Summary" totals them correctly.
5. Enter an invalid menu choice (e.g. `9`) — confirm the program shows an error and re-displays the menu instead of exiting.
## Screenshots
*(Add a screenshot or two of the menu and financial summary in action here — optional, but it helps show the program actually runs.)*
 
## Author
Built as a personal project to practice Python fundamentals — file handling, dictionaries, and JSON persistence — without relying on external libraries.
 