import streamlit as st
from common import bg_markdown
from mongodb_connect.connect import get_government_benefit_info

def employee_government_benefit(employee_document):

    # get employee salary data
    
    government_benefit_data = get_government_benefit_info(government_benefit_id=employee_document['government_benefit'])

    agencies = {
        'sss':'Social Security System',
        'philhealth':'PhilHealth',
        'pagibig':'Pag-IBIG',
        'tax':'Tax'}

    cols = st.columns(4)
    i = 0
    for agency in government_benefit_data:
        if agency in ['sss', 'philhealth', 'pagibig', 'tax']:
            with cols[i]:
                st.markdown(f'#### {agencies[agency]} ####')
                for k, _item in government_benefit_data[agency].items():
                    rows = st.columns(2, gap='xxsmall')
                    with rows[0]:
                        _label = k.replace("_", " ").title()
                        st.markdown(f'**_{_label}:_**')
                    with rows[1]:
                        bg_markdown(_item)
            i+=1
    
    


            # rows = st.columns([3,7], gap='xxsmall')
            # with rows[0]:
            #     st.markdown('**_Number:_**')
            # with rows[1]:
            #     bg_markdown(government_benefit_data['sss']['sss_number'])
            
            # rows = st.columns([3,7], gap='xxsmall')
            # with rows[0]:
            #     st.markdown('**_Status:_**')
            # with rows[1]:
            #     bg_markdown(government_benefit_data['sss']['membership_status'])
            
            # rows = st.columns([3,7], gap='xxsmall')
            # with rows[0]:
            #     st.markdown('**_Status:_**')
            # with rows[1]:
            #     bg_markdown(government_benefit_data['sss']['membership_status'])

        
        
        # st.write(government_benefit_data)