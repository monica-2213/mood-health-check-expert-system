import streamlit as st

# Define your knowledge base as a dictionary
knowledge_base = {
    "question_1": {
        "text": "How often have you been feeling down, depressed, or hopeless in the past 2 weeks?",
        "options": {
            "Not at all": "question_2",
            "Several days": "question_3",
            "More than half the days": "question_4",
            "Nearly every day": "question_5"
        }
    },
    "question_2": {
        "text": "Have you experienced a loss of interest or pleasure in doing things that you normally enjoy?",
        "options": {
            "No": "result_no_depression",
            "Yes": "question_6"
        }
    },
    "question_3": {
        "text": "Have you experienced a loss of interest or pleasure in doing things that you normally enjoy?",
        "options": {
            "No": "result_mild_depression",
            "Yes": "question_6"
        }
    },
    "question_4": {
        "text": "Have you experienced a loss of interest or pleasure in doing things that you normally enjoy?",
        "options": {
            "No": "result_mild_depression",
            "Yes": "question_6"
        }
    },
    "question_5": {
        "text": "Have you experienced a loss of interest or pleasure in doing things that you normally enjoy?",
        "options": {
            "No": "result_severe_depression",
            "Yes": "question_6"
        }
    },
    "question_6": {
        "text": "Have you experienced a significant weight loss or gain?",
        "options": {
            "No": "question_7",
            "Yes": "result_severe_depression"
        }
    },
    "question_7": {
        "text": "Have you experienced trouble sleeping or sleeping too much?",
        "options": {
            "No": "question_8",
            "Yes": "result_mild_depression"
        }
    },
    "question_8": {
        "text": "Have you experienced feelings of worthlessness or excessive guilt?",
        "options": {
            "No": "question_9",
            "Yes": "result_mild_depression"
        }
    },
    "question_9": {
        "text": "Have you experienced difficulty in concentrating or making decisions?",
        "options": {
            "No": "result_mild_depression",
            "Yes": "result_severe_depression"
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
        "recommendation": "It's important to seek professional help as soon as possible. Reach out to your healthcare provider or a mental health professional for support and guidance. They can help you create a treatment plan and provide you with the necessary resources to support your mental health."
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
    
    # Initialize the answers dictionary
    answers = {}
    
    # Display all questions at once
    for question_key, question_info in knowledge_base.items():
        if "options" in question_info:
            question = question_info["text"]
            options = list(question_info["options"].keys())
            answer = st.radio(question, options, key=question_key)
            answers[question_key] = answer

    # Get the result based on answers
    result_key = answers.get("question_1")  # Start from question_1
    
    # Traverse through the knowledge base until a result is found
    while result_key and "result" not in result_key:
        # Ensure that the result_key is valid
        next_key = knowledge_base.get(result_key)
        if next_key and "options" in next_key:
            result_key = next_key["options"].get(answers.get(result_key))
        else:
            break

    # Get final result
    result = knowledge_base.get(result_key, {})
    
    if result:
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
    else:
        st.write("There was an error processing the results.")

# Run the app
if __name__ == "__main__":
    app()
