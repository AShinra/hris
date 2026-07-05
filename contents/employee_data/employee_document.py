import streamlit as st
import re
from mongodb_connect.connect import connect_to_collection
from pathlib import Path

def employee_data(employee_id, employee_status):
    collection = connect_to_collection('employees')
    return collection.find_one(
        {
            "employee_id":employee_id,
            'status':employee_status
        })

def get_employee_document(employee_id, employee_status):

    if re.fullmatch(r"EMP\d{3}", employee_id):
        st.session_state.employee_document = employee_data(employee_id, employee_status)
    else:
        st.error("⚠️ Invalid employee id format. Format should be EMP001")
        st.session_state.employee_document = None