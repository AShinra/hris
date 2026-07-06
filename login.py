import streamlit as st
import pandas as pd
from streamlit_geolocation import streamlit_geolocation


# ---------------------------------------------------------------------------
# Auth — replace this with your real authentication (DB lookup, OAuth, etc.).
# Never hard-code real credentials in production; use secrets/env vars.
# ---------------------------------------------------------------------------
CREDENTIALS = {
    "admin": "password123",
    "ronald": "letmein",
}


def check_credentials(username: str, password: str) -> bool:
    return CREDENTIALS.get(username) == password


# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
def init_state():
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("username", "")


# ---------------------------------------------------------------------------
# Login screen
# ---------------------------------------------------------------------------
def login_screen():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid username or password.")


# ---------------------------------------------------------------------------
# Main app — shown only after login. Captures the user's location.
# ---------------------------------------------------------------------------
def location_screen():
    st.title("📍 Your Location")
    st.write(f"Welcome, **{st.session_state.username}**!")

    st.write("Click the location icon below and allow access in your browser:")

    # The component renders its own button. Call it directly and check the
    # coordinate values — a dict full of None is still truthy.
    location = streamlit_geolocation()

    if location and location.get("latitude") is not None:
        latitude = location["latitude"]
        longitude = location["longitude"]

        st.success(f"Latitude: {latitude}")
        st.success(f"Longitude: {longitude}")

        accuracy = location.get("accuracy")
        if accuracy is not None:
            st.caption(f"Accuracy: ±{accuracy:.0f} m")

        st.map(pd.DataFrame({"lat": [latitude], "lon": [longitude]}))

        with st.expander("Raw location data"):
            st.write(location)
    else:
        st.info("Waiting for location — click the icon above and allow access.")

    st.divider()
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------
def main():
    init_state()

    if st.session_state.logged_in:
        location_screen()
    else:
        login_screen()


if __name__ == "__main__":
    main()