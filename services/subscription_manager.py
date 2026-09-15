from data.file_handler import load_data, save_data
from models.user import create_user, add_subscription, remove_subscription
from models.subscription import create_subscription, format_subscription

def initialize_app(username="Default User"):
    data = load_data()
    if not data:
        user = create_user(username)
        save_data(user)
        return user
    
    if username and username.strip():
        data["username"] = username.strip()
        save_data(data)
        
    return data

def add_new_subscription(user, name, cost, cycle, category, renewal_date):
    sub = create_subscription(name, cost, cycle, category, renewal_date)
    add_subscription(user, sub)
    save_data(user)
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
        save_data(user)
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
    print(f"Total Monthly Cost: Rs{monthly_total:.2f}")
    print(f"Total Yearly Cost:  Rs{yearly_total:.2f}")