import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_card import card
import requests

# Load Lottie animation (optional)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

projects_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json")

def show_projects():
    # Container for the page layout with margins on the sides
    margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

    with body:
        st.header("Projects", divider='rainbow')

        st_lottie(projects_animation, height=300, key="projects")

        st.write("### Featured Projects")

        col1, col2 = st.columns(2)
        with col1:
            card(title="Project 1", text="Description of project 1.", image="https://via.placeholder.com/150")
            card(title="Project 3", text="Description of project 3.", image="https://via.placeholder.com/150")
        with col2:
            card(title="Project 2", text="Description of project 2.", image="https://via.placeholder.com/150")
            card(title="Project 4", text="Description of project 4.", image="https://via.placeholder.com/150")
