import pandas as pd
import plotly.express as px
import streamlit as st

# Cargamos los datos limpios
car_data = pd.read_csv('./vehicles_us_clean.csv')

# Creamos el encabezado
st.header("Análisis de vehículos")

# Mostramos los datos del dataframe
st.write(car_data)

# Creamos los botones y los checkbox
hist_button = st.button('Construir histograma de precios por año de modelo')
scatter_button = st.button('Construir gráfico de dispersión entre año de modelo y precio')
boxplot_checkbox = st.checkbox('Construir gráfico de cajas de precio por condición de vehículo')
fuel_checkbox = st.checkbox('Mostrar gráfico de precio promedio por tipo de combustible')


# Si el botón de histograma es presionado
if hist_button:
    st.write('Histograma')
    price_avg_by_year = car_data.groupby('model_year')['price'].mean().reset_index()
    fig = px.bar(
        price_avg_by_year, 
        x="model_year", 
        y="price", 
        title="Promedio de Precios por Año de Modelo",
        labels={"model_year": "Año del modelo", "price": "Precio en USD"}
    )
    st.plotly_chart(fig, use_container_width=True)

# Si el botón de gráfico de dispersión es presionado
if scatter_button:
    st.write('Gráfico de dispersión')
    fig2 = px.scatter(
        car_data, 
        x='model_year', 
        y='price', 
        color='condition', 
        title="Precio vs Año de modelo por condición",
        labels={"model_year": "Año del modelo", "price": "Precio en USD", "condition": "Condición del vehículo"}
    )
    st.plotly_chart(fig2, use_container_width=True)

# Si el checkbox de gráfico de cajas es presionado
if boxplot_checkbox:
    st.write('Boxplot')
    fig3 = px.box(
        car_data, 
        x="condition", 
        y="price", 
        title="Precios por condición de vehículo",
        labels={"condition": "Condición del Vehículo", "price": "Precio en USD"}
    )
    st.plotly_chart(fig3, use_container_width=True)

# Si el checkbox de gráfico de precios promedio por tipo de combustible es presionado
if fuel_checkbox:
    st.write('Gráfico de barras')
    fuel_avg_price = car_data.groupby('fuel')['price'].mean().reset_index()
    fig4 = px.bar(fuel_avg_price, x='fuel', y='price', title="Precio promedio por tipo de combustible", 
                 labels={"fuel": "Tipo de combustible", "price": "Precio promedio en USD"}
                 )
    st.plotly_chart(fig4, use_container_width=True)