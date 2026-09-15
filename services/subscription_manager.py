from data.file_handler import load_data, save_data
from models.user import create_user, add_subscription, remove_subscription
from models.subscription import create_subscription, format_subscription

def initialize_app(username="Default User"):
    data = load_data() or {}
    username = username.strip() if username and username.strip() else "Default User"
    
    # Upgrade single-user JSON structure to multi-user dictionary
    if "users" not in data:
        old_user = data.get("username", "Default User")
        old_subs = data.get("subscriptions", [])
        data = {"users": {old_user: {"username": old_user, "subscriptions": old_subs}}}
    
    # Create a new profile if the username does not exist
    if username not in data["users"]:
        data["users"][username] = create_user(username)
        save_data(data)
        
    return data["users"][username]

def _sync_user_to_db(user):
    """Saves current user data back into multi-user JSON storage."""
    data = load_data() or {"users": {}}
    if "users" not in data:
        data = {"users": {}}
    data["users"][user["username"]] = user
    save_data(data)

def add_new_subscription(user, name, cost, cycle, category, renewal_date):
    sub = create_subscription(name, cost, cycle, category, renewal_date)
    add_subscription(user, sub)
    _sync_user_to_db(user)
    print(f"'{name}' added successfully")

def view_subscriptions(user):
    subs = user.get("subscriptions", [])
    owner = user.get("username", "User")
    print(f"\n--- {owner}'s Subscriptions ---")
    if not subs:
        print("No subscriptions found.")
        return
    for i, sub in enumerate(subs, 1):
        print(f"{i}. {format_subscription(sub)}")

def delete_subscription(user, name):
    removed = remove_subscription(user, name)
    if removed:
        _sync_user_to_db(user)
        print(f"'{name}' deleted successfully.")
    else:
        print(f"Subscription '{name}' not found.")

def calculate_total_expenses(user):
    subs = user.get("subscriptions", [])
    monthly_total = 0.0
    yearly_total = 0.0

    for sub in subs:
        cost = float(sub.get("cost", 0.0))
        cycle = str(sub.get("cycle", "monthly")).lower()

        if cycle == "monthly":
            monthly_total += cost
            yearly_total += cost * 12
        elif cycle == "yearly":
            yearly_total += cost
            monthly_total += cost / 12

    print("\n--- Financial Summary ---")
    print(f"Total Monthly Cost: Rs. {monthly_total:.2f}")
    print(f"Total Yearly Cost:  Rs. {yearly_total:.2f}")