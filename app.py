import streamlit as st
import json
import os
from dotenv import load_dotenv

from utils.roadmap_generator import generate_roadmap_text
from utils.flowchart_visualizer import generate_flowchart
from langchain_chain import get_recommendations
from quiz_model import run_quiz

# Load environment variables
load_dotenv()

# File paths
CAREER_DB_PATH = "database/career_db.json"
USERS_JSON_PATH = "database/users.json"

# Load career database
def load_career_db():
    with open(CAREER_DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Save user data to JSON
def save_user_data(user_data):
    if not os.path.exists(USERS_JSON_PATH):
        with open(USERS_JSON_PATH, "w") as f:
            json.dump([], f)

    with open(USERS_JSON_PATH, "r+") as f:
        try:
            existing = json.load(f)
        except:
            existing = []
        existing.append(user_data)
        f.seek(0)
        json.dump(existing, f, indent=2)

# Load data
career_db = load_career_db()

# Streamlit UI setup
st.set_page_config(page_title="AI Career Recommendation", layout="wide")
st.title("🎓 AI-Powered Career Recommendation System")

st.header("Step 1: Enter Your Details")
with st.form("user_form"):
    name = st.text_input("Your Name")
    education_level = st.selectbox("Current Education Level", options=["10th"])
    subjects = st.multiselect("Subjects you like", ["Maths", "Physics", "Biology", "Chemistry", "English"])
    skills = st.multiselect("Your Skills / Hobbies", ["Coding", "Drawing", "Communication", "Problem Solving", "Leadership", "Creativity"])
    take_quiz = st.checkbox("Take interest quiz for better results?")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("✔️ Data submitted. Now choose a path below.")

    st.session_state["user_data"] = {
        "name": name,
        "education": education_level,
        "interests": subjects,
        "skills": skills
    }

# Stop here if no user data yet
if "user_data" not in st.session_state:
    st.stop()

user_data = st.session_state["user_data"]

# Step 2: Show available paths
st.header("Step 2: Choose an Education Path")
available_paths = career_db.get("10th", {}).get("paths", {})

if not available_paths:
    st.error("❌ No paths found in database for this education level.")
    st.stop()

selected_path = st.selectbox("Available Options", list(available_paths.keys()))
st.session_state["selected_path"] = selected_path

# Step 3: Show career options for selected path
st.header("Step 3: Explore Career Options")

career_options = career_db.get(selected_path, {}).get("careers", {})

if not career_options:
    st.warning("⚠️ No career data found for this path in the database.")
    st.stop()

selected_career = st.selectbox("Select a Career", list(career_options.keys()))
career_data = career_options.get(selected_career)

# Step 4: Show AI recommendations
st.header("Step 4: AI Career Recommendation")

if take_quiz:
    quiz_result = run_quiz()
    user_data["quiz_result"] = quiz_result
else:
    user_data["quiz_result"] = "Not specified"

user_data["selected_path"] = selected_path

recommendation = get_recommendations(user_data)
st.write(recommendation)

# Step 5: Show roadmap
st.header("Step 5: Career Roadmap")
roadmap_text = generate_roadmap_text(
    current_stage=user_data["education"],
    path=selected_path,
    selected_career=selected_career,
    career_data=career_data
)
st.text_area("Career Roadmap", roadmap_text, height=250)

# Step 6: Flowchart Visualization
st.header("Step 6: Visual Flowchart")
st.graphviz_chart(generate_flowchart(user_data["education"], selected_path, career_options))

# Step 7: Save Option
if st.button("💾 Save Career Plan"):
    save_user_data({
        "user": user_data,
        "selected_career": selected_career,
        "roadmap": roadmap_text,
        "recommendation": recommendation
    })
    st.success("Profile saved successfully!")
