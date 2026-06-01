import uuid
import random
import csv
import os

def generate_order_data(file_path, num_records=1000000):
    print(f"[PROCESS] Generating {num_records} records to {file_path}...")
    tenants = ['tenant_a', 'tenant_b', 'tenant_c']
    
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['order_id', 'tenant_id', 'amount', 'timestamp'])
        for _ in range(num_records):
            writer.writerow([
                str(uuid.uuid4()),
                random.choice(tenants),
                round(random.uniform(10.0, 5000.0), 2),
                "2024-01-01 10:00:00"
            ])
    print(f"[SUCCESS] Data generation complete.")

if __name__ == "__main__":
    os.makedirs("/home/yoonwoodev/googleAI_/plan_A/data", exist_ok=True)
    generate_order_data("/home/yoonwoodev/googleAI_/plan_A/data/heavy_orders.csv")