# app.py

import streamlit as st

def main():
    st.title("Penalty SLA Prediction")

    # CSS styling for centering the title
    st.markdown(
        """
        <style>
            .title {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input form
    st.sidebar.header("Input Parameters")

    inputs_left = []
    inputs_right = []
    for i in range(1, 12):
        inputs_left.append(st.sidebar.text_input(f"Input {i} Left"))
        inputs_right.append(st.sidebar.text_input(f"Input {i} Right"))

    # HTML content with input boxes
    html_content = """
    <div style="background-color:#008B8B;padding:20px;border-radius:10px;">
        <h5 style="color:#ffffff;" class="title">Input your project specifics, historical data, and performance benchmarks to ensure project oversight and risks.</h5>
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
            label {
                color: #ffffff;
            }
            input[type=text] {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 1px solid #007bff;
                border-radius: 4px;
            }
            button {
                cursor: pointer;
                background-color:#ffffff;
                color:#007bff;
                border:none;
                padding:8px 16px;
                border-radius:5px;
                margin-top:10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
