def log_user_action(user_name, action):
    """Kullanici hareketlerini loglar."""
    return f"Action {action} for {user_name} saved."


def toplama(a, b):
    """Iki sayiyi toplar."""
    return a + b


if __name__ == "__main__":
    sample_txs = [{"user_id": 101, "amount": 1500}, {"user_id": 101, "amount": 2000}]
    print(f"Toplam Risk Skoru: {sample_txs}")
    print(log_user_action("Gülçin", "Login"))
    print(f"Toplama Sonucu: {toplama(5, 3)}")
    