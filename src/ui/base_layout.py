import streamlit as st

def style_background_home():
    
    st.markdown("""
        <style>

            .stApp {
                background:#68C1FF !important;
            }
            
            .stApp div[data-testid="stColumn"]{
                background-color: #A1D0FF !important;
                padding:2.5rem !important;
                border-radius:5rem !important;
            }

        </style>            

                """, unsafe_allow_html=True)


def style_background_dashboard():
    
    st.markdown("""
        <style>

            .stApp {
                background: #bde0fe !important;
            }
        </style>            

                """, unsafe_allow_html=True)
    
    
def style_base_layout():
    
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:wght@100..900&display=swap');

            /* Hide Top Bar of streamlit*/
            #MainMenu, header, footer {
                visibility: hidden; 
            }
            
            [data-testid="stToast"] {
                color: white !important;
            }
            
            .block-container {
                padding-top: 1.5rem !important;
            }


            h1 {
                font-family: 'Montserrat' !important;
                font-size: 3.5rem !important;
                font-weight: 900 !important;
                line-height: 0.8!important;
                margin-bottom: 0rem !important;
            }

            h2 {
                color: #475569 !important;
                font-family: 'Montserrat' !important;
                font-size: 2rem !important;
                font-weight: 900 !important;
                line-height: 1.1!important;
                margin-bottom: 0rem !important;
            }
            
            h3, h4 {
                color: #475569 !important;
                font-family: 'Roboto' !important;
                font-weight: 700 !important;
            }
            
            
            button {
                background-color: #2F80AD !important;
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                tranisition: transform 0.25s ease-in-out !important;
            }
            button[kind="secondary"] {
                background-color: #2C4E99 !important;
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                tranisition: transform 0.25s ease-in-out !important;
            }
            
            button[kind="tertiary"] {
                background-color: #D6EAF5 !important;
                border-radius: 1.5rem !important;
                color: black !important;
                padding: 10px 20px !important;
                border: none !important;
                tranisition: transform 0.25s ease-in-out !important;
            }
            
            button:hover{
                transform: scale(1.07) !important;
            }
                
        </style>            

                """, unsafe_allow_html=True)