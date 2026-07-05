import streamlit as st
from common import bg_markdown
from mongodb_connect.connect import get_salary_info

def employee_salary_info(employee_document):

    # get employee salary data
    
    salary_data = get_salary_info(salary_info_id=employee_document['salary_info'])
    
    row1 = st.columns([1,1,1,1,1])

    # basic salary details
    with row1[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Basic:_**')
        with col1[1]:
            bg_markdown(f"{salary_data['basic_salary']:,.2f}")
    
    # basic salary details
    with row1[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Type:_**')
        with col2[1]:
            bg_markdown(salary_data['salary_type'])
    
    # pay frequency details
    with row1[2]:
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Pay Freq:_**')
        with col3[1]:
            bg_markdown(salary_data['pay_frequency'])
    
    # currency details
    with row1[3]:
        col4 = st.columns([3.2,6.8], gap='xxsmall')
        with col4[0]:
            st.markdown('**_Currency_**')
        with col4[1]:
            bg_markdown(salary_data['currency'])
    
    # salary grade details
    with row1[4]:
        col5 = st.columns([3.2,6.8], gap='xxsmall')
        with col5[0]:
            st.markdown('**_Grade_**')
        with col5[1]:
            bg_markdown(salary_data['salary_grade'])


    row2 = st.columns([1,1,1,1,1])

    # increment details
    with row2[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Increment:_**')
        with col1[1]:
            bg_markdown(salary_data['step_increment'])
    
    # increment details
    with row2[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Effectivity:_**')
        with col2[1]:
            bg_markdown(salary_data['effective_date'].strftime("%B %d, %Y"))
        
        