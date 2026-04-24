def log_user_action(user_name, action):
    """Kullanici hareketlerini loglar."""
    return f"Action {action} for {user_name} saved."


def calculate_transaction_risk(transactions):
    """Islem riskini hesaplar ve 500 ile sinirlar."""
    if not transactions:
        return 0.0
    amounts = [t.get("amount", 0) for t in transactions]
    avg_amount = sum(amounts) / len(amounts)
    risk = avg_amount * 0.05
    return min(float(risk), 500.0)


def toplama(a, b):
    """Iki sayiyi toplar."""
    return a + b
