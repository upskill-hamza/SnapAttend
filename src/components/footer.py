import streamlit as st

def footer_dashboard():
   
    linkedin_svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#0077B5">
        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
    </svg>
    """

    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.18); }
        100% { transform: scale(1); }
    }
    .custom-footer {
        margin-top: 4rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
        background: transparent; 
        width: 100%;
    }
    .footer-text {
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 500;
        font-size: 20px !important;
        color: #31333F;
        margin: 0;
        letter-spacing: 0.5px;
        opacity: 0.85; 
    }
    .heart-icon {
        display: inline-block;
        color: #ff4b4b;
        animation: pulse 1.6s infinite ease-in-out;
    }
    .gradient-name {
        background: linear-gradient(45deg, #ff4b4b, #ff7e5f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    .linkedin-link {
        display: flex;
        align-items: center;
        transition: transform 0.2s;
    }
    .linkedin-link:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # 3. Render the structural HTML with the SVG injected
    st.markdown(f"""
    <div class="custom-footer">
        <p class="footer-text">Created with <span class="heart-icon">❤️</span> by <span class="gradient-name">Hamza</span></p><a class="linkedin-link" href="https://linkedin.com/in/hamza-ansari-1240ab2b7" target="_blank">{linkedin_svg}</a>
    </div>
    """, unsafe_allow_html=True)
    