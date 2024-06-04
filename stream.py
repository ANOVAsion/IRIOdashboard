import streamlit as st
from data import *
import hydralit_components as hc

st.set_page_config(
    page_title="ANOVAtion Prototype",
    page_icon="💸",
    layout='wide',
)

## ------------------------------ NAVBAR ------------------------------

st.markdown('<h1 style="text-align:center"><b>TABLE IRIO BPS 2016 - ANOVAtion PROTOTYPE</b></h1>', unsafe_allow_html=True)

menu_data = [
    {'id': 'home', 'label':'Home'},
    {'id': 'about', 'label':'About'},
    {'id': 'pdrb', 'label':'PDRB'},
    {'id': 'eksim', 'label':'Ekspor-Impor'},
    {'id': 'flbl', 'label':'Forward-Backward Linkage'},
    {'id': 'simul', 'label':'Simulasi Pengganda'},
    {'id': 'clust', 'label':'Model Segmentasi'},
    {'id': 'chat', 'label':'Chatbot'}    
]

over_theme = {'txc_inactive': '#FFFFFF'}

page = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=False,
    sticky_nav=True, 
    sticky_mode='pinned', 
)

## ------------------------------ TAB HOME ------------------------------

## ------------------------------ TAB ABOUT ------------------------------


## ------------------------------ TAB PDRB ------------------------------


## ------------------------------ TAB EKSIM ------------------------------


## ------------------------------ TAB FLBL ------------------------------


## ------------------------------ TAB SIMULATION ------------------------------


## ------------------------------ TAB CLUSTERING ------------------------------


## ------------------------------ TAB CHATBOT ------------------------------
