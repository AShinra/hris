import streamlit as st
from common import bg_markdown
from mongodb_connect.connect import get_personal_info

def employee_personal_info(employee_document):

    # get employee personal data
    personal_data = get_personal_info(personal_info_id=employee_document['personal_info'])

    row1 = st.columns([1,1,1,1,1])

    # birth date details
    with row1[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Birthday:_**')
        with col1[1]:
            bg_markdown(personal_data['date_of_birth'].strftime("%B %d, %Y"))
    
    # place of birth details
    with row1[1]:
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Birth Place:_**')
        with col2[1]:
            bg_markdown(personal_data['place_of_birth'])
    
    # gender details
    with row1[2]:
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Gender:_**')
        with col3[1]:                    
            bg_markdown(personal_data['gender'])
    
    # civil status details
    with row1[3]:
        col4 = st.columns([3.2,6.8], gap='xxsmall')
        with col4[0]:
            st.markdown('**_Civil Status:_**')
        with col4[1]:                    
            bg_markdown(personal_data['civil_status'])
    
    # nationality details
    with row1[4]:
        col5 = st.columns([3.2,6.8], gap='xxsmall')
        with col5[0]:
            st.markdown('**_Nationality:_**')
        with col5[1]:                    
            bg_markdown(personal_data['nationality'])
    
    row2 = st.columns([1,2,2])

    with row2[0]:
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Blood Type:_**')
        with col1[1]:                    
            bg_markdown(personal_data['blood_type'])
    
    with row2[1]:
        # current address details
        street_address = personal_data['current_address'][0]
        barangay_address = personal_data['current_address'][1]
        city_address = personal_data['current_address'][2]

        address = ", ".join(
            filter(None, [street_address, barangay_address, city_address]))

        col1 = st.columns([2.5,7.5], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Current Address:_**')
        with col1[1]:                    
            bg_markdown(address)
    

    with row2[2]:                    
        # permanent address details
        street_address = personal_data['permanent_address'][0]
        barangay_address = personal_data['permanent_address'][1]
        city_address = personal_data['permanent_address'][2]

        address = ", ".join(
            filter(None, [street_address, barangay_address, city_address]))

        col2 = st.columns([2.5,7.5], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Permanent Address:_**')
        with col2[1]:                    
            bg_markdown(address)                
    

    row3 = st.columns([1,1,1,2])
    with row3[0]:
        # emergency contact details
        col1 = st.columns([3.2,6.8], gap='xxsmall')
        with col1[0]:
            st.markdown('**_Contact:_**')
        with col1[1]:                    
            bg_markdown(personal_data['contact_person'])
        
    with row3[1]:
        # relationship details
        col2 = st.columns([3.2,6.8], gap='xxsmall')
        with col2[0]:
            st.markdown('**_Relation:_**')
        with col2[1]:                    
            bg_markdown(personal_data['relationship'])
        
    with row3[2]:
        # contact no details
        col3 = st.columns([3.2,6.8], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Contact No.:_**')
        with col3[1]:                    
            bg_markdown(personal_data['contact_no'])
    
    with row3[3]:
        # contact address details
        street_address = personal_data['contact_address'][0]
        barangay_address = personal_data['contact_address'][1]
        city_address = personal_data['contact_address'][2]

        address = ", ".join(
            filter(None, [street_address, barangay_address, city_address]))
        col3 = st.columns([2.5,7.5], gap='xxsmall')
        with col3[0]:
            st.markdown('**_Contact Address:_**')
        with col3[1]:                    
            bg_markdown(address)
