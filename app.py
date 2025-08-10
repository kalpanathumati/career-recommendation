import streamlit as st
import json
import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Import internal modules (after utils/__init__.py exists)
from utils.roadmap_generator import generate_roadmap_text
from utils.flowchart_visualizer import generate_flowchart
from langchain_chain import get_recommendations
from quiz_model import run_quiz

# ───────────────────────────────────────────────
# Load Paths
CAREER_DB_PATH = 'database/career_db.json'
USERS_JSON_PATH = 'database/users.json'

# ───────────────────────────────────────────────
# Load career database from JSON
@st.cache_data
def load_career_db():
    with open(CAREER_DB_PATH, 'r') as f:
        return json.load(f)

# Load users
def load_users():
    if not os.path.exists(USERS_JSON_PATH):
        with open(USERS_JSON_PATH, 'w') as f:
            json.dump({"users": []}, f)
    with open(USERS_JSON_PATH, 'r') as f:
        return json.load(f)

# Save user data to JSON
def save_user(user_data):
    users = load_users()
    users['users'].append(user_data)
    with open(USERS_JSON_PATH, 'w') as f:
        json.dump(users, f, indent=4)

# ───────────────────────────────────────────────
# Page Config and Styles
st.set_page_config(page_title="AI Career Recommendation System", layout="wide")

# Optional CSS Styling
if os.path.exists("styles/custom.css"):
    st.markdown(
        f"<style>{open('styles/custom.css').read()}</style>",
        unsafe_allow_html=True
    )

# ───────────────────────────────────────────────
# Main App Interface

career_db = load_career_db()
st.title("🎓 AI Career Recommendation System")

with st.form("user_input_form"):
    st.header("Step 1: Enter Your Details")

    name = st.text_input("Your Name")
    education_level = st.selectbox("Select your current academic stage:", options=list(career_db.keys()))
    
    subjects = st.multiselect("Subjects you like", [
        "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", 
        "English", "Economics", "History", "Geography"
    ])

    skills = st.multiselect("Your skills or hobbies", [
        "Coding", "Communication", "Creativity", "Problem Solving", "Leadership",
        "Teamwork", "Drawing", "Writing", "Sports"
    ])

    future_goals = st.text_area("Your future goals (optional)")

    submitted = st.form_submit_button("Submit")

# ───────────────────────────────────────────────
# After submission
if submitted and name and education_level:
    st.success("✅ Details submitted successfully!")

    quiz_result = None
    if st.checkbox("Take a short career interest quiz?"):
        quiz_result = run_quiz()
        st.info(f"Quiz Result: {quiz_result}")

    # Step 3: Show education paths
    paths = career_db.get(education_level, {}).get('paths', {})
    if not paths:
        st.warning("⚠️ No paths found for this education level.")
    else:
        st.header("Step 2: Choose an Education Path")
        selected_path = st.radio("Available Options", options=list(paths.keys()))

        # Step 4: Career options
        st.header("Step 3: Explore Career Options")
        careers = career_db.get(selected_path, {}).get('careers', {})
        if careers:
            selected_career = st.selectbox("Select a career to explore in detail:", options=list(careers.keys()))
            
            # Step 5: AI Recommendations
            st.header("Step 4: AI Career Recommendations")
            user_profile = {
                "name": name,
                "education": education_level,
                "interests": subjects,
                "skills": skills,
                "quiz_result": quiz_result or "",
                "selected_path": selected_path
            }

            try:
                recommendation_text = get_recommendations(user_profile)
                st.markdown("#### ✨ AI Recommendations")
                st.write(recommendation_text)
            except Exception as e:
                st.error(f"Error from AI model: {e}")

            # Step 6: Roadmap
            st.header("Step 5: Career Roadmap")
            roadmap_text = generate_roadmap_text(education_level, selected_path, selected_career, careers[selected_career])
            st.text_area("Career Roadmap (copy/save):", value=roadmap_text, height=250)

            # Step 7: Flowchart
            st.header("Step 6: Visual Flowchart")
            graph = generate_flowchart(education_level, selected_path, careers)
            st.graphviz_chart(graph)

            # Step 8: Save Profile
            if st.button("💾 Save My Career Profile"):
                user_data = {
                    "name": name,
                    "education_level": education_level,
                    "interests": subjects,
                    "skills": skills,
                    "quiz_result": quiz_result or "",
                    "selected_path": selected_path,
                    "recommended_careers": list(careers.keys())
                }
                save_user(user_data)
                st.success("🎉 Career profile saved successfully!")
        else:
            st.warning("No career data found for this path.")
elif submitted:
    st.warning("Please fill in your name and select an education level.")
