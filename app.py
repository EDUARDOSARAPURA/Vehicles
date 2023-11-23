import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Graficos de datos de los Vehiculos')
hist_button = st.checkbox('Construir histograma')  # crear un botón
long_df = px.data.medals_long('vehicles_us.csv')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

dist_button = st.checkbox('Construir grafico de dispercion')  # crear un botón

if dist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    # crear un grafico de dispercion
    fig2 = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

bar_button = st.button('Construir grafico de barras')

if bar_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de barras para el conjunto de datos de anuncios de venta de coches')
    # crear un grafico de dispercion
    fig3 = px.bar(long_df, x="model_year", y="count", color="condition",
                  title="Cantidad de vehiculos por año y condicion")
    # mostrar un gráfico Plotly interactivo
    fig3.show()
