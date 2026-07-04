import streamlit as st
import re
from mongodb_connect.connect import connect_to_collection, get_personal_info, get_employment_info, get_salary_info
from pathlib import Path

def bg_markdown(item):
    st.markdown(
    f"""
    <div style="
        background-color:#000000;
        color:white;
        padding:0px 12px;
        border-radius:6px;
        text-align:left;
        width:100%;
        box-sizing:border-box;
    ">
        {item}
    </div>
    """,
    unsafe_allow_html=True
)


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
        employee_document = st.session_state.employee_document
        with st.container(border=False):


            cols = st.columns([1.3,8.7], gap='xxsmall', border=True)
            with cols[0]:

                image_path = Path("images/employees") / f"{employee_id}.jpg"
                default_image = Path("images/employees/photo_emp_blank.jpg")

                if image_path.exists():
                    st.image(str(image_path), width='stretch')
                else:
                    st.image(str(default_image))
                
            with cols[1]:
                st.markdown('**Basic Information**')

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
        
        # personal data
        personal_data = get_personal_info(personal_info_id=employee_document['personal_info'])
        
        with st.container(border=True):
            tabs = st.tabs(['Personal Information', 'Employment Information', 'Compensation'])
            with tabs[0]:
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

            with tabs[1]:
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
            
            with tabs[2]:
                # compensation data
                tabs1 = st.tabs(['Salary', 'Allowances', 'Benefits'])

                with tabs1[0]:
                    
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
                    
                    # alary grade details
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



                




        
        
            
            

            
        

    





