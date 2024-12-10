import streamlit as st
from app.rag import process_query
from app.settings import APP_TITLE, APP_ICON

st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)
st.title("AI-Powered Fitness Assistant")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- **Ask a Fitness Question**: Use the text box below to get fitness advice.
- **About**: Learn about the project and its features.
""")

# Main input area
user_query = st.text_input("Enter your fitness-related question:")
if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Processing your query..."):
            response = process_query(user_query)
            st.markdown("### Answer")
            st.write(response)
    else:
        st.error("Please enter a valid query.")
