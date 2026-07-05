import streamlit as st
from streamlit_geolocation import streamlit_geolocation


def get_user_location():
    st.title("Get User Location")

    if st.button("Get My Location"):
        location = streamlit_geolocation()

        if location:
            st.write(location)

            latitude = location["latitude"]
            longitude = location["longitude"]

            st.success(f"Latitude: {latitude}")
            st.success(f"Longitude: {longitude}")