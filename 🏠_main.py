import streamlit as st
from streamlit_navigation_bar import st_navbar

# Configure page layout to be wide and collapse the sidebar
st.set_page_config(page_title="Hanako", page_icon="😺", layout="wide",initial_sidebar_state="collapsed")

# Navigation Bar
page = st_navbar(["Home", "Skills", "Projects", "Contact Me"])

# Load and route to the appropriate page
if page == "Home":
    from pages.about_me import show_about_me
    show_about_me()
elif page == "Skills":
    from pages.skills import show_skills
    show_skills()
elif page == "Projects":
    from pages.projects import show_projects
    show_projects()
elif page == "Contact Me":
    from pages.contact_me import show_contact_me
    show_contact_me()
