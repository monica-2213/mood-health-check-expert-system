import streamlit as st

# Define your knowledge base with questions and scoring
knowledge_base = {
    "question_1": {
        "text": "How often have you been feeling down, depressed, or hopeless in the past 2 weeks?",
        "options": {
            "Not at all": 0,
            "Several days": 1,
            "More than half the days": 2,
            "Nearly every day": 3
        }
    },
    "question_2": {
        "text": "Have you experienced a loss of interest or pleasure in doing things that you normally enjoy?",
        "options": {
            "No": 0,
            "Yes": 2
        }
    },
    "question_3": {
        "text": "Have you experienced a significant weight loss or gain?",
        "options": {
            "No": 0,
            "Yes": 2
        }
    },
    "question_4": {
        "text": "Have you experienced trouble sleeping or sleeping too much?",
        "options": {
            "No": 0,
            "Yes": 1
        }
    },
    "question_5": {
        "text": "Have you experienced feelings of worthlessness or excessive guilt?",
        "options": {
            "No": 0,
            "Yes": 2
        }
    },
    "question_6": {
        "text": "Have you experienced difficulty in concentrating or making decisions?",
        "options": {
            "No": 0,
            "Yes": 1
        }
    },
    "result_no_depression": {
        "text": "Based on your responses, it appears that you are not experiencing depression.",
        "recommendation": "Keep up the good work and stay healthy! If you feel your mood changing, check in with your healthcare provider."
    },
    "result_mild_depression": {
        "text": "Based on your responses, it appears that you may be experiencing mild depression.",
        "recommendation": "It's important to take care of your mental health. Try engaging in activities that you enjoy, getting regular exercise, and reaching out to a mental health professional for support."
    },
    "result_severe_depression": {
        "text": "Based on your responses, it appears that you may be experiencing severe depression.",
        "recommendation": "It's important to seek professional help as soon as possible. Reach out to your healthcare provider or a mental health professional for support and guidance."
    }
}

# Define the Streamlit app
def app():
    # Set the app title and page icon
    st.set_page_config(page_title="Early Depression Detection", page_icon=":smiley:")
    # Set the app header
    st.header("Early Depression Detection")
    # Set the app subheader
    st.subheader("Answer the following questions to detect depression early")
    # Set the app background color
    st.markdown(
        """
        <style>
            body {
                background-color: #849DAB;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize the answers and score
    answers = {}
    score = 0
    
    # Display all questions at once
    for question_key, question_info in knowledge_base.items():
        if "options" in question_info:
            question = question_info["text"]
            options = list(question_info["options"].keys())
            answer = st.radio(question, options, key=question_key)
            answers[question_key] = answer
            score += question_info["options"][answer]  # Add the score of the selected answer
    
    # Determine the result based on the score
    if score <= 2:
        result = knowledge_base["result_no_depression"]
    elif 3 <= score <= 6:
        result = knowledge_base["result_mild_depression"]
    else:
        result = knowledge_base["result_severe_depression"]

    # Display the result
    st.markdown(
        f"""
        <div style='background-color: #F18A85; padding: 10px'>
            <h3 style='color: white'>{result["text"]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write(result.get("recommendation", ""))
    
# Run the app
if __name__ == "__main__":
    app()
