import os, json, random
from datetime import datetime, timedelta
def create_fixtures():
    os.makedirs("data_samples", exist_ok=True)
    start_time = datetime(2026, 7, 5, 12, 0, 0)
    with open("data_samples/app_logs.txt", "w", encoding="utf-8") as f:
        for i in range(100):
            if i % 15 == 0: f.write("\n"); continue
            level = random.choice(["INFO", "DEBUG", "WARNING", "ERROR"])
            t = (start_time + timedelta(seconds=i*15)).strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{t}|{level}|Test message\n")
    orders = [{"id": 1000+i, "timestamp": start_time.isoformat(), "status": "new", "amount": 100.0} for i in range(1, 21)]
    with open("data_samples/raw_orders.json", "w", encoding="utf-8") as f: json.dump(orders, f, indent=4)
    print("[Успех] Файлы данных сгенерированы.")
if __name__ == "__main__": create_fixtures()
