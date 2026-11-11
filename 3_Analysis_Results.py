
import streamlit as st

st.set_page_config(
    page_title="Analysis Results",
    page_icon="📊"
)

st.title("📊 Feedback Analysis Results")

st.write("View your AI-generated feedback report.")

result = st.session_state.get("analysis_result", "")

if result:

    st.success("AI analysis report is available!")

    st.markdown(result)

    st.download_button(
        "📥 Download Analysis Report",
        data=result,
        file_name="feedback_analysis.txt",
        mime="text/plain"
    )

else:
    st.warning("No analysis available yet.")
    st.write("Please submit feedback and run the AI analysis first.")

st.caption("AI Feedback Analyzer Agent")
