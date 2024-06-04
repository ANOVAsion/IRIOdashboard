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
    opt_skala = st.toggle("Skala Provinsi")
    if opt_skala:
        pd_col1a, pd_col1b = st.columns([3,7])
        with pd_col1a:
            with st.container(border=True):
                jenis_pdrb = st.radio(label='**Pilih jenis PDRB :**', 
                                    options=['PRODUKSI', 'PENDAPATAN', 'PENGELUARAN'])
            with st.container(border=True):
                if jenis_pdrb == 'PRODUKSI':
                    opt_sektor = opt_sektor_prod
                elif jenis_pdrb == 'PENDAPATAN':
                    opt_sektor = opt_sektor_pend
                else:
                    opt_sektor = opt_sektor_peng
                if st.checkbox('Semua Sektor'):
                    sektor = st.multiselect('**Pilih Sektor**',
                                                                opt_sektor,
                                                                disabled=True)
                    sektor =  opt_sektor.tolist()
                else:
                    sektor =  st.multiselect('**Pilih Sektor**',
                                                                opt_sektor)
            with st.container(border=True):
                if st.checkbox('Semua Provinsi'):
                    provinsi = st.multiselect('**Pilih Provinsi**',
                                                                opt_provinsi,
                                                                disabled=True)
                    provinsi =  opt_provinsi.tolist()
                else:
                    provinsi =  st.multiselect('**Pilih Provinsi**',
                                                                opt_provinsi)
        with pd_col1b:   
            dat1, fig1 = plotBerdasarkanJenisPDRB(jenis_pdrb, provinsi, sektor)
            st.dataframe(dat1[['nama_prov', 'jenis_pdrb', 'nama_komp', 'nilai_jt']], use_container_width=True)
        st.plotly_chart(fig1, use_container_width=True)
        
    else:
        pd_col3a, pd_col3b = st.columns([3,7])
        with pd_col3a:
            with st.container(border=True):
                jenis_pdrb = st.radio(label='**Pilih jenis PDRB :**', 
                                    options=['PRODUKSI', 'PENDAPATAN', 'PENGELUARAN'])
            with st.container(border=True):
                if jenis_pdrb == 'PRODUKSI':
                    opt_sektor = opt_sektor_prod
                elif jenis_pdrb == 'PENDAPATAN':
                    opt_sektor = opt_sektor_pend
                else:
                    opt_sektor = opt_sektor_peng
                if st.checkbox('Semua Sektor'):
                    sektor = st.multiselect('**Pilih Sektor**',
                                                                opt_sektor,
                                                                disabled=True)
                    sektor =  opt_sektor.tolist()
                else:
                    sektor =  st.multiselect('**Pilih Sektor**',
                                                                opt_sektor)
                max_slider = len(df_pdrb_nasional[df_pdrb_nasional['jenis_pdrb'] == jenis_pdrb])
                n_sektor = st.slider("**Tentukan banyak sektor:**",
                                        min_value=1, max_value=max_slider)     
        with pd_col3b:   
            dat2, fig2 = plotNasionalBerdasarkanJenisPDRB(jenis_pdrb, sektor, n_sektor)
            st.dataframe(dat2[['nama_komp', 'nilai_jt']].sort_values(['nilai_jt'], ascending=False), use_container_width=True)
        pd_col4a, pd_col4b = st.columns([3,7])
        with pd_col4a:
            sum_pdrb = dat2['nilai_jt'].head(n_sektor).sum()
            st.metric("**Total PDRB:**", value = 'Rp ' + str((sum_pdrb/1000000).round(3)) + ' T')
        with pd_col4b:
            st.plotly_chart(fig2, use_container_width=True)

