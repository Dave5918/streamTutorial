import streamlit as st

st.title("Hello...This streamlit web app")
st.header("HOLA!")
st.subheader("welcome!")
st.text("""
So, this is what i developed  while
learning the basics of streamlit
from a youtube tutorial, enjoy!.
""")
st.markdown("**Hello**,*world*")
st.caption("..Dave..")

json={
    "Name":"David Omondi",
    "Age":22,
    "Occupation":"student"
}
st.json(json)
code="""
print(hello world)
def count():
    return 0
"""
st.code(code,"python")

#Checkboxes

st.checkbox("accept",value=True)

#radio-buttons
st.radio("What's your gender",options=("male","female","trans","prefer not"))

#button
st.button("Send")

#select boxes...single and multiple
st.selectbox("What's our favorite club",options=("Arsenal","Man Utd","chelsea","spurs"))
st.multiselect("Favorite sport",options=("football","rugby","golf","tennis","soccer","basketball"))

st.write(" ## Upload files")
st.markdown("---") #draws a line

images=st.file_uploader("select an image",type=["png","jpg"],accept_multiple_files=True)
if images is not None:
    st.image(images)

#sliders
st.slider("this is a slider",min_value=0,max_value=100,value=70)

#input
st.text_input("Enter course title",max_chars=60)
st.text_area("Course Description")
st.date_input("Enter registration date")
st.time_input("set timer")

#progress bars
st.markdown("# Progress bar")
st.progress(57)


#forms
st.markdown("# Signing up")
with st.form("Registration form"):
    col1,col2=st.columns(2)
    name1=col1.text_input("First name")
    name2=col2.text_input("Second Name")
    st.text_input("Email")
    st.text_input("Password")
    st.text_input(("Confirm password"))
    state=st.form_submit_button("Submit")
    
    if state:
        if name1=="" and name2=="":
            st.warning("please fill the above fields")
        else:
            st.success("submitted succesfully")

import numpy as np

x=np.linspace(10,20,100)

xbar=["Monday","Tuesday","Wednesday","Thursday","Friday"]
ybar=[10,30,15,45,54]

st.sidebar.markdown("# Side bar")
opt=st.sidebar.radio("Graph",options=("line","bar","scatter"))
import matplotlib.pyplot as plt
if opt == "line" :
    st.markdown("<h1>line graph</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    st.write(fig)
elif opt=="scatter":
    st.markdown("<h1>scatter graph</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.scatter(x,np.sin(x))
    plt.scatter(x,np.cos(x))
    st.write(fig)
elif opt=="bar":
    st.markdown("<h1>bar graph</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.bar(xbar,ybar)
    st.write(fig)
