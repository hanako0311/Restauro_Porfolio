import streamlit as st

def show_skills():
    # Container for the page layout with margins on the sides
    margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

    with body:
        st.header("Skills", divider='rainbow')

        st.write("### Technologies and Tools")

        # Frontend Skills
        st.write("#### Frontend")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="badge-container"><a href="https://reactjs.org/" class="badge"><img src="https://img.icons8.com/color/48/000000/react-native.png"/>ReactJS</a></div>', unsafe_allow_html=True)
            st.markdown('<div class="badge-container"><a href="https://vitejs.dev/" class="badge"><img src="https://vitejs.dev/logo.svg" alt="Vite" height="20"/>Vite</a></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="badge-container"><a href="https://tailwindcss.com/" class="badge"><img src="https://img.icons8.com/color/48/000000/tailwind-css.png"/>Tailwind</a></div>', unsafe_allow_html=True)
            st.markdown('<div class="badge-container"><a href="https://www.figma.com/" class="badge"><img src="https://img.icons8.com/color/48/000000/figma.png"/>Figma</a></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="badge-container"><a href="https://www.canva.com/" class="badge"><img src="https://img.icons8.com/color/48/000000/canva.png"/>Canva</a></div>', unsafe_allow_html=True)

        # Backend Skills
        st.write("#### Backend")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="badge-container"><a href="https://nodejs.org/" class="badge"><img src="https://img.icons8.com/color/48/000000/nodejs.png"/>NodeJS</a></div>', unsafe_allow_html=True)
            st.markdown('<div class="badge-container"><a href="https://expressjs.com/" class="badge"><img src="https://img.icons8.com/ios-filled/48/000000/express-js.png"/>Express</a></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="badge-container"><a href="https://spring.io/projects/spring-boot" class="badge"><img src="https://img.icons8.com/color/48/000000/spring-logo.png"/>Spring Boot</a></div>', unsafe_allow_html=True)
            st.markdown('<div class="badge-container"><a href="https://www.mongodb.com/" class="badge"><img src="https://img.icons8.com/color/48/000000/mongodb.png"/>MongoDB</a></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="badge-container"><a href="https://www.mysql.com/" class="badge"><img src="https://img.icons8.com/color/48/000000/mysql-logo.png"/>SQL</a></div>', unsafe_allow_html=True)
            st.markdown('<div class="badge-container"><a href="https://www.python.org/" class="badge"><img src="https://img.icons8.com/color/48/000000/python.png"/>Python</a></div>', unsafe_allow_html=True)

        # Tools
        st.write("#### Tools")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="badge-container"><a href="https://www.postman.com/" class="badge"><img src="https://img.icons8.com/dusk/64/000000/postman-api.png"/>Postman</a></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="badge-container"></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="badge-container"></div>', unsafe_allow_html=True)
