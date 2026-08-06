import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Simulador Multi-Isapre | Asesoría Independiente",
    page_icon="❇️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS con la paleta alegre y colorida (Verde, Naranja, Azul, Púrpura)
st.markdown("""
    <style>
    /* Fondo general suave y fresco */
    .stApp {
        background-color: #F0FDF4;
    }
    
    /* Header Principal Verde */
    .main-header {
        background: linear-gradient(135deg, #009B3A 0%, #007A2E 100%);
        padding: 2.2rem 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 20px rgba(0, 155, 58, 0.2);
    }
    
    /* Insignia de Independencia en Naranja */
    .neutral-badge {
        background-color: #F58220;
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 0.8rem;
        box-shadow: 0 4px 6px rgba(245, 130, 32, 0.3);
    }

    /* Tarjetas del Simulador en Azul */
    .metric-card {
        background-color: #FFFFFF;
        border: 3px solid #0072CE;
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 114, 206, 0.15);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        color: #0072CE;
    }
    .metric-label {
        font-size: 0.95rem;
        color: #334155;
        font-weight: 700;
    }

    /* Tarjeta de Aviso Púrpura */
    .purp-badge {
        background-color: #F3E8FF;
        border-left: 5px solid #6C2D91;
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        color: #581C87;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* Botón de Acción Naranja */
    .stButton>button {
        background: linear-gradient(135deg, #F58220 0%, #E06B00 100%) !important;
        color: white !important;
        font-size: 1.25rem !important;
        font-weight: 800 !important;
        padding: 0.9rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 6px 15px rgba(245, 130, 32, 0.4);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(245, 130, 32, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Listas Técnicas
LISTA_PREVISION = [
    "Fonasa", "Banmédica", "Colmena", "Consalud", "Cruz Blanca", 
    "Nueva Masvida", "Vida Tres", "Esencial", "ISalud / Empresa", 
    "Dipreca / Capredena", "Sin previsión"
]
LISTA_AFPS = ["Habitat", "Capital", "Cuprum", "Modelo", "PlanVital", "Provida", "Uno", "No cotiza"]
SITUACION_LABORAL = ["Dependiente", "Independiente", "Pensionado", "Voluntario", "Cesante"]
MEDIOS_CONTACTO = ["📱 Mensaje de WhatsApp", "📞 Llamada Telefónica", "📧 Correo Electrónico"]

LISTA_REGIONES = [
    "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo",
    "Valparaíso", "Región Metropolitana", "O'Higgins", "Maule", "Ñuble",
    "Bío Bío", "La Araucanía", "Los Ríos", "Los Lagos", "Aysén", "Magallanes"
]

# Base de Datos
if "prospectos" not in st.session_state:
    st.session_state.prospectos = pd.DataFrame([
        {
            "ID": 1,
            "Nombre": "Juan Pérez",
            "RUT": "15.432.890-1",
            "Teléfono": "+56912345678",
            "Previsión Actual": "Banmédica",
            "Situación Laboral": "Dependiente",
            "AFP": "Habitat",
            "Renta Imponible ($)": 1800000,
            "7% Legal ($)": 126000,
            "Región": "Región Metropolitana",
            "Comuna": "Providencia",
            "Medio Contacto": "📱 Mensaje de WhatsApp",
            "Estado": "📄 En cotización"
        }
    ])

ESTADOS = ["📞 Por contactar", "📄 En cotización", "🩺 Evaluando médica", "✅ Afiliado / Cerrado", "❌ Descartado"]

# Navegación Privada
st.sidebar.title("⚙️ Navegación Privada")
modo = st.sidebar.radio("Selecciona vista:", ["💡 Simulador e Interactivo (Publicidad)", "🔒 CRM Interno Ventas"], index=0)

# -----------------------------------------------------------------------------
# VISTA 1: SIMULADOR PÚBLICO CLIENTES
# -----------------------------------------------------------------------------
if modo == "💡 Simulador e Interactivo (Publicidad)":
    
    st.markdown("""
        <div class="main-header">
            <div class="neutral-badge">❇️ Consultoría Privada e Independiente</div>
            <h1 style="font-size: 2.3rem; font-weight: 800; margin-bottom: 0.4rem;">Simulador de Planes de Salud e Isapre</h1>
            <p style="font-size: 1.1rem; opacity: 0.95; max-width: 800px; margin: 0 auto;">
                Calcula tu 7% legal en tiempo real y compara objetivamente entre todas las Isapres de Chile.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN INTERACTIVA 1
    st.subheader("⚡ Paso 1: Calcula tu 7% legal obligatorio")
    st.caption("Desliza el monto de tu sueldo imponible mensual para calcular tu capacidad de cotización.")
    
    col_s1, col_s2 = st.columns([2, 1])
    
    with col_s1:
        renta_sim = st.slider(
            "Selecciona tu Renta Imponible mensual ($ CLP):",
            min_value=500000,
            max_value=5000000,
            value=1500000,
            step=50000,
            format="$%d"
        )
        cargas_sim = st.number_input("👨‍👩‍👧 Número de cargas familiares (Hijos / Cónyuge)", min_value=0, max_value=8, value=0)

    # Cálculos en Vivo
    siete_pesos = int(renta_sim * 0.07)
    uf_estimada = 38000
    siete_uf = round(siete_pesos / uf_estimada, 2)

    with col_s2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Tu 7% Legal Aportable</div>
                <div class="metric-value">${siete_pesos:,} CLP</div>
                <div style="font-size: 1rem; color: #009B3A; font-weight: 700;">Equivalente a ~ {siete_uf} UF / mes</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if renta_sim >= 1200000:
        st.success(f"✅ **Perfil Óptimo para Isapre:** Con tu aportación legal de **${siete_pesos:,} CLP**, accedes a planes completos en Isapres abiertas con cobertura en clínicas privadas.")
    elif renta_sim >= 800000:
        st.info(f"💡 **Perfil Apto:** Tu 7% (**${siete_pesos:,} CLP**) permite evaluar convenios de Isapre o combinaciones estratégicas de salud.")
    else:
        st.warning("ℹ️ **Sugerencia:** Analizaremos las opciones preferentes de Isapre o esquemas Fonasa + Seguro que mejor aprovechen tu presupuesto.")

    st.divider()

    # SECCIÓN 2: FORMULARIO
    st.subheader("📩 Paso 2: Recibe la comparativa completa de Isapres")
    st.caption("Ingresa tus datos para procesar tu simulación y enviarte una tabla comparativa personalizada.")

    with st.form("form_interactivo_cliente", clear_on_submit=True):
        c1, c2 = st.columns(2)
        
        with c1:
            nombre = st.text_input("👤 Nombre y Apellido *", placeholder="Ej: Constanza Morales")
            rut = st.text_input("🆔 RUT *", placeholder="Ej: 18.765.432-1")
            telefono = st.text_input("📱 Teléfono / WhatsApp de contacto *", placeholder="+56 9 1234 5678")
            fecha_nac = st.date_input("🎂 Fecha de Nacimiento", value=date(1992, 1, 1), min_value=date(1940, 1, 1))

        with c2:
            prevision = st.selectbox("🏥 Previsión de Salud Actual *", LISTA_PREVISION)
            situacion = st.selectbox("💼 Situación Laboral *", SITUACION_LABORAL)
            afp = st.selectbox("🏦 AFP Actual", LISTA_AFPS)
            region = st.selectbox("🗺️ Región de Residencia", LISTA_REGIONES, index=6)

        c3, c4 = st.columns(2)
        with c3:
            comuna = st.text_input("🏙️ Comuna de Residencia", placeholder="Ej: Las Condes, Concepción, Viña del Mar")
        with c4:
            medio_contacto = st.selectbox("📞 ¿Cómo prefieres que te contactemos?", MEDIOS_CONTACTO)

        notas = st.text_area("💬 Preferencias de clínicas o cobertura (Opcional)", placeholder="Ej: Busco Clínica Indisa / Alemana, cobertura dental, plan con parto, etc.")
        
        st.markdown("""
            <div class="purp-badge">
                🔒 <b>Compromiso de Privacidad:</b> Somos una plataforma de asesoría independiente. Tus datos son estrictamente confidenciales bajo la ley chilena y no serán compartidos con terceros.
            </div>
        """, unsafe_allow_html=True)
        
        enviar = st.form_submit_button("🚀 SOLICITAR COMPARATIVA DE ISAPRES")

        if enviar:
            if nombre and rut and telefono:
                df = st.session_state.prospectos
                nuevo_id = int(df["ID"].max() + 1) if not df.empty else 1
                
                nuevo_registro = pd.DataFrame([{
                    "ID": nuevo_id,
                    "Nombre": nombre,
                    "RUT": rut,
                    "Teléfono": telefono,
                    "Fecha Nacimiento": str(fecha_nac),
                    "Previsión Actual": prevision,
                    "Situación Laboral": situacion,
                    "AFP": afp,
                    "Renta Imponible ($)": renta_sim,
                    "7% Legal ($)": siete_pesos,
                    "Región": region,
                    "Comuna": comuna,
                    "Medio Contacto": medio_contacto,
                    "Cargas": cargas_sim,
                    "Estado": "📞 Por contactar",
                    "Notas": notas
                }])
                
                st.session_state.prospectos = pd.concat([st.session_state.prospectos, nuevo_registro], ignore_index=True)
                st.balloons()
                st.success(f"🎉 ¡Simulación procesada con éxito! Te contactaremos mediante {medio_contacto} a la brevedad.")
            else:
                st.error("Por favor completa los campos requeridos (*): Nombre, RUT y Teléfono/WhatsApp.")

# -----------------------------------------------------------------------------
# VISTA 2: CRM PRIVADO INTERNO
# -----------------------------------------------------------------------------
else:
    st.title("💼 CRM Privado de Prospección Isapre")
    df = st.session_state.prospectos

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Prospectos", len(df))
    k2.metric("Por Contactar", len(df[df["Estado"] == "📞 Por contactar"]))
    k3.metric("En Cotización", len(df[df["Estado"] == "📄 En cotización"]))
    k4.metric("Cerrados", len(df[df["Estado"] == "✅ Afiliado / Cerrado"]))

    st.divider()

    st.subheader("📋 Base de Datos de Clientes")
    filtro_est = st.multiselect("Filtrar por estado:", ESTADOS, default=ESTADOS)
    df_filtrado = df[df["Estado"].isin(filtro_est)]
    
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

    st.sidebar.divider()
    st.sidebar.subheader("🔄 Cambiar Estado")
    if not df.empty:
        id_sel = st.sidebar.selectbox("Seleccionar Lead:", df["ID"].tolist(), format_func=lambda x: f"ID {x} - {df[df['ID']==x]['Nombre'].values[0]}")
        est_nuevo = st.sidebar.selectbox("Nuevo Estado:", ESTADOS)
        if st.sidebar.button("Actualizar Estado"):
            st.session_state.prospectos.loc[st.session_state.prospectos["ID"] == id_sel, "Estado"] = est_nuevo
            st.sidebar.success("¡Estado actualizado!")
            st.rerun()
