# 🛣️ Smart Road Damage Detection & Monitoring System (YOLOv8 + Streamlit)

Author: **Najib**

## 📌 Project Overview
This project is an **AI-powered Road Infrastructure Monitoring System** designed to detect road damage such as potholes and cracks using **YOLOv8 object detection**. The system allows road authorities, municipalities, and infrastructure agencies to monitor road conditions, generate reports, and prioritize repairs.

The platform integrates **computer vision, geolocation, analytics dashboards, and notification systems** to provide a modern **Smart City road maintenance solution**.

---

# 🚀 Key Features

## 1️⃣ AI Road Damage Detection
- Detects road damages using **YOLOv8**
- Supports:
  - Images
  - Videos
  - Optional Live Camera

Damage classes detected:

- **D00 – Longitudinal Crack**
- **D10 – Transverse Crack**
- **D20 – Alligator Crack**
- **D40 – Pothole**

---

## 2️⃣ Real-Time Monitoring
Optional **webcam monitoring** for detecting road damage in real time.

---

## 3️⃣ Inspection Logging System
Stores inspections including:

- Damage type
- Severity
- Area size
- GPS coordinates
- Street name
- Timestamp

Stored using **SQLite database**.

---

## 4️⃣ Government Infrastructure Dashboard
Provides monitoring metrics including:

- Total inspections
- Number of potholes detected
- High severity damage alerts
- Infrastructure health score
- Inspection records

---

## 5️⃣ Road Damage Heatmap
Displays detected road damages on an **interactive map** using:

- Folium
- Geolocation coordinates
- Heatmap visualization

---

## 6️⃣ Pothole Hotspot Detection
Uses **DBSCAN clustering** to identify areas with repeated road damage occurrences.

Helps authorities detect **critical road sections needing urgent repair**.

---

## 7️⃣ Repair Priority Ranking
Road repair priority is calculated based on the number of detected damages per road.

Example:

| Street | Damage Count |
|------|------|
| Highway A | 25 |
| Main Road | 18 |
| City Road | 12 |

---

## 8️⃣ Damage Trend Analytics
Displays trends of road damage over time using line charts.

Helps answer:

- Are potholes increasing?
- Which months have the most road damage?

---

## 9️⃣ WhatsApp Notification System
When severe damage is detected, the system can notify management via **WhatsApp redirect link** with:

- Damage image
- GPS location
- Severity level

---

# 
