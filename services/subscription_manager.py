from models.subscription import create_subscription, format_subscription
from models.user import create_user, add_subscription, remove_subscription
from data.file_handler import save_data, load_data

def initialize_app():
    data = load_data()
    if not data:
        user = create_user("My Subscriptions")
        save_data(user)
        return user
    return data
#----------------------------------------------------------------------------------------------------------------------------------------
def add_new_subscription(user, name, cost, cycle, category, renewal_date):
    sub = create_subscription(name, cost, cycle, category, renewal_date)
    add_subscription(user, sub)
    save_data(user)
    print(f"'{name}' added successfully")
#----------------------------------------------------------------------------------------------------------------------------------------
def view_subscriptions(user):
    subs = user.get("subscriptions", [])
    if not subs:
        print("\nNo subscriptions found.")
        return
    print("\n--- Your Subscriptions ---")
    for i, sub in enumerate(subs, 1):
        print(f"{i}. {format_subscription(sub)}")
#----------------------------------------------------------------------------------------------------------------------------------------
def delete_subscription(user, name):
    success = remove_subscription(user, name)
    if success:
        save_data(user)
        print(f"Subscription '{name}' deleted successfully.")
    else:
        print(f"Subscription '{name}' not found.")
#----------------------------------------------------------------------------------------------------------------------------------------
def calculate_total_expenses(user: dict):
    subs = user.get("subscriptions", [])
    monthly_total = 0.0
    yearly_total = 0.0
    for sub in subs:
        cost = sub["cost"]
        if sub["cycle"] == "monthly":
            monthly_total += cost
            yearly_total += cost * 12
        elif sub["cycle"] == "yearly":
            yearly_total += cost
            monthly_total += cost / 12
    print(f"Total Monthly Burn Rate: Rs{monthly_total:.2f}")
    print(f"Total Yearly Burn Rate:  Rs{yearly_total:.2f}")
#----------------------------------------------------------------------------------------------------------------------------------------