import streamlit as st 
import pandas as pd
import plotly.express as px

def page1():
    st.title('Apresentação pessoal')
    st.write('Conteúdo da página 1')

def page2():
    st.title('Conteudos Sobre a Cyrela')
    st.write('Conteúdo da página 2')

def page3():
    st.title('Apresentação do Case')
    st.write('Conteúdo da página 3')

# Criando o seletor de abas
page = st.sidebar.selectbox('Selecione a página', ('Apresentação pessoal', 'Sobre a Cyrela', 'Apresentação do Case'))

# Renderizando a página selecionada
if page == 'Apresentação pessoal':
    page1()
elif page == 'Sobre a Cyrela':
    page2()
elif page == 'Apresentação do Case':
    page3()


