import streamlit as st


def header_home():
  
    logo_url = "https://i.ibb.co/XfzW10Cg/Snap-Attend.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:7px;">
            <img src='{logo_url}' style="border-radius: 20px; height:100px" /> 
            <h1>SnapAttend</h1>

        </div>
    
    """, unsafe_allow_html=True)
    
    
def header_dashboard():
    
    logo_url = "https://i.ibb.co/XfzW10Cg/Snap-Attend.png"
    
    st.markdown(f"""
        <div style="display:flex; justify-content:center; align-items:center; gap:10px">
            <img src='{logo_url}' style="border-radius: 20px; height: 80px" /> 
            <h2 style="text-align: left;">Snap<br>Attend</h2>

        </div>
    
    """, unsafe_allow_html=True)