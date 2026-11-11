
import streamlit as st

st.set_page_config(
    page_title="Feedback History",
    page_icon="📋"
)

st.title("📋 Feedback History")

st.write("View all feedback submitted during this session.")

feedback_list = st.session_state.get("feedback_list", [])

if feedback_list:

    st.success(f"Total Feedback: {len(feedback_list)}")

    for i, item in enumerate(feedback_list, start=1):

        with st.expander(f"Feedback {i} - {item['category']}"):

            st.write("Name:", item["name"])
            st.write("Category:", item["category"])
            st.write("Rating:", str(item["rating"]) + "/5")
            st.write("Feedback:", item["feedback"])

    if st.button("Clear Feedback History"):
        st.session_state.feedback_list = []
        st.session_state.analysis_result = ""
        st.rerun()

else:
    st.info("No feedback submitted yet.")

st.caption("AI Feedback Analyzer Agent")
