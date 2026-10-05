import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Roadmap Generator",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🎓 AI Career Roadmap Generator")

st.write(
    "Enter your details and AI will create a personalized career roadmap."
)


# -----------------------------
# User Inputs
# -----------------------------
education = st.text_input(
    "Education",
    placeholder="Example: B.Tech ECE"
)

skills = st.text_input(
    "Current Skills",
    placeholder="Example: C, Python, Verilog"
)

interest = st.text_input(
    "Career Interest",
    placeholder="Example: AI and Embedded Systems"
)

level = st.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

study_time = st.selectbox(
    "Study Time Per Day",
    ["30 minutes", "1 hour", "2 hours", "3+ hours"]
)

goal = st.selectbox(
    "Career Goal",
    [
        "Get a Job",
        "Internship",
        "Build Projects",
        "Higher Studies"
    ]
)


# -----------------------------
# Generate Roadmap
# -----------------------------
if st.button("🚀 Generate Career Roadmap"):

    if not education or not interest:
        st.warning("Please enter your education and career interest.")

    else:

        # Ollama model
        llm = ChatOllama(
            model="llama3.2",
            temperature=0.3
        )

        # Prompt
        prompt = ChatPromptTemplate.from_template("""
You are an AI career guidance assistant.

Create a simple and practical career roadmap for the student.

Student Details:

Education: {education}
Current Skills: {skills}
Career Interest: {interest}
Experience Level: {level}
Study Time: {study_time}
Career Goal: {goal}

Give the answer in the following format:

1. Recommended Career
2. Why this career is suitable
3. Skills to Learn
4. Month-wise Roadmap
5. Projects to Build
6. Tools and Technologies
7. Job Roles
8. Final Advice

Make the explanation simple and suitable for a beginner.
Do not give unnecessary information.
""")

        # LangChain chain
        chain = prompt | llm | StrOutputParser()

        # Generate response
        with st.spinner("Generating your career roadmap..."):

            result = chain.invoke({
                "education": education,
                "skills": skills,
                "interest": interest,
                "level": level,
                "study_time": study_time,
                "goal": goal
            })

        # Display result
        st.success("Career roadmap generated!")

        st.markdown("## 📌 Your Personalized Career Roadmap")

        st.markdown(result)