import streamlit as st

def show_about_me():
    # Container for the page layout with margins on the sides
    margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

    # Info to be displayed in the About Me section
    info = {
        'name': 'Hannah Restauro',
        'study': 'BS Information Technology',
        'location': 'Cebu City, Philippines',
        'interest': 'Curiosity-Driven Learning',
        'brief': (
            "Hello! I'm Hannah, an IT student at Cebu Institute of Technology, driven by a deep curiosity and a commitment to learning. "
            "My journey into IT wasn't my original plan, but it has become a path where I've discovered a passion for technology's role in shaping the future. "
            "While Veterinary Medicine was my first dream, practical considerations led me to choose IT—a field full of opportunities and challenges. "
            "Now in my fourth year, I'm embracing this journey with an open mind, eager to explore where my strengths and interests align in this ever-evolving digital world."
        ),
        'linkedin': "www.linkedin.com/in/hannah-restauro-0bb679179"
    }

    # Main content body
    with body:
        # Large introduction at the top
        st.markdown("<h1 style='font-size: 4rem; font-weight: bold; color: #dc143c;'>HI, I'm Hannah Restauro</h1>", unsafe_allow_html=True)

        # Header with a rainbow divider
        st.header("About Me", divider='rainbow')

        # Columns for text and image
        col1, col2, col3 = st.columns([1.3, 0.2, 1])

        with col1:
            # Display brief and other information
            st.write(info['brief'])
            st.markdown(f"###### 🧑‍🎓 Who I Am: {info['name']} - A {info['study']} student")
            st.markdown(f"###### 🏙️ Where I'm Based: {info['location']}")
            st.markdown(f"###### 🚀 What Drives Me: {info['interest']}")
            st.markdown("###### 🔴 My Favorite Color: Crimson Red - symbolizing energy and determination")
            st.markdown(f"###### 🔗 Let's Connect: [LinkedIn]({info['linkedin']})")

            # Resume download button
            with open("public/resume.pdf", "rb") as file:
                pdf_file = file.read()

            st.download_button(
                label="Download my :blue[resume]",
                data=pdf_file,
                file_name="Hannah_Restauro_Resume.pdf",
                mime="application/pdf"
            )

        # Display the image in the second column
        with col3:
            st.image("public/Hannah.jpg", width=360)  # Replace with your actual image path
