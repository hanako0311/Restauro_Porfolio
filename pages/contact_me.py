import streamlit as st

def show_contact_me():
    # Container for the page layout with margins on the sides
    margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

    with body:
        st.header("Contact Me", divider='rainbow')

        st.write("### Get in touch")

        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message")

            submit_button = st.form_submit_button(label="Send")
            if submit_button:
                st.success("Message sent successfully!")
                # Here you'd add your email sending logic
