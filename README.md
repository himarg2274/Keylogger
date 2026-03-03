# 🛡️ Keylogging Attack Simulation with ML-Based Anomaly Detection

This project demonstrates a **controlled and ethical keylogging attack simulation** integrated with **machine learning–based anomaly detection** using Isolation Forest.

The objective is to study keylogging behavior and detect it using runtime system metrics such as CPU usage and disk write activity.

> ⚠️ This project is strictly for educational and defensive cybersecurity research purposes.

---

## 📂 Project Structure
├── keylogger.py # Keylogging attack simulation

├── train_baseline.py # Idle behavior training script

├── detector.py # Real-time anomaly detection

├── keylogs.txt # Captured keystrokes

├── wordlogs.txt # Captured words

├── system.log # Execution logs

├── summary.txt # Simulation summary

├── system_baseline.pkl # Trained Isolation Forest model

---

## ⚙️ Requirements

Install required Python packages:

```bash
pip install pynput psutil scikit-learn numpy joblib
```
🚀 How to Run the Project

Follow the steps in order.

🔹 Step 1: Train the Baseline Model (Idle State)

Before detection, the model must learn normal system behavior.

Run:
```bash
python train_baseline.py
```
⚠️ Important:

Leave the computer completely idle for 30 seconds.

Do NOT type or move the mouse.

After completion, this file will be created:
```bash
system_baseline.pkl
```
This is the trained Isolation Forest model.

🔹 Step 2: Start the Detector

Run:
```bash
python detector.py
```
The detector now continuously monitors:

CPU usage

Disk write activity

Runtime system behavior

🔹 Step 3: Start the Keylogger Simulation

Open another terminal and run:
```bash
python keylogger.py
```
Start typing normally.

🔹 Step 4: Observe Detection

While typing, the detector terminal should display:
```bash
🚨 ML ALERT: Anomalous Behavior Detected!
```
This occurs because:

Keylogger writes continuously to file

Disk write activity increases

System behavior deviates from baseline

Isolation Forest classifies it as anomaly

🧠 How Machine Learning Works Here

This project uses:

Isolation Forest (Unsupervised Anomaly Detection)

Training Phase:

Model learns normal system idle behavior

Features used:

CPU usage (%)

Disk write delta (bytes)

Detection Phase:

Real-time system metrics are collected

Model predicts:

1 → Normal

-1 → Anomaly

Keylogging behavior causes abnormal disk activity, which is detected as an outlier.

🔐 Ethical Considerations

Execution is strictly local

No remote data transmission

Email transfer is disabled by default

Simulation terminates using ESC key

Intended only for cybersecurity education
📊 System Workflow

User Types

↓

Keylogger Captures Input

↓

File Write Activity Increases

↓

Detector Collects CPU + Disk Metrics

↓

Isolation Forest Predicts Anomaly

↓

Alert Generated

🎯 Features

✔ Ethical keylogging simulation

✔ Real-time runtime monitoring

✔ Unsupervised ML detection

✔ Lightweight host-based intrusion detection

✔ No labeled attack data required
