import streamlit as st
import json
import os
from utils.roadmap_generator import generate_roadmap_text
from utils.flowchart_visualizer import generate_flowchart
from langchain_chain import get_recommendations
from quiz_model import run_quiz

# Paths to JSON files
CAREER_DB_PATH = 'database/career_db.json'
USERS_JSON_PATH = 'database/users.json'

st.set_page_config(page_title="AI Career Recommendation System", layout="wide")

# Load career database
@st.cache_data
def load_career_db():
    with open(CAREER_DB_PATH, 'r') as f:
        return json.load(f)

# Load users data
def load_users():
    if not os.path.exists(USERS_JSON_PATH):
        with open(USERS_JSON_PATH, 'w') as f:
            json.dump({"users": []}, f)
    with open(USERS_JSON_PATH, 'r') as f:
        return json.load(f)

# Save users data
def save_user(user_data):
    users = load_users()
    users['users'].append(user_data)
    with open(USERS_JSON_PATH, 'w') as f:
        json.dump(users, f, indent=4)

career_db = load_career_db()

st.title("🎓 AI Career Recommendation System")

with st.form("user_input_form"):
    st.header("Step 1: Enter Your Details")

    name = st.text_input("Your Name")
    education_level = st.selectbox("Select your current academic stage:", options=list(career_db.keys()))
    subjects = st.multiselect("Subjects you like", options=[
        "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "English", "Economics", "History", "Geography"
    ])
    skills = st.multiselect("Your skills or hobbies", options=[
        "Coding", "Communication", "Creativity", "Problem Solving", "Leadership", "Teamwork", "Drawing", "Writing", "Sports"
    ])
    future_goals = st.text_area("Your future goals (optional)")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Details submitted successfully!")
    
    # Step 2: Optional Career Interest Quiz
    if st.checkbox("Take a short career interest quiz?"):
        quiz_result = run_quiz()
        st.info(f"Quiz Result: {quiz_result}")
    else:
        quiz_result = None

    # Step 3: Show possible education paths from current stage
    paths = career_db.get(education_level, {}).get('paths', {})
    if not paths:
        st.warning("No education paths found for your selected academic stage.")
    else:
        st.header("Step 3: Choose an education path")
        selected_path = st.radio("Available Paths", options=list(paths.keys()))
        
        # Step 4: Show next-level career options for selected path
        st.header("Step 4: Career options for your chosen path")
        careers = career_db.get(selected_path, {}).get('careers', {})
        if not careers:
            st.info("No specific careers data found for this path yet.")
            career_options = []
        else:
            career_options = list(careers.keys())
            selected_career = st.selectbox("Select a career option", options=career_options)

            # Step 5: AI Recommendation based on user inputs and quiz
            st.header("Step 5: AI Recommended Careers")
            user_profile = {
                "name": name,
                "education": education_level,
                "interests": subjects,
                "skills": skills,
                "quiz_result": quiz_result or "",
                "selected_path": selected_path
            }
            recommendation_text = get_recommendations(user_profile)
            st.write(recommendation_text)

            # Step 6: Show roadmap visualization
            st.header("Career Roadmap Visualization")
            roadmap_text = generate_roadmap_text(education_level, selected_path, selected_career, careers[selected_career])
            st.text(roadmap_text)

            graph = generate_flowchart(education_level, selected_path, careers)
            st.graphviz_chart(graph)

            # Step 7: Save user data
            if st.button("Save my Career Profile"):
                user_data = {
                    "name": name,
                    "education_level": education_level,
                    "interests": subjects,
                    "skills": skills,
                    "quiz_result": quiz_result or "",
                    "selected_path": selected_path,
                    "recommended_careers": career_options
                }
                save_user(user_data)
                st.success("Your career profile has been saved!")
