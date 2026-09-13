def create_subscription(name, cost, cycle, category, renewal_date):
    return {"name": name,"cost": cost,"cycle": cycle,"category": category,"renewal_date": renewal_date}

def format_subscription(sub):
    name = sub.get("name", "Unknown")
    cost = sub.get("cost", 0.0)
    cycle = sub.get("cycle", "monthly")
    category = sub.get("category", "General")
    renewal = sub.get("Renewal Date", "N/A")
    
    return f"{name} - ${cost:.2f} ({cycle}) | Category: {category} | Renews: {renewal}"