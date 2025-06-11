# app.py
import streamlit as st
import pandas as pd
import datetime
from model import train_model
from suggestions import get_suggestions
import os

st.set_page_config(page_title="AI Habit Tracker", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
        body, .main {
            background-color: #000000;
            color: white;
        }
        .stApp {
            background-color: #000000;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, .css-1v3fvcr {
            color: white !important;
        }
        .footer-note {
            position: fixed;
            bottom: 10px;
            right: 20px;
            font-size: 16px;
            color: #888;
        }
    </style>
    <div class="footer-note">Done by Jyothsna Nageswari</div>
""", unsafe_allow_html=True)

# --- Project Info ---
st.title("🌱 AI Habit Tracker with Smart Suggestions")

st.markdown("""
This project helps users track their daily habits and receive personalized suggestions to improve well-being using AI.

**Technologies Used:**
- Python 🐍
- Streamlit 📊
- Scikit-learn 🤖
- Pandas 🧮

**Features:**
- Track water intake, sleep, screen time, and workouts
- Visualize your habits over time
- Get AI-generated habit improvement suggestions
""")

# --- Load or Create Data ---
if not os.path.exists("data.csv"):
    df = pd.DataFrame(columns=["date", "water_intake", "sleep_hours", "screen_time", "workout_done"])
    df.to_csv("data.csv", index=False)

# Read the data
df = pd.read_csv("data.csv")

# --- Input Section ---
st.subheader("📋 Enter Today’s Habits")

with st.form("habit_form"):
    date = st.date_input("Date", datetime.date.today())
    water = st.slider("Water Intake (Litres)", 0.0, 5.0, 2.0)
    sleep = st.slider("Sleep Duration (Hours)", 0.0, 12.0, 7.0)
    screen = st.slider("Screen Time (Hours)", 0.0, 12.0, 4.0)
    workout = st.selectbox("Workout Done?", ["yes", "no"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        new_entry = {
            "date": date,
            "water_intake": water,
            "sleep_hours": sleep,
            "screen_time": screen,
            "workout_done": workout
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv("data.csv", index=False)
        st.success("✅ Data recorded successfully!")

# --- Visualize Data ---
st.subheader("📈 Your Habit Trends")
if not df.empty:
    st.line_chart(df[["water_intake", "sleep_hours", "screen_time"]])
else:
    st.info("No data available to display trends yet.")

# --- AI Suggestion ---
st.subheader("🧠 AI Smart Suggestion")
if len(df) >= 5:
    model = train_model(df)
    latest = df.iloc[-1][["water_intake", "sleep_hours", "screen_time"]].values.reshape(1, -1)
    prediction = model.predict(latest)[0]
    suggestions = get_suggestions(*latest[0])
    st.markdown("### 💡 Suggestions:")
    for s in suggestions:
        st.write("-", s)
else:
    st.info("Add at least 5 entries to activate AI-based suggestions.")
