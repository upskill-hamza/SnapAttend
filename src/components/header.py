import streamlit as st


def header_home():
  
    logo_url = "https://i.ibb.co/XfzW10Cg/Snap-Attend.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:7px;">
            <img src='{logo_url}' style="border-radius: 20px; height:100px" /> 
            <h1>SnapAttend</h1>

        </div>
    
    """, unsafe_allow_html=True)