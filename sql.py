import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    choose = option_menu("SQL workshop",
                         ["About", 
                          "join", 
                          "aggregate", "string"
                             , "order by", "limit", "Algorithm theory and principle"],
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
