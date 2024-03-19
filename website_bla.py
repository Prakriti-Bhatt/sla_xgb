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

    # HTML content with input boxes
    html_content = """
    <div style="background-color:#008B8B;padding:20px;border-radius:10px;">
        <h3 style="color:#ffffff;" class="title">Input your project specifics, historical data, and performance benchmarks to ensure project oversight and risks.</h3>
        <form>
            <!-- Generate 22 input boxes -->
            <label for="input1" style="color:#ffffff;">Input 1:</label><br>
            <input type="text" id="input1" name="input1" style="margin-bottom: 10px;"><br>
            <label for="input2" style="color:#ffffff;">Input 2:</label><br>
            <input type="text" id="input2" name="input2" style="margin-bottom: 10px;"><br>
            <!-- Repeat for input3 through input22 -->
            <!-- Modify the above lines to add more input boxes as needed -->
            <button type="submit" style="background-color:#ffffff;color:#007bff;border:none;padding:8px 16px;border-radius:5px;margin-top:10px;">Predict</button>
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
            }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
