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
if page == 'home':
    st.header('Introduction to The Project')
    
    
    

## ------------------------------ TAB ABOUT ------------------------------
if page == 'about':
    st.header('Introduction to The Team')

## ------------------------------ TAB PDRB ------------------------------
if page == 'pdrb':
    st.header('Produk Domestik Regional Bruto (PDRB) 34 Provinsi')

## ------------------------------ TAB EKSIM ------------------------------
if page == 'eksim':
    st.header('Alur Transaksi Ekspor-Impor antar 34 Provinsi')

## ------------------------------ TAB FLBL ------------------------------
if page == 'flbl':
    st.header('Sektor Unggulan 34 Provinsi berdasarkan Forward & Backward Linkage')

## ------------------------------ TAB SIMULATION ------------------------------
if page == 'simul':
    st.header('Simulasi Perhitungan PDRB berdasarkan Provinsi dan Industri')

## ------------------------------ TAB CLUSTERING ------------------------------
if page == 'clust':
    st.header('Analisis Klasterisasi 34 Provinsi di Indonesia dari Berbagai Sektor')

## ------------------------------ TAB CHATBOT ------------------------------
if page == 'chat':
    st.header('Chatbot IRIO Indonesia')
    
    api_key = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])
    @st.cache_resource(show_spinner=False)
    def load_data():
        with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."):
            reader = SimpleDirectoryReader(input_dir="./corpus", recursive=True)
            docs = reader.load_data()
            service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features."))
            index = VectorStoreIndex.from_documents(docs, service_context=service_context)
            return index

    index = load_data()
    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages: 
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Silakan input keyword tentang hasil analisis table IRIO..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
                st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) 