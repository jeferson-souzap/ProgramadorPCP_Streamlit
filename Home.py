import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import locale

import seaborn as sns


#CONFIGURAÇÃO PAGINA
st.set_page_config(layout='wide', page_title='Inicio', page_icon='🏠', initial_sidebar_state="collapsed")
st.header('Indicadores de produção de Vidro')


#CONFIGURAÇÃO DATAFRAME
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

data_atual = datetime.now()

largura_grafico = 18
altura_grafico = 6


col1, col2, col3 = st.columns(3)


with col1:
    st.info(f'Total de Pedidos - {55}')

with col2:
    st.info(f'Pedidos em Aberto - {50}')
