import streamlit as st
from common import bg_markdown
from mongodb_connect.connect import get_employment_info

def employee_employment_info(employee_document):

    # employment data
    employment_data = get_employment_info(employment_info_id=employee_document['employment_info'])

    row1 = st.columns([1,1,1,1,1])
    # hire date details
    with row1[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Date Hired:_**')
        with col1[1]:
            bg_markdown(employment_data['date_hired'].strftime("%B %d, %Y"))
    
    # employment status details
    with row1[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Status:_**')
        with col2[1]:
            bg_markdown(employment_data['employment_status'])

    # employment type details
    with row1[2]:
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Type:_**')
        with col3[1]:
            bg_markdown(employment_data['employment_type'])
    
    # manager details
    with row1[3]:
        col4 = st.columns([3.2,6.8], gap='xxsmall')
        with col4[0]:
            st.markdown('**_Manager:_**')
        with col4[1]:
            bg_markdown(employment_data['manager'])
    
    # supervisor details
    with row1[4]:
        col5 = st.columns([3.2,6.8], gap='xxsmall')
        with col5[0]:
            st.markdown('**_Supervisor:_**')
        with col5[1]:
            bg_markdown(employment_data['supervisor'])

    row2 = st.columns([2,1,1,1])
    # department details
    with row2[0]:
        col1 = st.columns([2.5,7.5], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Department:_**')
        with col1[1]:
            bg_markdown(employment_data['department'])
    
    # position details
    with row2[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Position:_**')
        with col2[1]:
            bg_markdown(employment_data['position'])
    
    # position details
    with row2[2]:
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Work Env:_**')
        with col3[1]:
            bg_markdown(employment_data['work_arrangement'])
    
    # shift sched details
    time_in = employment_data['shift_schedule'][0]
    time_out = employment_data['shift_schedule'][1]

    shift_sched = "-".join(
        filter(None, [time_in, time_out]))
    
    with row2[3]:
        col4 = st.columns([3.2,6.8], gap='xxsmall')
        with col4[0]:
            st.markdown('**_Shift:_**')
        with col4[1]:
            bg_markdown(shift_sched)