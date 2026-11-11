
import streamlit as st

st.set_page_config(
    page_title="AI Feedback Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Feedback Analyzer Agent")

st.subheader("Welcome to Feedback Analyzer AI!")

st.write(
    "An AI-powered application that analyzes feedback, "
    "identifies common problems and suggests improvements."
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📝 Submit Feedback")

with col2:
    st.info("🤖 AI Analysis")

with col3:
    st.info("📈 View Results")

st.subheader("What can this agent do?")

st.write("""
- Analyze student and customer feedback.
- Identify positive and negative comments.
- Find common issues.
- Suggest improvements.
- Generate a feedback summary.
""")

st.success("Use the pages in the left sidebar to get started.")

st.caption("Python | Streamlit | Ollama | Llama 3.2")
