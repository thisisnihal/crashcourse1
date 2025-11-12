import json
import random
import time
from datetime import datetime, timedelta

def generate_log_entry(start_time):
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    services = ["AuthService", "PaymentService", "OrderService", "AnalyticsService", "InventoryService"]
    messages = [
        "User login successful",
        "Payment gateway timeout",
        "Cache miss occurred",
        "Database connection lost",
        "Order created successfully",
        "External API request failed"
    ]

    entry_time = start_time + timedelta(seconds=random.randint(1, 5))
    return {
        "timestamp": entry_time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(levels),
        "message": random.choice(messages),
        "service": random.choice(services)
    }, entry_time

def generate_large_log_file(filename, target_size_mb):
    start_time = datetime.now()
    size_limit = target_size_mb * 1024 * 1024  # MB -> bytes
    current_size = 0

    with open(filename, "w") as f:
        f.write("[\n")
        first = True

        while current_size < size_limit:
            entry, start_time = generate_log_entry(start_time)
            if not first:
                f.write(",\n")
            f.write(json.dumps(entry))
            first = False
            current_size = f.tell()

        f.write("\n]")
    print(f"Finished writing {filename} ({current_size / 1024 / 1024:.2f} MB)")

import os
generate_large_log_file(os.path.join('data', 'logs_50mb.json'), target_size_mb=50)
