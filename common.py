import streamlit as st

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
    unsafe_allow_html=True)