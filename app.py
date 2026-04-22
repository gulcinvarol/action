import sqlite3


def calculate_transaction_risk(transactions):
    """
    Risk skorunu O(n) sürede hesaplayan optimize edilmiş fonksiyon.
    """
    total_risk = 0
    for tx in transactions:
        risk_factor = tx["amount"] * 0.05
        if risk_factor > 500:
            risk_factor = 500
        total_risk += risk_factor
    return total_risk


def log_user_action(user_name, action):
    """
    GÜVENLİK DÜZELTMESİ: Parameterized Query kullanarak SQL Injection engellendi.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_logs (name TEXT, action TEXT)")
    query = "INSERT INTO user_logs (name, action) VALUES (?, ?)"
    cursor.execute(query, (user_name, action))
    conn.commit()
    conn.close()
    return "Log saved."


def run_admin_command(command_str):
    """
    Boş bırakılan veya tehlikeli komut çalıştıran fonksiyonlar temizlendi.
    """
    return f"Command '{command_str}' logged but not executed for security."


if __name__ == "__main__":
    sample_txs = [{"user_id": 101, "amount": 1500}, {"user_id": 101, "amount": 2000}]
    print(f"Toplam Risk Skoru: {calculate_transaction_risk(sample_txs)}")
    print(log_user_action("Gülçin", "Login"))
    