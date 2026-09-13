from secrets import choice

from services.subscription_manager import ( initialize_app,add_new_subscription,view_subscriptions,delete_subscription,calculate_total_expenses)

def main():
    print("Welcome to SubTrack Subscription Manager")
    user = initialize_app()
    
    while True:
        print("--- Menu ---")
        print("1. View Subscriptions")
        print("2. Add Subscription")
        print("3. Delete Subscription")
        print("4. View Financial Summary")
        print("5. Exit")
        
        c = input("Enter your choice: ").strip()
        if c == "1":
            view_subscriptions(user)
        elif c == "2":
            name = input("Enter subscription name: ").strip()
            try:
                cost = float(input("Enter cost : ").strip())
            except ValueError:
                print("Invalid cost format. Please enter a numeric value.")
                continue
            cycle = input("Enter cycle monthly or yearly: ").strip()
            category = input("Enter category  Entertainment, Work: ").strip()
            renewal_date = input("Enter renewal date DD-MM-YYYY: ").strip()
            
            add_new_subscription(user, name, cost, cycle, category, renewal_date)
            
        elif c == "3":
            view_subscriptions(user)
            name = input("Enter the name of the subscription to delete: ").strip()
            delete_subscription(user, name)
            
        elif c == "4":
            calculate_total_expenses(user)
            
        elif c == "5":
            print("Exiting the program ")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()