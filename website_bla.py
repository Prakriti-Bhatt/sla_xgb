# app.py

import streamlit as st

def main():
    st.title("Streamlit Basic Website")

    # HTML content
    html_content = """
    <div style="background-color:#f0f0f0;padding:10px;border-radius:10px;">
        <h2 style="color:#333;">Welcome to my Streamlit website!</h2>
        <p>This is a basic website built using Streamlit with HTML, CSS, and JavaScript.</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    # CSS styling
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #e6e6e6;
            }
            h2 {
                color: #0066cc;
            }
            p {
                color: #333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # JavaScript
    js_code = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Page loaded.');
        });
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
