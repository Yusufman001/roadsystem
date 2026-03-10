# 🛣️ AI-Based Road Damage Detection & Monitoring System (YOLOv8 + Streamlit)

Author: **Yusuf**

---

# 📌 Project Overview

This project is an **AI-powered Road Infrastructure Monitoring System** designed to detect road damage such as potholes and cracks using **YOLOv8 object detection**. The system allows road authorities, municipalities, and infrastructure agencies to monitor road conditions, generate reports, and prioritize repairs.

The platform integrates **computer vision, geolocation, analytics dashboards, and notification systems** to provide a modern **Smart City road maintenance solution**.

---

# 🚀 Key Features

## 1️⃣ AI Road Damage Detection

* Detects road damages using **YOLOv8**
* Supports:

  * Images
  * Videos
  * Optional Live Camera

### Damage Classes

* **D00 – Longitudinal Crack**
* **D10 – Transverse Crack**
* **D20 – Alligator Crack**
* **D40 – Pothole**

---

## 2️⃣ Real-Time Monitoring

Optional **webcam monitoring** for detecting road damage in real time.

---

## 3️⃣ Inspection Logging System

Stores inspections including:

* Damage type
* Severity
* Area size
* GPS coordinates
* Street name
* Timestamp

Stored using an **SQLite database**.

---

## 4️⃣ Government Infrastructure Dashboard

Provides monitoring metrics including:

* Total inspections
* Number of potholes detected
* High severity damage alerts
* Infrastructure health score
* Inspection records

---

## 5️⃣ Road Damage Heatmap

Displays detected road damages on an **interactive map** using:

* Folium
* Geolocation coordinates
* Heatmap visualization

---

## 6️⃣ Pothole Hotspot Detection

Uses **DBSCAN clustering** to identify areas with repeated road damage occurrences.

This helps authorities detect **critical road sections needing urgent repair**.

---

## 7️⃣ Repair Priority Ranking

Road repair priority is calculated based on the number of detected damages per road.

Example:

| Street    | Damage Count |
| --------- | ------------ |
| Highway A | 25           |
| Main Road | 18           |
| City Road | 12           |

---

## 8️⃣ Damage Trend Analytics

Displays trends of road damage over time using line charts.

Helps answer:

* Are potholes increasing?
* Which months have the most road damage?

---

## 9️⃣ WhatsApp Notification System

When severe damage is detected, the system can notify management via **WhatsApp redirect link** with:

* Damage image
* GPS location
* Severity level

---

# 🧠 System Architecture

```
User Upload / Camera
        │
        ▼
 YOLOv8 Detection Model
        │
        ▼
 Damage Classification
        │
        ▼
 Data Processing Layer
        │
        ├── SQLite Database
        ├── CSV Reports
        ├── Heatmap Generation
        └── Hotspot Clustering
        │
        ▼
 Streamlit Web Dashboard
        │
        ├── Detection Interface
        ├── Analytics Dashboard
        ├── Government Monitoring Panel
        └── Reporting System
```

---

# 💻 Local Installation & Setup Guide

Follow the steps below to install and run the system locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/road-damage-detection.git
cd road-damage-detection
```

Alternatively, download the **ZIP file** and extract it to your **Desktop**.

---

## 2️⃣ Install Python

Ensure **Python 3.9 – 3.11** is installed.

Check installation:

```bash
python --version
```

Download Python if needed:

https://www.python.org/downloads/

---

## 3️⃣ Install Visual Studio Code (Recommended)

Download VS Code:

https://code.visualstudio.com/

Recommended extensions:

* Python
* Pylance

---

## 4️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

If PowerShell blocks activation:

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 5️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

If requirements file is missing:

```bash
pip install streamlit ultralytics opencv-python pandas matplotlib folium scikit-learn streamlit-folium
```

---

## 6️⃣ Place the Trained YOLO Model

Ensure the trained model file exists in the project folder:

```
best.pt
```

Example structure:

```
road-damage-system
│
├── app.py
├── best.pt
├── requirements.txt
```

---

## 7️⃣ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## 8️⃣ Open the System in Your Browser

If it does not open automatically, go to:

```
http://localhost:8501
```

---

## 9️⃣ Using the System

Once running, the system allows you to:

* Upload **road images**
* Upload **road videos**
* Use **live camera detection**
* Generate **inspection reports**
* View **damage heatmaps**
* Send **WhatsApp alerts**
* Analyze **road repair priorities**

---

# 📂 Example Project Structure

```
road-damage-system/
│
├── app.py
├── best.pt
├── requirements.txt
├── road_damage.db
│
├── datasets/
│   ├── images/
│   └── labels/
│
├── reports/
│   └── inspection_reports.csv
│
└── README.md
```

---

# ⚠️ Troubleshooting

### Streamlit Not Found

```bash
pip install streamlit
```

### Camera Not Working

```bash
pip install opencv-python
```

### Map Not Loading

```bash
pip install folium streamlit-folium
```

---

# 📊 Example Use Cases

* Smart City Infrastructure Monitoring
* Municipal Road Maintenance
* Transportation Authority Inspection Systems
* AI-based Road Condition Monitoring

---

# 👨‍💻 Author

**Yusuf**
AI Road Infrastructure Monitoring System
