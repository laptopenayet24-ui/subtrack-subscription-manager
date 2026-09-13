import json
filename = "subscriptions_data.json"

def save_data(data: dict):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
#----------------------------------------------------------------------------------------------------------------------------------------
def load_data():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"username": "Default User", "subscriptions": []}
#-------------------------------------------------------------------