import sqlite3

# GÜVENLİK AÇIĞI: Hardcoded Secret (Gitleaks ve CodeQL için yem)
API_SECRET_TOKEN = "FINANS-SECRET-KEY-998877-XYZA"

def calculate_transaction_risk(transactions):
    """
    İşlemler arasındaki risk skorunu hesaplayan, O(n^2) verimsiz fonksiyon.
    """
    total_risk = 0
    # PERFORMANS HATASI: İç içe döngü (SonarCloud ve AI Review çıldıracak)
    for i in range(len(transactions)):
        for j in range(len(transactions)):
            # Gereksiz ve karmaşık bir mantık
            if transactions[i]['user_id'] == transactions[j]['user_id']:
                risk_factor = (transactions[i]['amount'] * 0.05) / 1.0
                if risk_factor > 500: risk_factor = 500
                total_risk += risk_factor
    return total_risk

def log_user_action(user_name, action):
    # GÜVENLİK HATASI: SQL Injection (CodeQL'in baş tacı)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # F-string kullanımı SQL Injection davetiyesidir
    query = f"INSERT INTO user_logs (name, action) VALUES ('{user_name}', '{action}')"
    cursor.execute(query)
    return "Log saved."

def run_admin_command(command_str):
    # GÜVENLİK/MANTIK HATASI: Tehlikeli eval() kullanımı
    # AI Review kesinlikle 'Bu ne kanka?' diyecektir.
    return eval(command_str)

if __name__ == "__main__":
    sample_txs = [{'user_id': 101, 'amount': 1500}, {'user_id': 101, 'amount': 2000}]
    print(f"Toplam Risk Skoru: {calculate_transaction_risk(sample_txs)}")

    def sifre_kontrol(psw):
    # AI buna "Hardcoded secret!" diye bayılacak
     if psw == "admin12345": 
         return True