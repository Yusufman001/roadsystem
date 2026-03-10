# ===============================================
# SMART ROAD DAMAGE DETECTION & MANAGEMENT SYSTEM
# ===============================================

import requests
import urllib.parse
import streamlit as st
from ultralytics import YOLO
import tempfile
import os
import cv2
import pandas as pd
from datetime import datetime
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import seaborn as sns
from folium.plugins import HeatMap

# ===============================================
# PAGE CONFIG
# ===============================================

st.set_page_config(
    page_title="AI Road Damage Management",
    layout="wide"
)

st.title("🛣 AI Road Damage Detection & Monitoring System")
st.caption("Detection • Mapping • Alerts • Infrastructure Analytics")

# ===============================================
# LOAD MODEL
# ===============================================

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ===============================================
# SESSION STATE
# ===============================================

if "df" not in st.session_state:
    st.session_state.df = None

if "img" not in st.session_state:
    st.session_state.img = None

# ===============================================
# AUTO GPS LOCATION
# ===============================================

def get_location():

    try:
        response = requests.get("https://ipinfo.io/json").json()

        loc = response.get("loc")
        city = response.get("city")
        region = response.get("region")
        country = response.get("country")

        lat, lon = loc.split(",")

        return float(lat), float(lon), f"{city}, {region}, {country}"

    except:
        return -1.0, 36.0, "Unknown Location"


lat, lon, location_name = get_location()

# ===============================================
# STREET NAME (REVERSE GEOCODING)
# ===============================================

def get_street_name(lat, lon):

    try:

        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"

        headers = {"User-Agent":"road-damage-system"}

        data = requests.get(url, headers=headers).json()

        address = data.get("address", {})

        road = address.get("road","Unknown Road")
        suburb = address.get("suburb","")
        city = address.get("city","")

        return f"{road}, {suburb}, {city}"

    except:
        return "Unknown Street"


street_name = get_street_name(lat, lon)

# ===============================================
# SIDEBAR SETTINGS
# ===============================================

st.sidebar.header("⚙ System Settings")

confidence = st.sidebar.slider(
    "Detection Confidence",
    0.1,0.9,0.3,0.05
)

enable_camera = st.sidebar.toggle("Enable Camera Capture")

st.sidebar.subheader("📍 Location")

st.sidebar.write(f"Latitude: {lat}")
st.sidebar.write(f"Longitude: {lon}")
st.sidebar.write(f"Area: {location_name}")
st.sidebar.write(f"Street: {street_name}")

# ===============================================
# DAMAGE SEVERITY LOGIC
# ===============================================

def severity(area):

    if area < 5000:
        return "Low"

    if area < 20000:
        return "Medium"

    return "High"

# ===============================================
# WHATSAPP ALERT BUTTON
# ===============================================

