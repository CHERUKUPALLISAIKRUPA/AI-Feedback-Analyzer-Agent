
import streamlit as st

st.set_page_config(page_title="Submit Feedback", page_icon="📝")

st.title("📝 Submit Your Feedback")

st.write("Share your experience with us.")

name = st.text_input("Enter your name")

category = st.selectbox(
    "Select feedback category",
    ["Teaching", "College Facilities", "Events", "Canteen", "Other"]
)

feedback = st.text_area(
    "Write your feedback",
    placeholder="Enter your comments here..."
)

rating = st.slider("Give your rating", 1, 5, 3)

if st.button("Submit Feedback", type="primary"):

    if name.strip() and feedback.strip():

        if "feedback_list" not in st.session_state:
            st.session_state.feedback_list = []

        st.session_state.feedback_list.append({
            "name": name,
            "category": category,
            "feedback": feedback,
            "rating": rating
        })

        st.success("Feedback submitted successfully!")

    else:
        st.warning("Please enter your name and feedback.")

st.caption("AI Feedback Analyzer Agent")
