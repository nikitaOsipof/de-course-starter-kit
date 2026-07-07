import os
import json
import random
from datetime import datetime, timedelta

def create_fixtures():
    os.makedirs("data_samples", exist_ok=True)
    start_time = datetime(2026, 7, 5, 12, 0, 0)
    
    # Логи для ЛР 2
    log_levels = ["INFO", "DEBUG", "WARNING", "ERROR"]
    messages = {"INFO": "Login success", "DEBUG": "Pool size: 10", "WARNING": "High RAM usage", "ERROR": "DB timeout"}
    with open("data_samples/app_logs.txt", "w", encoding="utf-8") as f:
        for i in range(100):
            if i % 15 == 0: f.write("\n"); continue
            level = random.choice(log_levels)
            t = (start_time + timedelta(seconds=i*15)).strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{t}|{level}|{messages[level]}\n")
            
    # Заказы для ЛР 4
    orders = []
    for i in range(1, 21):
        amount = -50.0 if i % 10 == 0 else round(random.uniform(10.0, 500.0), 2)
        status = "bad_status" if i % 7 == 0 else random.choice(["new", "processing", "done"])
        orders.append({"id": 1000+i, "timestamp": (start_time + timedelta(minutes=i)).isoformat(), "status": status, "amount": amount})
    with open("data_samples/raw_orders.json", "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4)
    print("[Успех] Файлы данных успешно сгенерированы в data_samples/")

if __name__ == "__main__":
    create_fixtures()
