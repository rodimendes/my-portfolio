import streamlit as st

st.set_page_config(
    page_title="Rodrigo's Stuff",
    page_icon="🔭",
    layout="centered",
)

CSS = """
h1, h2, h3, h5 {
    text-align: center;
}
"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.markdown("""# Hi, Rodrigo here! 👋""")
st.markdown("##### Data Engineer - Data Scientist")
st.info("")
col1, col2, col3, col4 = st.columns([0.25,1,0.25,3])
col2.image("images/me.png")
col4.markdown(""" **Hi, I am Rodrigo Pinto. I am an aspiring Data Engineer and Data Scientist, current living in Portugal.**  \n**I dedicate my time to personal projects, freelance work, strengthening concepts and learning new tools. Wants to know? I'm discovering many things... I'm interested in remote or hybrid work.**  \n**Below I present some of what I have been developing.**""")
st.write("---")
st.markdown("#### My tech stack")
with st.container():
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    col1.image("images/python.png")
    col2.image("images/sql.png")
    col3.image("images/docker.png")
    col4.image("images/git.png")
    col5.image("images/github.png")
    col6.image("images/html-5.png")
    col7.image("images/css-3.png")
    col8.image("images/plotly.png")
    col9, col10, col11, col12, col13, col14, col15 = st.columns(7)
    col9.write("")
    col9.write("")
    col9.write("")
    col9.image("images/flask.png")
    col10.write("")
    col10.image("images/bs4.png")
    col11.image("images/selenium2.png")
    col12.write("")
    col12.write("")
    col12.image("images/pandas.png")
    col13.write("")
    col13.write("")
    col13.image("images/sklearn.png")
    col14.write("")
    col14.write("")
    col14.image("images/aws.png")
    col15.image("images/seaborn.png")
st.write("---")

col1, col2 = st.columns([1,3], gap="medium")
col1.image("images/my_cv.png", caption="Resume")
col2.markdown("#### Main projects")

with col2:
    tab1, tab2, tab3, tab4 = st.tabs(["Braga's Cafes", "City Categorization", "Data Analysis", "Others"])
    video_file = open("videos/bragas-cafes-presentation.mp4", "rb")
    video_bytes = video_file.read()
    with tab1:
        st.video(video_bytes)
        with st.expander("Read more."):
            st.write("Project that records and displays cafes visited in Braga-PT (more cities may be included), with attribution of specific information for laptop users, such as wifi signal quality, sockets, in addition to the price of coffee and location. It also allows filling out a form for visiting and inclusion on the platform.")

st.components.v1.html('<p><a href="https://www.flaticon.com/free-icons/python" title="python icons">Python icons created by Freepik - Flaticon</a></p>')
