import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

#colocando logo na sidebar
image = Image.open('Logo-Cyrela.png')
st.sidebar.image(image,caption='',use_column_width=True)
st.sidebar.markdown('Apresentação Pessoal - Bruno Zocatelli')

#definindo as paginas 
def page1():
    
    st.title('Apresentação Pessoal')
    image = Image.open('AP1.png')
    st.image(image,caption='',use_column_width=True)

    image = Image.open('AP2.png')
    st.image(image,caption='',use_column_width=True)

    image = Image.open('AP3.png')
    st.image(image,caption='',use_column_width=True)
    
def page2():
    st.title('Habilidades')

    image = Image.open('HR1.png')
    st.image(image,caption='',use_column_width=True)

    image = Image.open('HR2.png')
    st.image(image,caption='',use_column_width=True)

    image = Image.open('HR3.png')
    st.image(image,caption='',use_column_width=True)

    image = Image.open('HR4.png')
    st.image(image,caption='',use_column_width=True)

def page3():
    st.title('Minha Trajetória e Visão de Futuro')

    image = Image.open('MT1.png')
    st.image(image,caption='',use_column_width=True)

# Criando o seletor de abas
page = st.sidebar.selectbox('Selecione a página', ('Apresentação pessoal', 'Habilidades', 'Minha Trajetória'))

# Renderizando a página selecionada
if page == 'Apresentação pessoal':
    page1()
elif page == 'Habilidades':
    page2()
elif page == 'Minha Trajetória':
    page3()


