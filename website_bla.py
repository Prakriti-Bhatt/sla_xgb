# app.py

import streamlit as st
import numpy as np
import pickle


# Load the model
model_pkl_file = "final_model_try.pkl"
with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)

dict_sldu = {'ENGG-DELIVERY UNIT-AMERICAS 1': 0, 'ENGG-DELIVERY UNIT-AMERICAS 2': 1, 'ENGG-DELIVERY UNIT-APMEA': 2, 'ENGG-DELIVERY UNIT-EUROPE': 3, 'FSC-CIS-DELIVERY UNIT-AMERICAS 1': 4, 'FSC-CIS-DELIVERY UNIT-AMERICAS 2': 5, 'FSC-CIS-DELIVERY UNIT-APMEA': 6, 'FSC-CIS-DELIVERY UNIT-EUROPE': 7, 'FSC-WDC-DELIVERY UNIT-AMERICAS 1': 8, 'FSC-WDC-DELIVERY UNIT-AMERICAS 2': 9, 'FSC-WDC-DELIVERY UNIT-APMEA': 10, 'FSC-WDC-DELIVERY UNIT-EUROPE': 11, 'NO EH': 12, 'WEF-CRS-DELIVERY UNIT-AMERICAS 1': 13, 'WEF-CRS-DELIVERY UNIT-AMERICAS 2': 14, 'WEF-CRS-DELIVERY UNIT-APMEA': 15, 'WEF-CRS-DELIVERY UNIT-EUROPE': 16, 'WEF-DA&I-DELIVERY UNIT-AMERICAS 1': 17, 'WEF-DA&I-DELIVERY UNIT-AMERICAS 2': 18, 'WEF-DA&I-DELIVERY UNIT-APMEA': 19, 'WEF-DA&I-DELIVERY UNIT-EUROPE': 20, 'WEF-EA-DELIVERY UNIT-AMERICAS 1': 21, 'WEF-EA-DELIVERY UNIT-AMERICAS 2': 22, 'WEF-EA-DELIVERY UNIT-APMEA': 23, 'WEF-EA-DELIVERY UNIT-EUROPE': 24}
    
dict_smu = {'AMERICAS 1': 0, 'AMERICAS 2': 1, 'APMEA': 2, 'EUROPE': 3, 'NO SMU': 4}




def predict_sla(sldu, smu, work_bots, user_supported, total_incidents, reopened, sr_resolved, same_day_sr, total_sr, sr_l1, l3, l2, incident_l1, first_hop, automation, same_day_incidents, reassigned, backlog, fte, incidents_resolved, team):
    
    # Create a list of input features
    input_features = [sldu, smu, work_bots, user_supported, total_incidents, reopened, sr_resolved, same_day_sr, total_sr, sr_l1, l3, l2, incident_l1, first_hop, automation, same_day_incidents, reassigned, backlog, fte, incidents_resolved, team]
    
    # Replace empty strings with NaN values in input features
    for i in range(len(input_features)):
        input_features[i] = np.nan if input_features[i] == "" else input_features[i]
    
    # Convert the input features into a numpy array with dtype=object
    feat_list = np.array(input_features, dtype=object)
    
    # Predict using the model
    prediction = model.predict([feat_list])
    probabilities = model.predict_proba([feat_list])
    #st.success("Probability of meeting SLAs ", probablities[0][1])
    #st.success("Probability of not meeting SLAs ", probablities[0][0])
    #result = np.array[prediction, probabilities]
    
    return prediction, probabilities



