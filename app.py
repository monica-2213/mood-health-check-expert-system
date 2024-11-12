import streamlit as st
from fpdf import FPDF

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

# Function to generate PDF report
def generate_pdf(answers, result):
    # Create instance of FPDF class and add a page
    pdf = FPDF()
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Mood Health Check Report", ln=True, align='C')

    # Add answers to the report
    pdf.ln(10)  # Line break
    pdf.cell(200, 10, txt="Your Responses:", ln=True)

    for question_key, answer in answers.items():
        question = knowledge_base.get(question_key, {}).get('text', '')
        pdf.cell(200, 10, txt=f"{question} {answer}", ln=True)

    # Add the result to the report
    pdf.ln(10)  # Line break
    pdf.cell(200, 10, txt="Results:", ln=True)
    pdf.cell(200, 10, txt=result["text"], ln=True)
    pdf.cell(200, 10, txt=result["recommendation"], ln=True)

    # Save the pdf to a file
    pdf_output = "/tmp/mood_health_report.pdf"
    pdf.output(pdf_output)

    return pdf_output

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
    
    # Display all questions
    for question_key, question_info in knowledge_base.items():
        if "options" in question_info:
            question = question_info["text"]
            options = list(question_info["options"].keys())
            answer = st.radio(question, options, key=question_key)
            answers[question_key] = answer
            score += question_info["options"][answer]  # Add the score of the selected answer
    
    # Button to check results
    if st.button("Check Results"):
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

        # Generate PDF report and provide a download link
        pdf_file = generate_pdf(answers, result)
        st.download_button(
            label="Download Report as PDF",
            data=open(pdf_file, "rb").read(),
            file_name="mood_health_report.pdf",
            mime="application/pdf"
        )
    
# Run the app
if __name__ == "__main__":
    app()
