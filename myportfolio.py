import streamlit as st

profile_image = "https://scontent.fceb2-1.fna.fbcdn.net/v/t39.30808-6/323044196_869584374229616_112345477164708761_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=s0yi6v7X2qQQ7kNvgHBApp4&_nc_ht=scontent.fceb2-1.fna&oh=00_AYCW3lo-eF02IsU5AbucIwCYZWbIcflHogqhCG9Amtq6dA&oe=66D4C697"
with st.sidebar:
    st.markdown("[1. Go to Basic Information ](#basic-information)", unsafe_allow_html=True)
    st.markdown("[2. Go to Education ](#education)", unsafe_allow_html=True)
    st.markdown("[3. Go to Contact Information ](#contact-information)", unsafe_allow_html=True)
    st.markdown("[4. Go to Portfolio ](#portfolio)", unsafe_allow_html=True)


st.title("My Autobiography")
st.subheader("Hi! I'm Breshly U. Abanid")
st.image(profile_image, width=400)

st.header("Basic Information")
st.markdown('<a id="basic-information"></a>', unsafe_allow_html=True)
st.write("Name: Breshly U. Abanid")
st.write("Age: 24 years old")
st.write("Birthdate: June 07, 2000")
st.write("Birthplace: Cogon Pardo, Cebu City")
st.divider()

st.header("Education")
st.markdown('<a id="education"></a>', unsafe_allow_html=True)
st.write("I am currently a 4th year college student pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology - University. At the same time, I'm also a working student at the University for almost 4 years.")
st.divider()

st.header("Contact Information")
st.markdown('<a id="contact-information"></a>', unsafe_allow_html=True)
st.write("Phone number: 09662466020")
st.write("Email: breshlyabanid@cit.edu")
st.write("Linked Profile: www.linkedin.com/in/breshly-abanid-281558277")
st.write("Facebook:  https://www.facebook.com/breshly.abanid")

st.divider() 
st.header("Portfolio")
st.markdown('<a id="portfolio"></a>', unsafe_allow_html=True)
st.write("Here are some of my personal project I made at school.")
st.subheader("1. UI Design for Cybersecurity App")
with st.expander("Click to see images"):
    image_paths = ["images/1.png", "images/2.png", "images/3.png", "images/4.png", "images/5.png", "images/6.png", "images/7.png", "images/8.png"]

    # Create two columns
    col1, col2 = st.columns(2)

    # Display images in two columns
    with col1:
        for i in range(0, len(image_paths), 2):  # Display every other image in the first column
            st.image(image_paths[i], use_column_width=True, caption=f"Image {i+1}")

    with col2:
        for i in range(1, len(image_paths), 2):  # Display the remaining images in the second column
            st.image(image_paths[i], use_column_width=True, caption=f"Image {i+2}")

