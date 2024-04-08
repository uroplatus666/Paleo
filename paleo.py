import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")


@st.cache_resource()
def load_model_1(model_name_1):
    C_N = pd.read_csv(model_name_1)
    return (C_N)


C_N = load_model_1('https://raw.githubusercontent.com/uroplatus666/Paleo/master/C_N.csv')


@st.cache_resource()
def load_model_2(model_name_2):
    gran = pd.read_csv(model_name_2)
    return (gran)


gran = load_model_2('https://raw.githubusercontent.com/uroplatus666/Paleo/master/gran.csv')

st.header('***:blue[Состав отложений и условия окружающей среды в период осадконакопления]***',anchor='center')
st.subheader('***:gray[Стоянка Хотылево_2]  2019***', divider='blue')
st.write(':grey[Все легенды и графики интерактивные]')
with st.container():
    fig = px.line(C_N, x='Содержание', y='Глубина, м', line_shape='spline',
                  color='Вещество', labels=dict(Вещество='<b>Вещество</b>'),
                  color_discrete_map={'С орг': '#4682B4',
                                      'Гумус': '#00BFFF',
                                      'СО2, %': '#7B68EE',
                                      'Карб, %': '#00008B'},width=800,height=600)
    fig.update_layout(
        yaxis={'autorange': 'reversed'},
        font_family="Courier New",
        font_color="black",
        title_font=dict(size=20),
        title={'text': "<b>Распределение веществ по глубине</b>",
               'y': 0.95,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        xaxis_title_font=dict(size=18),
        xaxis_title=dict(text='<b>Содержание вещества</b>'),
        yaxis_title_font=dict(size=18),
        yaxis_title=dict(text='<b>Глубина, м</b>'))
    st.plotly_chart(fig, theme="streamlit")
    st.write('---')
    fig = px.histogram(C_N, x='Содержание', y='№ слоя', histfunc='avg', orientation='h',
                       color='Вещество', labels=dict(Вещество='<b>Вещество</b>'),
                       color_discrete_map={'С орг': '#4682B4',
                                           'Гумус': '#00BFFF',
                                           'СО2, %': '#7B68EE',
                                           'Карб, %': '#00008B'},width=800,height=600)
    fig.update_layout(
        yaxis={'autorange': 'reversed'},
        font_family="Courier New",
        font_color="black",
        title_font=dict(size=20),
        title={'text': "<b>Распределение веществ по слоям</b>",
               'y': 0.95,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        xaxis_title_font=dict(size=18),
        xaxis_title=dict(text='<b>Содержание вещества</b>'),
        yaxis_title_font=dict(size=18),
        yaxis_title=dict(text='<b>Номер слоя</b>'))
    st.plotly_chart(fig, theme="streamlit")
st.write('---')
with st.container():
    fig = px.scatter(gran, x='Содержание в %',
                     y='Глубина, м', color='Диаметр частиц, мм',
                     symbol='Диаметр частиц, мм', size='Гигр.влага',
                     color_discrete_map={'<0.001': '#556B2F',
                                         '0.005-0.001': '#6B8E23',
                                         '0.01-0.005': '#9ACD32',
                                         '0.05-0.01': '#006400',
                                         '0.25-0.05': '#3CB371',
                                         '1-0.25': '#00FA9A'},width=800,height=600)
    fig.update_layout(
        yaxis={'autorange': 'reversed'},
        font_family="Courier New",
        font_color="black",
        title_font=dict(size=20),
        title={'text': "<b>Гранулометрический состав</b>",
               'y': 0.95,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        xaxis_title_font=dict(size=18),
        xaxis_title=dict(text='<b>Содержание вещества в %</b>'),
        yaxis_title_font=dict(size=18),
        yaxis_title=dict(text='<b>Глубина, м</b>'),
        legend=dict(title='<b>Диаметр частиц, мм</b>'))
    st.plotly_chart(fig, theme="streamlit")
    st.write('---')
    fig = px.line(gran, x='Содержание в %', line_shape='vhv',
                     y='№ слоя', color='Диаметр частиц, мм',
                     color_discrete_map={'<0.001': '#556B2F',
                                         '0.005-0.001': '#6B8E23',
                                         '0.01-0.005': '#9ACD32',
                                         '0.05-0.01': '#006400',
                                         '0.25-0.05': '#3CB371',
                                         '1-0.25': '#00FA9A'}, width=800, height=600)
    fig.update_layout(
        yaxis={'autorange': 'reversed'},
        font_family="Courier New",
        font_color="black",
        title_font=dict(size=20),
        title={'text': "<b>Гранулометрический состав</b>",
               'y': 0.95,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        xaxis_title_font=dict(size=18),
        xaxis_title=dict(text='<b>Содержание вещества в %</b>'),
        yaxis_title_font=dict(size=18),
        yaxis_title=dict(text='<b>Номер слоя</b>'),
        legend=dict(title='<b>Диаметр частиц, мм</b>'))
    st.plotly_chart(fig, theme="streamlit")
    st.write('---')
    fig = px.histogram(gran, x='Содержание в %', orientation='h',
                       histfunc='avg',
                       y='№ слоя', color='Диаметр частиц, мм',
                       hover_name='№ слоя',
                       color_discrete_map={'<0.001': '#556B2F',
                                           '0.005-0.001': '#6B8E23',
                                           '0.01-0.005': '#9ACD32',
                                           '0.05-0.01': '#006400',
                                           '0.25-0.05': '#3CB371',
                                           '1-0.25': '#00FA9A'},width=800,height=600)
    fig.update_layout(
        yaxis={'autorange': 'reversed'},
        font_family="Courier New",
        font_color="black",
        title_font=dict(size=20),
        title={'text': "<b>Гранулометрический состав по слоям</b>",
               'y': 0.95,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        xaxis_title_font=dict(size=18),
        xaxis_title=dict(text='<b>Содержание вещества в %</b>'),
        yaxis_title_font=dict(size=18),
        yaxis_title=dict(text='<b>Номер слоя</b>'),
        legend=dict(title='<b>Диаметр частиц, мм</b>'))
    st.plotly_chart(fig, theme="streamlit")








