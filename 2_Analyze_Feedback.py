
import streamlit as st
import requests

st.set_page_config(page_title="Analyze Feedback", page_icon="🤖")

st.title("🤖 AI Feedback Analysis")

st.write("Let AI analyze submitted feedback and identify important insights.")

feedback_list = st.session_state.get("feedback_list", [])

if not feedback_list:
    st.warning("No feedback found. Please submit feedback first.")

else:
    st.write("Total feedback submitted:", len(feedback_list))

    if st.button("Analyze Feedback", type="primary"):

        all_feedback = ""

        for item in feedback_list:
            all_feedback += (
                f"\nCategory: {item['category']}"
                f"\nRating: {item['rating']}/5"
                f"\nFeedback: {item['feedback']}\n"
            )

        prompt = f"""
You are an AI Feedback Analyzer Agent.

Analyze the following feedback:

{all_feedback}

Provide:
1. Overall feedback summary
2. Positive points
3. Negative points
4. Common problems
5. Improvement suggestions
6. Overall sentiment (Positive, Negative or Mixed)

Use simple English. Do not invent information.
"""

        try:
            with st.spinner("AI is analyzing feedback..."):

                response = requests.post(
                    "http://localhost:11434/api/chat",
                    json={
                        "model": "llama3.2:1b",
                        "messages": [
                            {"role": "user", "content": prompt}
                        ],
                        "stream": False
                    },
                    timeout=180
                )

                response.raise_for_status()

                result = response.json()["message"]["content"]

            st.session_state.analysis_result = result
            st.success("Analysis completed successfully!")

            st.subheader("AI Analysis")
            st.markdown(result)

        except requests.exceptions.ConnectionError:
            st.error("Please open Ollama and try again.")

        except Exception as e:
            st.error(f"Analysis failed: {e}")

st.caption("Powered by Ollama and Llama 3.2")
