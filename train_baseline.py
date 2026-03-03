import time
import numpy as np
import joblib
import psutil
import os
from sklearn.ensemble import IsolationForest

# Configuration
DURATION = 30  # 30 seconds of PURE IDLE
INTERVAL = 1
KEYLOG_FILE = "keylogs.txt"
features_list = []

print("TRAINING: LEAVE COMPUTER IDLE. Do not touch mouse or keyboard.")

start_time = time.time()
prev_disk = psutil.disk_io_counters().write_bytes

try:
    while time.time() - start_time < DURATION:
        cpu = psutil.cpu_percent(interval=INTERVAL)
        disk_now = psutil.disk_io_counters().write_bytes
        disk_delta = max(0, disk_now - prev_disk)
        prev_disk = disk_now
        
        # We focus on the tiny changes
        features_list.append([cpu, disk_delta])
        print(f"Sampling Idle State: {len(features_list)}/30", end="\r")

    X = np.array(features_list)
    # Very low contamination (0.01) because idle state should be perfect
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    model.fit(X)

    joblib.dump(model, "system_baseline.pkl")
    print("\n✅ Idle Baseline Saved. Now the model will be hypersensitive.")
except KeyboardInterrupt:
    print("\nAborted.")