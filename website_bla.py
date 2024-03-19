# app.py

import streamlit as st
import numpy as np
import pickle
import pandas as pd
import xgboost
from PIL import Image

pickle_in = open("final_model.pkl","rb")
final_model=pickle.load(pickle_in)


def predict_note_authentication(sldu,smu,work_bots,user_supported,total_incidents,reopened,sr_resolved,same_day_sr,total_sr,sr_l1,l3,l2,incident_l1,first_hop,automation,same_day_incidents,reassigned,backlog,fte,incidents_resolved,team):
    dict_sldu = {'ENGG-DELIVERY UNIT-AMERICAS 1': 0, 'ENGG-DELIVERY UNIT-AMERICAS 2': 1, 'ENGG-DELIVERY UNIT-APMEA': 2, 'ENGG-DELIVERY UNIT-EUROPE': 3, 'FSC-CIS-DELIVERY UNIT-AMERICAS 1': 4, 'FSC-CIS-DELIVERY UNIT-AMERICAS 2': 5, 'FSC-CIS-DELIVERY UNIT-APMEA': 6, 'FSC-CIS-DELIVERY UNIT-EUROPE': 7, 'FSC-WDC-DELIVERY UNIT-AMERICAS 1': 8, 'FSC-WDC-DELIVERY UNIT-AMERICAS 2': 9, 'FSC-WDC-DELIVERY UNIT-APMEA': 10, 'FSC-WDC-DELIVERY UNIT-EUROPE': 11, 'NO EH': 12, 'WEF-CRS-DELIVERY UNIT-AMERICAS 1': 13, 'WEF-CRS-DELIVERY UNIT-AMERICAS 2': 14, 'WEF-CRS-DELIVERY UNIT-APMEA': 15, 'WEF-CRS-DELIVERY UNIT-EUROPE': 16, 'WEF-DA&I-DELIVERY UNIT-AMERICAS 1': 17, 'WEF-DA&I-DELIVERY UNIT-AMERICAS 2': 18, 'WEF-DA&I-DELIVERY UNIT-APMEA': 19, 'WEF-DA&I-DELIVERY UNIT-EUROPE': 20, 'WEF-EA-DELIVERY UNIT-AMERICAS 1': 21, 'WEF-EA-DELIVERY UNIT-AMERICAS 2': 22, 'WEF-EA-DELIVERY UNIT-APMEA': 23, 'WEF-EA-DELIVERY UNIT-EUROPE': 24}
    
    dict_smu = {'AMERICAS 1': 0, 'AMERICAS 2': 1, 'AMERICAS1': 2, 'AMERICAS2': 3, 'APMEA': 4, 'Americas 1': 5, 'Americas 2': 6, 'EUROPE': 7, 'Europe': 8, 'NO SMU': 9}

    encoded_sldu = dict_sldu[sldu]
    encoded_smu = dict_smu[smu]
    
    prediction=final_model.predict([[encoded_sldu,encoded_smu,work_bots,user_supported,total_incidents,reopened,sr_resolved,same_day_sr,total_sr,sr_l1,l3,l2,incident_l1,first_hop,automation,same_day_incidents,reassigned,backlog,fte,incidents_resolved,team]])
    if prediction == 1 :
        pred = 'MET'
    else :
        pred = 'NOT MET'
    return pred


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

    # HTML content with input boxes
    html_content = """
    <div style="background-color:#008B8B;padding:20px;border-radius:10px;">
        <h4 style="color:#ffffff;" class="title">Input your project specifics, historical data, and performance benchmarks to ensure project oversight and risks.</h4>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    program = st.text_input("PROGRAM","Type Here") 
    sldu = st.text_input("SLDU","Type Here")
    smu = st.text_input("SMU","Type Here")
    work_bots = st.text_input("Work done by BOTs","Type Here")
    user_supported = st.text_input("Users Supported","Type Here")
    total_incidents = st.text_input("Total Number of Incidents Reported/Received","Type Here")
    reopened = st.text_input("Tickets Reopened","Type Here")
    sr_resolved = st.text_input("Service Requests resolved in the month","Type Here")
    same_day_sr = st.text_input("Same Day Resolution % of Service Requests","Type Here")
    total_sr = st.text_input("Number of Service Requests received","Type Here")
    sr_l1 = st.text_input("Number of Service Requests resolved by L1/L1.5 team","Type Here")
    l3 = st.text_input("Number of Incidents resolved by L3 and above team","Type Here")
    l2 = st.text_input("Number of Incidents resolved by L2 team","Type Here")
    incident_l1 = st.text_input("Number of Incidents resolved by L1/L1.5 team","Type Here")
    first_hop = st.text_input("Number of first hop resolved Incidents","Type Here")
    automation = st.text_input("% Tickets ( Incidents and Service Requests ) fully resolved through automation","Type Here")
    same_day_incidents = st.text_input("% Same Day Resolution of Incidents","Type Here")
    reassigned = st.text_input("% Re-Assigned Incidents more than twice","Type Here")
    backlog = st.text_input(" Overall Backlog Index (Incidents + SRs)","Type Here")
    fte = st.text_input("% FTE beyond SmartOps (Rest of the team)","Type Here")
    incidents_resolved = st.text_input("TOTAL INCIDENTS ","Type Here")
    team = st.text_input("Team Size ","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(sldu,smu,work_bots,user_supported,total_incidents,reopened,sr_resolved,same_day_sr,total_sr,sr_l1,l3,l2,incident_l1,first_hop,automation,same_day_incidents,reassigned,backlog,fte,incidents_resolved,team)
    st.success('The output is {}'.format(result))

    
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
