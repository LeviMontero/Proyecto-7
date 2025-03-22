import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('./vehicles_us_clean.csv')

# Crear un encabezado
st.header("Análisis de vehículos: Año, Precio y Condición")

# Crear botones para generar gráficos
hist_button = st.button('Construir histograma de precios por año de modelo')
scatter_button = st.button('Construir gráfico de dispersión entre año de modelo y precio')
boxplot_button = st.button('Construir gráfico de cajas por condición de vehículo')

# Si el botón de histograma es presionado
if hist_button:
    # Crear un histograma de los precios por año de modelo
    fig = px.histogram(car_data, x="model_year", y="price", histfunc="avg", title="Promedio de Precios por Año de Modelo")
    st.plotly_chart(fig, use_container_width=True)

# Si el botón de gráfico de dispersión es presionado
if scatter_button:
    # Crear un gráfico de dispersión entre año de modelo y precio, coloreado por condición
    fig2 = px.scatter(car_data, x='model_year', y='price', color='condition', title="Precio vs Año de Modelo por Condición")
    st.plotly_chart(fig2, use_container_width=True)

# Si el botón de gráfico de cajas es presionado
if boxplot_button:
    # Crear un gráfico de cajas que muestra la distribución de precios por condición
    fig3 = px.box(car_data, x="condition", y="price", title="Distribución de Precios por Condición de Vehículo")
    st.plotly_chart(fig3, use_container_width=True)