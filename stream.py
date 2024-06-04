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
    {'id': 'clust', 'label':'Model Klasterisasi'},
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
    
    home_col1a, home_col1b, home_col1c = st.columns([8,1,18])
    with home_col1a:
        st.markdown('<div style="text-align: justify">Selamat datang di <b>Dashboard Tabel IO 2016</b> oleh <b>ANOVAsion Team</b>!</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify">Tabel IO merupakan tools yang menjelaskan aliran transaksi barang dan jasa antar wilayah provinsi dan sektor ekonomi, di mana selain bermanfaat untuk mengetahui karakteristik ekonomi juga berfungsi untuk menentukan kebijakan ekonomi. Tabel IO dapat digunakan untuk melihat wilayah dan sektor ekonomi mana yang harus diatensi, serta wilayah dan sektor ekonomi mana yang menjadi unggulan di suatu negara.</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify">Beberapa analisis pada dashboard ini antara lain:</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify"><li> Analisis deskriptif visualisasi tabel IO, meliputi: analisis PDRB menurut sektor, analisis supply dan demand, analisis struktur output, dll;</li></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify"><li> Analisis keterkaitan, meliputi: keterkaitan antar sektor dalam perekonomian, backward linkage, forward linkage, dan sektor unggulan; </li></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify"><li> Analisis Multiplier Effect, meliputi: analisis pengganda output pendapatan, dan tenaga kerja; </li></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify"><li> Analisis Machine Learning untuk aglomerasi dan klustering sektor usaha dari wilayah provinsi di Indonesia; serta </li></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify"><li> Fitur chatbot yang memudahkan Bank Indonesia dalam menentukan kebijakan moneter terkait pengembangan ekonomi digital dan keuangan berbasis indikator ekonomi makro sektoral tersebut. </li></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify"></div>', unsafe_allow_html=True)

    with home_col1c:
        'Detail informasi dari masing-masing tab pada Dashboard Tabel IO ini aadalah sebagai berikut:'
        st.info('**Home**: Berisi informasi umum dari fitur-fitur yang tersedia dalam dashboard.')
        st.info('**About**: Berisi informasi umum dari kontributor dashboard.')
        st.info('**PDRB**: Berisi tabel dan visualisasi interaktif dari kontribusi ekonomi masing-masing dari 34 provinsi di Indonesia berdasarkan nilai PDRB tahun 2016 dari berbagai sektor/industri berdasarkan tabel IRIO BPS tahun 2016.')
        st.info('**Ekspor-Impor**: Berisi tabel dan visualisasi interaktif dari kontribusi ekonomi masing-masing dari 34 provinsi di Indonesia berdasarkan transaksi ekspor dan impor antar provinsi tahun 2016 dari berbagai sekto/industri berdasarkan tabel IRIO BPS tahun 2016.')
        st.info('**Forward-Backward Linkage**: Berisi tabel dan visualisasi interaktif dari sektor unggulan masing-masing dari 34 provinsi di Indonesia tahun 2016 dari berbagai sektor berdasarkan tabel IRIO BPS tahun 2016.')
        st.info('**Simulasi Pengganda**: Berisi tabel interaktif simulasi sederhana untuk memperoleh total nilai PDRB dari 34 provinsi di Indonesia berdasarkan nilai masukan yang ditentukan pengguna berdasarkan tabel IRIO BPS tahun 2016.')
        st.info('**Model Klasterisasi**: Berisi tabel dan visualisasi interaktif dari klasterisasi 34 provinsi di Indonesia berdasarkan berbagai sektor menggunakan model ML (machine learning).')
        st.info('**Chatbot**: Berisi fitur chatbot untuk memudahkan pengambilan informasi dan interpretasi dari statistik ekonomi dari tabel IO 34 provinsi di Indonesia atau informasi lainnya yang relevan.')

## ------------------------------ TAB ABOUT ------------------------------
if page == 'about':
    st.header('Meet The Team')
    
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = st.columns([2,1,1,1,1,1,1,1,2])
    with p1, p3, p5, p7, p9:
        st.write("")
    with p8:
        st.image("properties/PHOTO-2024-06-04-22-20-18.jpg")
        st.markdown(
            """<div style="text-align: center"> <a href="https://www.linkedin.com/in/dhea-dewanti?originalSubdomain=id/">Dhea Dewanti</a></div>""", unsafe_allow_html=True,
        )
    with p6:
        st.image("properties/PHOTO-2024-06-04-22-20-19.jpg")
        st.markdown(
            """<div style="text-align: center"><a href="https://linkedin/com/in/nurkhamidah">Nur Khamidah</a></div>""", unsafe_allow_html=True,
        )
    with p2:
        st.image("properties/PHOTO-2024-06-04-22-20-17.jpg")
        st.markdown(
            """<div style="text-align: center"> <a href="https://www.linkedin.com/in/alfanugraha/">Alfa Nugraha P</a></div>""", unsafe_allow_html=True,
        )
    with p4:
        st.image("properties/PHOTO-2024-06-04-22-20-18 2.jpg")
        st.markdown(
            """<div style="text-align: center"><a href="https://www.linkedin.com/in/teguhprasetyo08/">Teguh Prasetyo</a></div>""", unsafe_allow_html=True,
        )
    

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
    
    api_key = OpenAI(api_key = os.getenv['OPENAI_API_KEY'])
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