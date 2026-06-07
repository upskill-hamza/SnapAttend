import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter details of the new subject")
    sub_id = st.text_input("Subject Code", placeholder="DSC-501")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Deep Learning")

    if st.button("Create Subject Now", type='primary', width="stretch"):
        if sub_id and sub_name:
            try:
                create_subject(sub_id, sub_name, teacher_id)
                st.toast("Subject Created Successfully")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")