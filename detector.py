import time
import numpy as np
import joblib
import psutil
import os

# Load the hypersensitive model
model = joblib.load("system_baseline.pkl")
KEYLOG_FILE = "keylogs.txt"
prev_disk = psutil.disk_io_counters().write_bytes

print("DETECTOR ACTIVE: Monitoring for any deviation from Idle...")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        disk_now = psutil.disk_io_counters().write_bytes
        disk_delta = max(0, disk_now - prev_disk)
        prev_disk = disk_now
        
        # Check if log file is being modified
        size_before = os.path.getsize(KEYLOG_FILE) if os.path.exists(KEYLOG_FILE) else 0
        time.sleep(1)
        size_after = os.path.getsize(KEYLOG_FILE) if os.path.exists(KEYLOG_FILE) else 0
        growth = size_after - size_before

        # Model Prediction
        X = [[cpu, disk_delta]]
        is_anomaly = model.predict(X)[0]

        # LOGIC: If the system isn't idle AND the log is growing = Keylogger
        if growth > 0:
            print(f"🚨 ALERT: KEYLOGGING DETECTED!")
        elif is_anomaly == -1:
            # This catches apps opening
            print(f"SYSTEM ACTIVITY DETECTED (Not necessarily a keylogger)")
        else:
            print(f"Status: Idle/Normal", end="\r")
            
except KeyboardInterrupt:
    print("\nDetector stopped.")