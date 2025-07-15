import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import locale 
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide")

st.header('Plano de Máquina')

#configurar uma forma de salvar os dados em banco de dados 


# Botão "Salvar Tudo"
if st.button("Salvar Tudo"):
    st.success("Dados salvos com sucesso! (Funcionalidade de salvamento ainda precisa ser implementada)")
    # Aqui você adicionaria a lógica para processar e salvar os dados
    # Por exemplo, coletar os dados dos inputs e enviá-los para um banco de dados ou CSV.


maquinas = [
        'PICOTADEIRA 01', 'PICOTADEIRA 02', 'PICOTADEIRA 03', 'PICOTADEIRA 04',
        'PICOTADEIRA 05', 'PICOTADEIRA 06', 'PICOTADEIRA 07','PICOTADEIRA 08',
        'PICOTADEIRA 09','PICOTADEIRA 10','PICOTADEIRA 11','PICOTADEIRA 12'
    ]


dados_maquinas = {}

for maquina in maquinas:
        st.header(maquina)
        
        # Criar uma tabela (DataFrame) para cada máquina para facilitar a entrada de dados
        # Vamos inicializar com colunas vazias
        colunas = [
            "Num Carga", "Tipo Material", "Cliente", "Ordem Produção", "Material",
            "Qtd Fardos", "Qtd kg", "Qtd unid", "Data hora Inicial", "Data hora Final",
            "Bobina Usada", "Observação"
        ]
        
        # Cria um DataFrame vazio com as colunas e 10 linhas para entradas
        df_maquina = pd.DataFrame(columns=colunas, index=range(8))

        # Usar st.data_editor para uma tabela editável
        st.write(f"Preencha os dados para {maquina}:")
        edited_df = st.data_editor(
            df_maquina,
            num_rows="dynamic", # Permite adicionar ou remover linhas
            column_config={
                "Num Carga": st.column_config.TextColumn("Num Carga", help="Número da carga", default=""),
                "Tipo Material": st.column_config.TextColumn("Tipo Material", help="Tipo de material", default=""),
                "Cliente": st.column_config.TextColumn("Cliente", help="Nome do cliente", default=""),
                "Ordem Produção": st.column_config.NumberColumn("Ordem Produção", help="Número da ordem de produção", default=0, format="%d"),
                "Material": st.column_config.TextColumn("Material", help="Tipo de material", default=""),
                "Qtd Fardos": st.column_config.NumberColumn("Qtd Fardos", help="Quantidade de fardos", default=0, format="%d"),
                "Qtd kg": st.column_config.NumberColumn("Qtd kg", help="Quantidade em kg", default=0.0, format="%.2f"),
                "Qtd unid": st.column_config.NumberColumn("Qtd unid", help="Quantidade em unidades", default=0, format="%d"),
                "Data hora Inicial": st.column_config.DatetimeColumn("Data hora Inicial", help="Data e hora de início", format="YYYY-MM-DD HH:mm:ss"),
                "Data hora Final": st.column_config.DatetimeColumn("Data hora Final", help="Data e hora final", format="YYYY-MM-DD HH:mm:ss"),
                "Bobina Usada": st.column_config.TextColumn("Bobina Usada", help="Informações da bobina utilizada", default=""),
                "Observação": st.column_config.TextColumn("Observação", help="Observações adicionais", default="")
            },
            key=f"editor_{maquina}" # Chave única para cada editor de dados
        )

        dados_maquinas[maquina] = edited_df
    



