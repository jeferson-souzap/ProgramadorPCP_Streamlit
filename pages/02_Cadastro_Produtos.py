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

#CONFIGURAÇÃO DA PAGINA
st.set_page_config(layout='wide', page_title='Cadastro Material', initial_sidebar_state="collapsed")
#st.set_page_config(page_title='Cadastro Material', initial_sidebar_state="collapsed")
st.header('Cadastro de produtos')


#FUNÇÕES E PROCEDIMENTOS
@st.cache_data
def carregar_dados():
    try:
        conn = sqlite3.connect(LOCAL_BANCO)
        tab_cadastro = pd.read_sql_query("SELECT * FROM cadastro_material", conn)
        conn.close()
        return  tab_cadastro
    except sqlite3.Error as e:
        st.error(f"Erro ao conectar no banco: {e}")
        return pd.DataFrame()


with st.expander('Importar relatório', expanded=False):
    #st.subheader("Importe o relatório de produtos ACE4")
    arquivo_cadastro = st.file_uploader("--", type=["xlsx", "xls"])
    df_cadastro = tratamento_cadastro(arquivo_cadastro)
    importar_cadastro(df_cadastro, 'cadastro_material')

with st.expander('Edição cadastro', expanded=True):
    cad_col01, cad_col02, cad_col03 = st.columns(3)

    with cad_col01:
        cod_produto = st.text_input('Código produto: ')
        cod_grupo = st.text_input('Código de grupo:')
        descricao = st.text_input('Descrição material', key='descr_01')
        #descricao_detalhada = st.text_input('Descrição material', key='descr_02')


    with cad_col02:
        unidade_med = st.text_input('Unidade Medida')
        peso = st.number_input('Peso liquido:', min_value=0.0, max_value=100.0)
        peso_bruto = st.number_input('Peso Bruto:', min_value=0.0, max_value=100.0)

    with cad_col03:
        qtd_embalagem = st.number_input('Quantidade bobinas no fardo: ', min_value=0, max_value=10)
        peso_fardo = float(peso_bruto) * int(qtd_embalagem)
        st.text(f"Peso de Fardo = {peso_fardo}")
        #st.text_input('Peso do fardo', value=peso_fardo)


with st.expander("Cadastro de Material", expanded=True):
    bt_col01, bt_col02 = st.columns(2)

    with bt_col01:
        if st.button('Salvar Alterações'):
            pass

    with bt_col02:
        if st.button('Salvar Deletar'):
            pass


    linha_selecionada = st.dataframe(carregar_dados(),
                 on_select='rerun',
                 selection_mode='single-row',
                 hide_index=True,
                 key='data_frame'
                 )
    st.text(linha_selecionada)
    #Vai funcionar desse jeito só falta implementar a lógica de carregamento, edição e o botão de excluir


