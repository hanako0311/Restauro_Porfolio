import streamlit as st
from streamlit_lottie import st_lottie
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
        st.header("Projects")  # Removed divider argument

        st_lottie(projects_animation, height=300, key="projects")

        st.write("### Featured Projects")

        # Custom CSS for card styling
        st.markdown("""
            <style>
            .card {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                text-align: center;
            }
            .card h3 {
                color: #333;
                font-size: 24px;
                margin-bottom: 10px;
            }
            .card p {
                color: #555;
                font-size: 16px;
            }
            .card a {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 15px;
                color: white;
                background-color: #dc143c;
                border-radius: 5px;
                text-decoration: none;
                font-weight: bold;
            }
            .card a:hover {
                background-color: #bf0f35;
            }
            .card .app-link {
                margin-right: 10px;
                background-color: #4CAF50;
            }
            .card .app-link:hover {
                background-color: #45A049;
            }
            </style>
        """, unsafe_allow_html=True)

        # Create project cards with images and links
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div class="card">
                    <h3>FindNest - Advanced Lost and Found Management System</h3>
                    <p>FindNest is an innovative digital solution designed to streamline and enhance the lost and found process at CIT-University. 
                    This system automates traditional manual procedures, making it easier for students, faculty, and staff to report and claim lost items efficiently. 
                    With a user-friendly interface and a strong focus on security, FindNest offers a comprehensive platform that integrates the reporting, tracking, and management of lost and found items.</p>
                    <a href="https://github.com/hanako0311/FindNest" class="app-link">View on GitHub</a>
                    <a href="https://findnest.onrender.com/" class="app-link">View Deployed App</a>
                </div>
            """, unsafe_allow_html=True)

            # Display image using Streamlit's st.image inside the card
            st.image("public/FindNest.png", use_column_width=True)
        
        with col2:
            st.markdown("""
                <div class="card">
                    <h3>Nexa-Ai - AI Chatbot with PDF Reading</h3>
                    <p>Nexa-Ai is an AI-powered chatbot developed using Azure OpenAI services, with the unique capability of reading and processing PDFs. 
                    This project uses Streamlit for the frontend interface and seamlessly integrates with Azure OpenAI's API to deliver intelligent and responsive interactions.</p>
                    <a href="https://github.com/hanako0311/Nexa-Ai" class="app-link">View on GitHub</a>
                    <a href="https://nexa-ai.streamlit.app/" class="app-link">View Deployed App</a>
                </div>
            """, unsafe_allow_html=True)

            # Display image using Streamlit's st.image inside the card
            st.image("public/NexaAi.png", use_column_width=True)
