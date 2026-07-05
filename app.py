import streamlit as st
from streamlit_option_menu import option_menu
import contents.employees as employees
from login import get_user_location


if __name__ == '__main__':

    st.set_page_config(
        page_title="HRIS",
        page_icon="👥",
        layout="wide",
        initial_sidebar_state="expanded")

    with st.sidebar:
        selected_option = option_menu(
            menu_title='Main', # Hide the menu header
            options = [
                "Dashboard",
                "Employees",
                "Leave Management",
                "Payroll",
                'Login'],
            icons = [
                "speedometer2",
                "people-fill",
                "calendar-minus",
                "cash-stack",
                "door-open"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical")
    
if selected_option=='Employees':
    employees.employees_dashboard()
if selected_option=='Login':
    get_user_location()