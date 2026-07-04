import streamlit as st
from streamlit_option_menu import option_menu
import contents.employees as employees


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
                "Payroll"],
            icons = [
                "speedometer2",
                "people-fill",
                "calendar-minus",
                "cash-stack"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical")
    
if selected_option=='Employees':
    employees.employees_dashboard()