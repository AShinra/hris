import streamlit as st
from pathlib import Path
from common import bg_markdown

def employee_profile_photo(employee_id):

    image_path = Path("images/employees") / f"{employee_id}.jpg"
    default_image = Path("images/employees/photo_emp_blank.jpg")
    
    if image_path.exists():
        st.image(str(image_path), width='stretch')
    else:
        st.image(str(default_image))


def employee_basic_info(employee_document):

    st.markdown('**Basic Information**')

    for key in list(st.session_state.keys()):
        del st.session_state[key]

    row1 = st.columns([1,1,1,1])

    # last name details
    with row1[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Last Name:_**')
        with col1[1]:
            bg_markdown(employee_document['last_name'])
    
    # first name details
    with row1[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_First Name:_**')
        with col2[1]:
            bg_markdown(employee_document['first_name'])

    # middle details
    with row1[2]:
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Mid Name:_**')
        with col3[1]:
            bg_markdown(employee_document['middle_name'])
    
    # suffix details
    with row1[3]:
        col4 = st.columns([3.2,6.8], gap='xxsmall')
        with col4[0]:
            st.markdown('**_Suffix:_**')
        with col4[1]:
            if employee_document['suffix']:
                bg_markdown(employee_document['suffix'])
            else:
                bg_markdown('')
    

    row2 = st.columns([1,1,1,1])
    # nick name details
    with row2[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Nickname:_**')
        with col1[1]:
            if employee_document['nickname']:
                bg_markdown(employee_document['nickname'])
            else:
                bg_markdown('Not Provided')
    
    # mobile details
    with row2[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Mobile:_**')
        with col2[1]:
            if employee_document['mobile_no']:
                bg_markdown(employee_document['mobile_no'])
            else:
                bg_markdown('Not Provided')
    
    # status details
    with row2[2]:
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Status:_**')
        with col3[1]:
            bg_markdown(employee_document['status'])


    row3 = st.columns([2,3])
    # email details
    with row3[0]:
        col2 = st.columns([2.5,7.5], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Work Mail:_**')
        with col2[1]:
            if employee_document['work_email']:
                bg_markdown(employee_document['work_email'])
            else:
                bg_markdown('Not Provided')
