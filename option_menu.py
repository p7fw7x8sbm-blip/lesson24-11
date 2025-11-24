import streamlit as st
from streamlit_option_menu import option_menu

st.title('Hello, Students!')
st.write('This is your Python Programming course.')

with st.sidebar:                                          # create new area
    selected=option_menu(                                 # customize option menu
        menu_title = "Menu",
        options = ["ISOM3400", "About", "Contact"],           # use list [] ; names within side bar
        icons = ["house", "cloud-upload", "list-task"],       # symbols within side bar
        menu_icon= "cast",
        default_index=0,
    )

if selected == "ISOM3400":  # make sure it matches with the options "" above 
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")
