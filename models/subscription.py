def create_subscription(name: str, cost: float, cycle: str, category: str, renewal_date: str) -> dict:
    """Creates and returns a subscription dictionary."""
    return {
        "name": name,
        "cost": float(cost),
        "cycle": cycle,
        "category": category,
        "renewal_date": renewal_date
    }

def format_subscription(sub: dict) -> str:
    """Formats a subscription dictionary into a clean readable string."""
    name = sub.get("name", "Unknown")
    cost = sub.get("cost", 0.0)
    cycle = sub.get("cycle", "monthly")
    category = sub.get("category", "General")
    
    renewal = "N/A"
    for key, val in sub.items():
        if key.lower().replace(" ", "").replace("_", "") in ["renewaldate", "renewdate", "renewal"]:
            if val:
                renewal = str(val)
                break

    return f"{name} - Rs. {cost:.2f} ({cycle}) | Category: {category} | Renews: {renewal}"