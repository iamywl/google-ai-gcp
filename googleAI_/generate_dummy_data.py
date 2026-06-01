import pandas as pd
import uuid
from datetime import datetime, timedelta
import random
import os

def generate_data(file_path="/home/yoonwoodev/plan_A/dummy_logs.csv", n=100):
    depts = ["Sales", "Purchase", "Legal", "Finance", "Management"]
    actions = ["Request", "Approve", "Reject", "Comment"]
    
    data = []
    for _ in range(n):
        data.append({
            "id": str(uuid.uuid4()),
            "department_from": random.choice(depts),
            "department_to": random.choice(depts),
            "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 720))).isoformat(),
            "action": random.choice(actions)
        })
    
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"Successfully generated dummy data at {file_path}")

if __name__ == "__main__":
    generate_data()