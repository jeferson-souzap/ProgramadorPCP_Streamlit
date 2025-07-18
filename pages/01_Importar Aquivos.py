import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import locale
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

from fontTools.misc.cython import returns
from numpy.matlib import empty
from sympy.codegen.ast import none

from utils.config_cadastro import tratamento_cadastro, importar_cadastro
from db.config_db import LOCAL_BANCO


st.header('Importe arquivos de cadastro e configuração')

# CONFIGURAÇÃO DA PAGINA
st.set_page_config(layout='wide', page_title='Cadastro Material', initial_sidebar_state="collapsed")
# st.set_page_config(page_title='Cadastro Material', initial_sidebar_state="collapsed")
st.header('Cadastro de produtos')


# FUNÇÕES E PROCEDIMENTOS
@st.cache_data
def carregar_dados():
    try:
        conn = sqlite3.connect(LOCAL_BANCO)
        tab_cadastro = pd.read_sql_query("SELECT * FROM cadastro_material", conn)
        conn.close()
        return tab_cadastro
    except sqlite3.Error as e:
        st.error(f"Erro ao conectar no banco: {e}")
        return pd.DataFrame()




with st.expander("Arquivo de cadastro AC4"):



with st.expander('Importar relatório', expanded=False):
    # st.subheader("Importe o relatório de produtos ACE4")
    arquivo_cadastro = st.file_uploader("--", type=["xlsx", "xls"])
    df_cadastro = tratamento_cadastro(arquivo_cadastro)
    importar_cadastro(df_cadastro, 'cadastro_material')
