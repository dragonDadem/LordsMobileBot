# Lords Mobile Automation Bot (Professional Grade)

A modular, fault-tolerant automation framework for Lords Mobile on LDPlayer. Designed for long-running autonomous farming with human-like behavior.

## 🚀 Key Features

- **Adaptive Spiral Scanning:** Systematic world map search starting from the center.
- **Intelligent Resource Detection:** OpenCV-powered multi-scale template matching (Levels 1-5).
- **Persistent Timer System:** SQLite-backed task tracking that survives crashes.
- **Anti-Detection (Humanization):** Randomized delays, jittered clicks, and natural break patterns.
- **Modern Dashboard:** Real-time PyQt6 interface with live event logging and task monitoring.
- **High Performance:** Optimized Win32 API screen capture for minimal latency.

## 📂 Project Structure

- `core/`: Logging and core utilities.
- `emulator/`: LDPlayer window management and ADB integration.
- `vision/`: Screen capture and resource detection engine.
- `scanner/`: Spiral navigation algorithms.
- `dispatch/`: Army management and click sequences.
- `storage/`: SQLite database and persistent state.
- `safety/`: Humanization and anti-ban logic.
- `ui/`: PyQt6 dashboard.
- `assets/templates/`: Place your resource icons here.

## 🛠 Setup & Requirements

1. **Emulator Settings:**
   - Use **LDPlayer**.
   - Set resolution to **1600x900**.
   - Enable **ADB** in settings.

2. **Installation:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Resource Templates:**
   - Capture small icons of resources from the map.
   - Save to `assets/templates/` as `Gold_lv5.png`, `Wood_lv4.png`, etc.

4. **Coordinates:**
   - Update button coordinates in `dispatch/manager.py` to match your screen layout.

## 🚦 How to Run

```bash
python main.py
```

## 🛡 Safety Warning
This bot includes humanization features, but automation always carries risks. Use responsibly.