def whatsapp_button(message):

    phone = "254707558206"

    encoded = urllib.parse.quote(message)

    link = f"https://wa.me/{phone}?text={encoded}"

    st.markdown(
        f"""
        <a href="{link}" target="_blank">
        <button style="
        background-color:#25D366;
        color:white;
        padding:14px 28px;
        border:none;
        border-radius:10px;
        font-size:18px;
        cursor:pointer;">
        📲 Send Alert via WhatsApp
        </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# ===============================================
# MAP DISPLAY
# ===============================================

def show_damage_map(df):

    m = folium.Map(
        location=[lat, lon],
        zoom_start=15
    )

    for _, row in df.iterrows():

        popup = f"""
        <b>Damage:</b> {row['damage']}<br>
        <b>Severity:</b> {row['severity']}<br>
        <b>Street:</b> {street_name}<br>
        <b>Time:</b> {row['time']}
        """

        color = "green"

        if row["severity"] == "Medium":
            color = "orange"

        if row["severity"] == "High":
            color = "red"

        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=popup,
            icon=folium.Icon(color=color)
        ).add_to(m)

    st_folium(m, width=1000, height=500)

# ===============================================
# ANALYTICS FUNCTIONS
# ===============================================

def damage_distribution_chart(df):

    fig, ax = plt.subplots()

    df["damage"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Damage Type Distribution")

    st.pyplot(fig)

def severity_chart(df):

    fig, ax = plt.subplots()

    df["severity"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_title("Damage Severity")

    st.pyplot(fig)

def road_health_score(df):

    high = (df["severity"]=="High").sum()
    medium = (df["severity"]=="Medium").sum()

    score = max(0, 100 - (high*10 + medium*5))

    return score

# ===============================================
# TABS
# ===============================================

tab1, tab2, tab3 = st.tabs([
    "🔍 Detection",
    "📄 Reports",
    "📊 Analytics"
])

# ===============================================
# DETECTION TAB
# ===============================================

with tab1:

    st.subheader("Input Source")

    src = st.radio(
        "Choose Input",
        ["Upload Image"] + (["Camera"] if enable_camera else []),
        horizontal=True
    )

    file=None

    if src=="Upload Image":
        file = st.file_uploader(
            "Upload Road Image",
            type=["jpg","png","jpeg"]
        )

    if src=="Camera":
        file = st.camera_input("Capture Image")

    run_btn = st.button("🚀 Run Detection", use_container_width=True)

    if run_btn and file:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:

            tmp.write(file.read())

            path = tmp.name

        with st.spinner("Running AI Detection..."):

            results = model.predict(path, conf=confidence)[0]

        boxes = results.boxes.xyxy.cpu().numpy()
        clss = results.boxes.cls.cpu().numpy()

        rows=[]

        for b,c in zip(boxes,clss):

            x1,y1,x2,y2 = b

            area = (x2-x1)*(y2-y1)

            rows.append({
                "damage":model.names[int(c)],
                "severity":severity(area),
                "area":int(area),
                "lat":lat,
                "lon":lon,
                "time":datetime.now()
            })

        df = pd.DataFrame(rows)

        st.session_state.df = df
        st.session_state.img = cv2.cvtColor(
            results.plot(),
            cv2.COLOR_BGR2RGB
        )

        os.remove(path)

# ===============================================
# RESULTS PANEL
# ===============================================

    if st.session_state.df is not None:

        df = st.session_state.df

        st.divider()

        st.subheader("Detection Dashboard")

        c1,c2,c3,c4 = st.columns(4)

        c1.metric("Damages", len(df))
        c2.metric("High Severity",(df.severity=="High").sum())
        c3.metric("Potholes",(df.damage=="D40").sum())

        score = road_health_score(df)

        c4.metric("Road Health Score",score)

        st.progress(score/100)

        st.image(st.session_state.img)

        st.dataframe(df)

        message = f"""
Road Damage Detected

Location: {street_name}

High Severity: {(df.severity=='High').sum()}

Total Damage: {len(df)}
"""

        whatsapp_button(message)

        st.subheader("🗺 Damage Map")

        show_damage_map(df)

# ===============================================
# REPORTS TAB
# ===============================================

with tab2:

    st.subheader("Inspection Reports")

    if st.session_state.df is None:

        st.info("Run detection first")

    else:

        df = st.session_state.df

        col1,col2 = st.columns(2)

        if col1.button("💾 Save Inspection Log"):

            if os.path.exists("inspection_log.csv"):

                df.to_csv(
                    "inspection_log.csv",
                    mode="a",
                    header=False,
                    index=False
                )

            else:

                df.to_csv(
                    "inspection_log.csv",
                    index=False
                )

            st.success("Inspection Saved")

        col2.download_button(

            "📄 Download CSV Report",

            df.to_csv(index=False),

            "inspection_report.csv"
        )

# ===============================================
# ANALYTICS TAB
# ===============================================

with tab3:

    st.subheader("Infrastructure Analytics")

    if os.path.exists("inspection_log.csv"):

        hist = pd.read_csv("inspection_log.csv")

        st.dataframe(hist)

        col1,col2 = st.columns(2)

        with col1:
            damage_distribution_chart(hist)

        with col2:
            severity_chart(hist)

        st.subheader("Road Damage Heatmap")

        m = folium.Map(
            location=[lat,lon],
            zoom_start=13
        )

        heat_data = [
            [row["lat"],row["lon"]]
            for _,row in hist.iterrows()
        ]

        HeatMap(heat_data).add_to(m)

        st_folium(m,width=1000,height=500)

    else:

        st.info("No inspection history yet")