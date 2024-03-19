# app.py

import streamlit as st

def main():
    st.title("Streamlit Basic Website")

    # HTML content
    html_content = """
    <div style="background-color:#007bff;padding:20px;border-radius:10px;">
        <h2 style="color:#ffffff;">Welcome to my Streamlit website!</h2>
        <p style="color:#ffffff;">This is a basic website built using Streamlit with HTML, CSS, and JavaScript.</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    # CSS styling
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #ffffff;
                color: #333;
            }
            h2 {
                color: #007bff;
            }
            p {
                color: #007bff;
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
