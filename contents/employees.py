import streamlit as st
from contents.employee_data.basic_info import employee_profile_photo, employee_basic_info
from contents.employee_data.personal_info import employee_personal_info
from contents.employee_data.employment_info import employee_employment_info
from contents.employee_data.salary_info import employee_salary_info
from contents.employee_data.employee_document import get_employee_document
from contents.employee_data.benefits_government import employee_government_benefit

def employees_dashboard():

    if "employee_document" not in st.session_state:
        st.session_state.employee_document = None

    with st.container():
        main_cols = st.columns(3)
        with main_cols[0]:
            cols=st.columns([2.5,7.5], gap='xxsmall')
            with cols[0]:
                st.markdown('**Employee Type**')
            with cols[1]:
                employee_status=st.selectbox(
                    label='Employee Type',
                    label_visibility='collapsed',
                    options=['Active', 'Inactive'],
                    key='employee_type')
                
        with main_cols[1]:
            cols=st.columns([2.5,7.5], gap='xxsmall')
            with cols[0]:
                st.markdown('**Employee ID**')
            with cols[1]:
                employee_id=st.text_input(
                    label='Employee Search',
                    label_visibility='collapsed',
                    key='employee_id')
                
        with main_cols[2]:
            if st.button(label='Search', width='stretch'):
                employee_id = employee_id.strip().upper()
                get_employee_document(
                    employee_id=employee_id,
                    employee_status=employee_status)
    
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
                tabs1 = st.tabs(['Salary', 'Benefits', 'Allowances'])

                with tabs1[0]:
                    try:
                        employee_salary_info(employee_document=employee_document)
                    except:
                        st.info('Updating...')
                
                with tabs1[1]:
                    try:
                        employee_government_benefit(employee_document=employee_document)
                    except:
                        st.info('Updating...')
                
                with tabs1[2]:
                    ''''''
                    



                




        
        
            
            

            
        

    





