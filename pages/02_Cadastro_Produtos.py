import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import locale 
import matplotlib.pyplot as plt
import seaborn as sns

from utils.config_cadastro import tratamento_cadastro

#CONFIGURAÇÃO DA PAGINA
st.set_page_config(layout='wide', page_title='Cadastro Material', initial_sidebar_state="collapsed")

st.header('Cadastro de produtos')

#-----------------------

with st.expander('Importar relatório', expanded=False):
    #st.subheader("Importe o relatório de produtos ACE4")
    df_cadastro = st.file_uploader("--", type=["xlsx", "xls"])


tratamento_cadastro(df_cadastro)    