def main():
    st.title("Penalty SLA Prediction")

    # CSS styling for centering the title
    st.markdown(
        """
        <style>
            /* Targeting the Streamlit title class */
            .title-container {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input form
    st.sidebar.header("Input Parameters")

    # HTML content with input boxes
    html_content = """
    <div style="background-color:#008B8B;padding:20px;border-radius:10px;">
        <h4 style="color:#ffffff;" class="title">Input your project specifics, historical data, and performance benchmarks to ensure project oversight and risks.</h4>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    program = st.text_input("PROGRAM"," ") 
    
    # Selectbox for SLDU
    sldu_options = ['ENGG-DELIVERY UNIT-AMERICAS 1', 'ENGG-DELIVERY UNIT-AMERICAS 2', 'ENGG-DELIVERY UNIT-APMEA', 'ENGG-DELIVERY UNIT-EUROPE', 'FSC-CIS-DELIVERY UNIT-AMERICAS 1', 'FSC-CIS-DELIVERY UNIT-AMERICAS 2', 'FSC-CIS-DELIVERY UNIT-APMEA', 'FSC-CIS-DELIVERY UNIT-EUROPE', 'FSC-WDC-DELIVERY UNIT-AMERICAS 1', 'FSC-WDC-DELIVERY UNIT-AMERICAS 2', 'FSC-WDC-DELIVERY UNIT-APMEA', 'FSC-WDC-DELIVERY UNIT-EUROPE', 'NO EH', 'WEF-CRS-DELIVERY UNIT-AMERICAS 1', 'WEF-CRS-DELIVERY UNIT-AMERICAS 2', 'WEF-CRS-DELIVERY UNIT-APMEA', 'WEF-CRS-DELIVERY UNIT-EUROPE', 'WEF-DA&I-DELIVERY UNIT-AMERICAS 1', 'WEF-DA&I-DELIVERY UNIT-AMERICAS 2', 'WEF-DA&I-DELIVERY UNIT-APMEA', 'WEF-DA&I-DELIVERY UNIT-EUROPE', 'WEF-EA-DELIVERY UNIT-AMERICAS 1', 'WEF-EA-DELIVERY UNIT-AMERICAS 2', 'WEF-EA-DELIVERY UNIT-APMEA', 'WEF-EA-DELIVERY UNIT-EUROPE']
    sldu = st.selectbox("SLDU", sldu_options)

    # If the selected option is " ", show a text input box
    if sldu == " ":
        custom_sldu = st.text_input("Enter custom SLDU" )
        st.write("You entered:", custom_sldu)
    else:
        encoded_sldu = dict_sldu[sldu]
    
    # Selectbox for SMU
    smu_options = ['AMERICAS 1', 'AMERICAS 2', 'APMEA', 'EUROPE', 'NO SMU']
    smu = st.selectbox("SMU", smu_options)

    # If the selected option is " ", show a text input box
    if smu == " ":
        custom_smu = st.text_input("Enter custom SMU" )
        st.write("You entered:", custom_smu)
    else:
        encoded_smu = dict_smu[smu]

    # Other input fields
    work_bots = st.text_input("Work done by BOTs")
    user_supported = st.text_input("Users Supported")
    total_incidents = st.text_input("Total Number of Incidents Reported/Received")
    reopened = st.text_input("Tickets Reopened")
    sr_resolved = st.text_input("Service Requests resolved in the month")
    same_day_sr = st.text_input("Same Day Resolution % of Service Requests")
    total_sr = st.text_input("Number of Service Requests received")
    sr_l1 = st.text_input("Number of Service Requests resolved by L1/L1.5 team")
    l3 = st.text_input("Number of Incidents resolved by L3 and above team")
    l2 = st.text_input("Number of Incidents resolved by L2 team")
    incident_l1 = st.text_input("Number of Incidents resolved by L1/L1.5 team")
    first_hop = st.text_input("Number of first hop resolved Incidents")
    automation = st.text_input("% Tickets ( Incidents and Service Requests ) fully resolved through automation")
    same_day_incidents = st.text_input("% Same Day Resolution of Incidents")
    reassigned = st.text_input("% Re-Assigned Incidents more than twice")
    backlog = st.text_input(" Overall Backlog Index (Incidents + SRs)")
    fte = st.text_input("% FTE beyond SmartOps (Rest of the team)")
    incidents_resolved = st.text_input("Total incidents resolved in a month ")
    team = st.text_input("Team Size ")
    
    result = ""
    if st.button("Predict"):
        result, prob = predict_sla(encoded_sldu, encoded_smu, work_bots, user_supported, total_incidents, reopened, sr_resolved, same_day_sr, total_sr, sr_l1, l3, l2, incident_l1, first_hop, automation, same_day_incidents, reassigned, backlog, fte, incidents_resolved, team)
        st.success("Probability of meeting SLAs: {:.2f}%".format(probabilities[0][1] * 100))
        st.success("Probability of not meeting SLAs: {:.2f}%".format(probabilities[0][0] * 100))
        
        if prediction[0] == 1:
            st.success("Program will meet Penalty SLAs")
        else:
            st.error("Program will not meet Penalty SLAs")


    
    # CSS styling
    st.markdown(
        """
        <style>
            body {
            background-color: #f0f0f0; 
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
    background-color: red; /* Updated color */
    color: white; /* Text color */
    border: none;
    padding: 8px 16px;
    border-radius: 5px;
    margin-top: 10px;
    text-align: center; /* Center the button horizontally */
}


        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