## ------------------------------ TAB EKSIM ------------------------------
if page == 'eksim':
    st.header('Alur Transaksi Ekspor-Impor antar 34 Provinsi')
    eks0a, eks_col1a, eks_col1b, eks0b, eks_col1c = st.columns([2,2,3,1,3])
    with eks_col1a:
        eks_fil1 = st.radio('**Pilih Kriteria**', ['Industri', 'Provinsi'])
    with eks_col1b :
        if eks_fil1 == 'Industri':
            eks_fil2 = st.selectbox('**Pilih Industri:**', opt_eksim_ind)
        else :
            eks_fil2 = st.selectbox('**Pilih Provinsi:**', opt_provinsi)
    with eks_col1c:
        eks_fil3 = st.radio('**Pilih Jenis Transaksi:**', ["Ekspor antar Provinsi", "Impor antar Provinsi", "Net Ekspor"])
    data_eks = filterTableEksim(crit=eks_fil1, crit2=eks_fil2, jenis=eks_fil3)
    with st.expander('**Tabel {} {} Berdasarkan {}**'.format(eks_fil3, eks_fil2, eks_fil1), expanded=True):
        st.dataframe(data_eks, use_container_width=True, height=600)
    
    dat3 = makeTableEksImp(crit=eks_fil1, crit2=eks_fil2, jenis=eks_fil3)
    fig3 = plotSpatial(dat3)
    eks_col2a, eks_col2b = st.columns([1,4])
    with eks_col2b:
        if eks_fil3 == "Impor antar Provinsi":
            st.markdown('<div style="text-align:center"><b>{} dari {} {} menurut Provinsi Asal (Miliar Rupiah)</b></div>'.format(eks_fil3, eks_fil1, eks_fil2), 
                        unsafe_allow_html=True)
        else:
            st.write('<div style="text-align:center"><b>{} dari {} {} menurut Provinsi Tujuan (Miliar Rupiah)</b></div>'.format(eks_fil3, eks_fil1, eks_fil2),
                    unsafe_allow_html=True)
        st.plotly_chart(fig3, use_container_width=True)
    with eks_col2a:
        '**PERDAGANGAN ANTAR PROVINSI**'
        nil_eks = get_total_eksim(crit = eks_fil1, crit2 = eks_fil2, data_eksim=df_eksim)[0]['nilai_mil']
        nil_imp = get_total_eksim(crit = eks_fil1, crit2 = eks_fil2, data_eksim=df_eksim)[1]['nilai_mil']
        st.metric('**Nilai Ekspor:**', 'Rp {} T'.format((nil_eks/1000).round(2)))
        st.metric('**Nilai Impor:**', 'Rp {} T'.format((nil_imp/1000).round(2)))
        if nil_imp > nil_eks:
            st.metric('**Defisit:**', 'Rp {} T'.format(((nil_imp - nil_eks)/1000).round(2)))
        else:
            st.metric('**Surplus:**', 'Rp {} T'.format(((nil_eks - nil_imp)/1000).round(2)))
            
    eks_col3a, eks_col3b = st.columns([1,1])
    eks_col4a, eks_col4b, eks_col4c = st.columns([1,1,1])
    df_4a = makeTableEksImp(crit = eks_fil1, crit2 = eks_fil2, jenis=eks_fil3).sort_values(['nilai_mil'], ascending = False)
    with eks_col4b:
        eks_slid = st.slider('**Masukkan Banyak Provinsi yang Ditampilkan**', 1, len(df_4a))
    with eks_col3a:
        st.markdown('<div style="text-align:center"><b>Visualisasi {} {} dengan {} Teratas</b></div>'.format(eks_slid, eks_fil1, eks_fil3), unsafe_allow_html=True)
        fig4a = makeBarChart(df_4a.head(eks_slid), colx = 'kode_prov', coly = 'nilai_mil')
        st.plotly_chart(fig4a, use_container_width = True)
    with eks_col3b:
        st.markdown('<div style="text-align:center"><b>Visualisasi {} {} dengan {} Terbawah</b></div>'.format(eks_slid, eks_fil1, eks_fil3), unsafe_allow_html=True)
        df_4b = makeTableEksImp(crit = eks_fil1, crit2 = eks_fil2, jenis=eks_fil3).sort_values(['nilai_mil'], ascending = True)
        fig4b = makeBarChart(df_4b.head(eks_slid), colx = 'kode_prov', coly = 'nilai_mil')
        st.plotly_chart(fig4b, use_container_width = True)

