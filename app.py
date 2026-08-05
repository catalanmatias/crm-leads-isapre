
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CRM Prospección Isapre", layout="wide")

st.title("🏥 CRM de Prospección - Asesoría de Salud e Isapre")
st.write("Gestión de leads y cotizaciones para cambio o incorporación a Isapre.")

# Formulario para ingresar nuevo prospecto
with st.sidebar:
    st.header("➕ Agregar Nuevo Prospecto")
    nombre = st.text_input("Nombre completo")
    origen = st.selectbox("Red Social de Origen", ["LinkedIn", "Instagram", "Facebook", "GitHub", "Referido"])
    renta = st.number_input("Renta Imponible (CLP)", min_value=0, step=50000, value=1200000)
    sistema_actual = st.selectbox("Sistema Actual", ["Fonasa A/B", "Fonasa C/D", "Banmédica", "Consalud", "CruzBlanca", "Colmena", "Vida Tres", "Esencial", "Nueva Masvida"])
    cargas = st.number_input("Número de Cargas Familiares", min_value=0, max_value=10, value=0)
    estado = st.selectbox("Estado del Embudo", ["1. Lead Captado", "2. Contactado", "3. Propuesta Enviada", "4. En Tramitación (FUN)", "5. Cerrado / Afiliado"])
    
    # Cálculo estimado del 7% cotizable
    cotizacion_7 = renta * 0.07
    st.info(f"💡 Cotización estimada del 7%: **${cotizacion_7:,.0f} CLP**")
    
    btn_guardar = st.button("Guardar Prospecto")

st.subheader("📋 Lista de Prospectos en Seguimiento")
st.caption("Filtra y gestiona tus cotizaciones activas.")
