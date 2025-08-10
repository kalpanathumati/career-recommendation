import streamlit as st

# Define simple quiz questions with options tied to interest areas
QUIZ_QUESTIONS = [
    {
        "question": "Which activity do you enjoy the most?",
        "options": {
            "Solving puzzles or math problems": "Analytical",
            "Helping and caring for others": "Social",
            "Working with machines or tools": "Technical",
            "Creating art or writing": "Creative"
        }
    },
    {
        "question": "Which subject do you prefer?",
        "options": {
            "Mathematics": "Analytical",
            "Biology": "Social",
            "Physics": "Technical",
            "Literature": "Creative"
        }
    },
    {
        "question": "What kind of work environment do you prefer?",
        "options": {
            "Office with data and reports": "Analytical",
            "Hospitals or community centers": "Social",
            "Workshops or labs": "Technical",
            "Studios or design firms": "Creative"
        }
    }
]

def run_quiz() -> str:
    st.header("Career Interest Quiz")
    scores = {"Analytical": 0, "Social": 0, "Technical": 0, "Creative": 0}

    for i, q in enumerate(QUIZ_QUESTIONS):
        st.write(f"**Q{i+1}: {q['question']}**")
        choice = st.radio("Select one:", options=list(q['options'].keys()), key=f"q{i}")
        scores[q['options'][choice]] += 1

    # Calculate highest scoring interest area
    max_interest = max(scores, key=scores.get)
    st.write(f"Your dominant interest area is: **{max_interest}**")
    return max_interest