## ------------------------------ TAB FLBL ------------------------------
if page == 'flbl':
    st.header('Sektor Unggulan 34 Provinsi berdasarkan Forward & Backward Linkage')
    
    lin_col1a, lin_col1b = st.columns([2,5])
    with lin_col1a:
        lin_prov = st.selectbox('**Pilih Provinsi:**', opt_provinsi)
        st.write('**Industri Unggulan Provinsi {} Berdasarkan Forward-Backward Linkage**'.format(lin_prov))
        lin_df, lin_fig1 = makeScatterPlotFLBL(df_flbl, lin_prov)
        unggulan_f_id = lin_df['nama_ind'][lin_df['n_forward'].idxmax()]
        unggulan_b_id = lin_df['nama_ind'][lin_df['n_backward'].idxmax()]
        st.metric('Forward Linkage', value=unggulan_f_id)
        st.metric('Backward Linkage', value=unggulan_b_id)
        
    with lin_col1b:
        st.plotly_chart(lin_fig1, use_container_width=True)

    lin_col2a, lin_col2b, lin_col2c = st.columns([1,1,1])
    with lin_col2b : 
        lin_slid1 = st.slider('**Masukkan Banyak Industri yang Ingin Ditampilkan:**', 1, len(lin_df))

    lin_col3a, lin_col3b = st.columns([1,1])
    with lin_col3a:
        lin_fig2a = makeBarChart(lin_df.sort_values('n_forward', ascending=False).head(lin_slid1), colx='nama_ind', coly='n_forward')
        st.plotly_chart(lin_fig2a)
    with lin_col3b:
        lin_fig2b = makeBarChart(lin_df.sort_values('n_backward', ascending=False).head(lin_slid1), colx='nama_ind', coly='n_backward')
        st.plotly_chart(lin_fig2b)

## ------------------------------ TAB SIMULATION ------------------------------
if page == 'simul':
    st.header('Simulasi Perhitungan PDRB berdasarkan Provinsi dan Industri')
    
    sim_col1a, sim_col1b, sim_col1c = st.columns([1,1,1])
    with sim_col1a:
        '**Cari Berdasarkan:**'
        sim_opt1 = st.checkbox('Provinsi')
        sim_opt2 = st.checkbox('Industri')
    with sim_col1b:         
        if sim_opt1:
            sim_prov = st.selectbox('**Pilih Provinsi:**', opt_provinsi)
            sim_prov = [sim_prov]
        else:
            sim_prov = opt_provinsi 
        if sim_opt2:
            sim_ind = st.selectbox('**Pilih Industri:**', opt_ind)
            sim_ind = [sim_ind]
        else: 
            sim_ind = opt_ind
    df_sim = base_irio[base_irio['nama_prov'].isin(sim_prov)][base_irio['nama_ind'].isin(sim_ind)]   
    row_number = st.number_input('Number of rows', min_value=0, value=len(df_sim)) 
    
    defaultColDef = {
        "filter": True,
        "resizable": True,
        "sortable": True,
    }
    
    options = {
        "rowSelection": "multiple",
        "rowMultiSelectWithClick": True,
        "enableRangeSelection": True,
    }
    options_builder = GridOptionsBuilder.from_dataframe(df_sim)
    options_builder.configure_default_column(**defaultColDef)
    options_builder.configure_grid_options(**options)
    options_builder.configure_column('target', editable=True)
    grid_options = options_builder.build()
    df_eksim2 = AgGrid(df_sim, gridOptions=grid_options,
                       height=600,
                       fit_columns_on_grid_load=True,
                       header_checkbox_selection_filtered_only=True,
                       allow_unsafe_jscode=True)
    data = df_eksim2['data']

    sim_base, sim_sim = simulationIRIO(data)
    with sim_col1c:
        sim_col1c_1, sim_col1c_2 = st.columns([1,1])
        with sim_col1c_1:
            st.metric('**Nilai PDRB Awal:**', 'Rp ' + str((sim_base).round(3)) + ' T')
        with sim_col1c_2:
            st.metric('**Nilai PDRB Akhir:**',  'Rp ' + str((sim_sim).round(3)) + ' T')

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