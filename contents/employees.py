import streamlit as st
import re
from mongodb_connect.connect import connect_to_collection
from pathlib import Path
from contents.employee_data.basic_info import employee_profile_photo, employee_basic_info
from contents.employee_data.personal_info import employee_personal_info
from contents.employee_data.employment_info import employee_employment_info
from contents.employee_data.salary_info import employee_salary_info

def employee_data(employee_id, employee_status):
    collection = connect_to_collection('employees')
    return collection.find_one(
        {
            "employee_id":employee_id,
            'status':employee_status
        })

def employees_dashboard():

    if "employee_document" not in st.session_state:
        st.session_state.employee_document = None

    with st.container(border=True):
        cols=st.columns([1,1,8], gap='xxsmall')
        with cols[0]:
            st.markdown('Employee Type')
        with cols[1]:
            employee_status=st.selectbox(
                label='Employee Type',
                label_visibility='collapsed',
                options=['Active', 'Inactive'],
                key='employee_type')
        
        cols=st.columns([1,1,8], gap='xxsmall')
        with cols[0]:
            st.markdown('Employee ID')
        with cols[1]:
            employee_id=st.text_input(
                label='Employee Search',
                label_visibility='collapsed',
                key='employee_id')
        with cols[2]:
            if st.button(label='Search'):
                employee_id = employee_id.strip().upper()
                if re.fullmatch(r"EMP\d{3}", employee_id):
                    st.session_state.employee_document = employee_data(employee_id, employee_status)
                else:
                    st.error("⚠️ Invalid employee id format. Format should be EMP001")
                    st.session_state.employee_document = None
    
    if st.session_state.employee_document:
        # main document for employee
        employee_document = st.session_state.employee_document

        # basic information
        with st.container(border=False):
            cols = st.columns([1.3,8.7], gap='xxsmall', border=True)

            with cols[0]:
                employee_profile_photo(employee_id=employee_id)                

            with cols[1]:
                employee_basic_info(employee_document=employee_document)
        
        with st.container(border=True):
            tabs = st.tabs(['Personal Information', 'Employment Information', 'Compensation'])

            with tabs[0]:               
                # personal info
                employee_personal_info(employee_document=employee_document)

            with tabs[1]:
                # employment info
                employee_employment_info(employee_document=employee_document)
            
            with tabs[2]:                
                # compensation data
                tabs1 = st.tabs(['Salary', 'Allowances', 'Benefits'])

                with tabs1[0]:
                    employee_salary_info(employee_document=employee_document)
                
                with tabs1[1]:
                    ''''''
                
                with tabs1[2]:
                    ''''''
                    



                




        
        
            
            

            
        

    





