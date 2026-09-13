def create_user(username = "Default User"):
    return {"username": username,"subscriptions": []  }
#-------------------------------------------------------------------
def add_subscription(user, subscription) :
    user["subscriptions"].append(subscription)
#-------------------------------------------------------------------
def remove_subscription(user, name):
    for sub in user["subscriptions"]:
        if sub["name"].lower() == name.lower():
            user["subscriptions"].remove(sub)
            return True
    return False
#-------------------------------------------------------------------
