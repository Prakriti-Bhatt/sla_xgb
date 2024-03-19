# app.py

import streamlit as st

def main():
    st.title("Streamlit Basic Website")

    # HTML content with input boxes
    html_content = """
    <div style="background-color:#007bff;padding:20px;border-radius:10px;">
        <h2 style="color:#ffffff;">Welcome to my Streamlit website!</h2>
        <p style="color:#ffffff;">This is a basic website built using Streamlit with HTML, CSS, and JavaScript.</p>
        <form>
            <label for="name" style="color:#ffffff;">Enter your name:</label><br>
            <input type="text" id="name" name="name" style="margin-bottom: 10px;"><br>
            <label for="email" style="color:#ffffff;">Enter your email:</label><br>
            <input type="email" id="email" name="email" style="margin-bottom: 10px;"><br>
            <button type="submit" style="background-color:#ffffff;color:#007bff;border:none;padding:8px 16px;border-radius:5px;">Submit</button>
        </form>
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
            input[type=text], input[type=email] {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 1px solid #007bff;
                border-radius: 4px;
            }
            button {
                cursor: pointer;
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
