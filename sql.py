import streamlit as st
!pip install streamlit-option-menu
with st.sidebar:
    choose = option_menu("DS Project",
                         ["About", 
                          "Toronto condo price prediction", 
                          "Condo clustering", "Condo search engine"
                             , "Multi-criteria ranked condos", "Talk to AI Libby", "Algorithm theory and principle"],
                         icons=['fingerprint', 'house fill', 'kanban', 'google', 'award', 'robot', 'book'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#fafafa"},
                             "icon": {"color": "orange", "font-size": "18px"},
                             "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px",
                                          "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#02ab21"},
                         }
                         )
