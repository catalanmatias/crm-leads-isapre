import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Cotizador Gratuito Isapre - Asesoría de Salud",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS con paleta de colores del sector Salud (Turquesa / Verde Menta)
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    .main-title {
        color: #0F766E;
        font-size: 2.3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #334155;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 1.8rem;
    }
    .health-card {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .stButton>button {
        background-color: #0D9488 !important;
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 4px 6px -1px rgba(13, 148, 136, 0.3);
    }
    .stButton>button:hover {
        background-color: #0F766E !important;
    }
    </style>
""", unsafe_allow_html=True)

# Listas de Opciones Técnicas de Previsión y AFP
LISTA_PREVISION = [
    "Fonasa",
    "--- ISAPRES ABIERTAS ---",
    "Banmédica",
    "Colmena",
    "Consalud",
    "Cruz Blanca",
    "Nueva Masvida",
    "Vida Tres",
    "Esencial",
    "--- ISAPRES CERRADAS DE EMPRESA ---",
    "ISalud",
    "Cruz del Norte",
    "Fundación",
    "Isapre San Lorenzo",
    "Isapre Fusat",
    "Isapre Chuquicamata",
    "--- OTROS ---",
    "Dipreca / Capredena",
    "Sin previsión actualmente"
]

LISTA_AFPS = ["Habitat", "Capital", "Cuprum", "Modelo", "PlanVital", "Provida", "Uno", "No cotiza en AFP"]
SITUACION_LABORAL = ["Dependiente", "Independiente", "Pensionado", "Voluntario", "Cesante"]

LISTA_REGIONES = [
    "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo",
    "Valparaíso", "Región Metropolitana", "O'Higgins", "Maule", "Ñuble",
    "Bío Bío", "La Araucanía", "Los Ríos", "Los Lagos", "Aysén", "Magallanes"
]

# Inicialización de Base de Datos
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
            "Región": "Región Metropolitana",
            "Comuna": "Providencia",
            "Estado": "📄 En cotización"
        }
    ])

ESTADOS = ["📞 Por contactar", "📄 En cotización", "🩺 Evaluando médica", "✅ Afiliado / Cerrado", "❌ Descartado"]

# Navegación Privada
st.sidebar.title("📍 Navegación Privada")
modo = st.sidebar.radio("Selecciona vista:", ["📝 Formulario Clientes (Publicidad)", "🔒 CRM Interno Ventas"], index=0)

# -----------------------------------------------------------------------------
# VISTA 1: FORMULARIO PÚBLICO CLIENTES
# -----------------------------------------------------------------------------
if modo == "📝 Formulario Clientes (Publicidad)":
    
    st.markdown('<div class="main-title">🩺 Cotización Personalizada de Isapre</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Compara alternativas de salud y optimiza tu 7% legal con asesoría gratuita.</div>', unsafe_allow_html=True)

    # Bloques de beneficio
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        st.markdown('<div class="health-card">🏥 <b>Todas las Isapres</b><br><small>Revisión de planes abiertos del mercado.</small></div>', unsafe_allow_html=True)
    with col_b2:
        st.markdown('<div class="health-card">⚡ <b>Asesoría 100% Gratuita</b><br><small>Respuesta rápida vía WhatsApp.</small></div>', unsafe_allow_html=True)
    with col_b3:
        st.markdown('<div class="health-card">🛡️ <b>Confidencial</b><br><small>Protección estricta de datos de salud.</small></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.form("form_cliente_isapre", clear_on_submit=True):
        st.subheader("📋 Antecedentes del Titular")
        
        c1, c2 = st.columns(2)
        with c1:
            nombre = st.text_input("👤 Nombre Completo *", placeholder="Ej: Constanza Morales")
            rut = st.text_input("🆔 RUT *", placeholder="Ej: 18.765.432-1")
            fecha_nac = st.date_input("🎂 Fecha de Nacimiento", value=date(1992, 1, 1), min_value=date(1940, 1, 1))
            telefono = st.text_input("📱 Teléfono / WhatsApp *", placeholder="+56 9 1234 5678")

        with c2:
            prevision = st.selectbox("🏥 ¿Cuál es tu previsión de salud actual? *", LISTA_PREVISION)
            situacion = st.selectbox("💼 Situación Laboral *", SITUACION_LABORAL)
            afp = st.selectbox("🏦 AFP Actual", LISTA_AFPS)
            renta = st.number_input("💰 Renta Imponible Estimada ($)", min_value=0, step=100000)

        st.subheader("📍 Ubicación y Cargas")
        c3, c4 = st.columns(2)
        with c3:
            region = st.selectbox("🗺️ Región de Residencia", LISTA_REGIONES, index=6)
            comuna = st.text_input("🏙️ Comuna", placeholder="Ej: Las Condes, Concepción, Viña del Mar")
        
        with c4:
            cargas = st.number_input("👨‍👩‍👧 Número de Cargas (Hijos / Cónyuge)", min_value=0, max_value=10, step=1)

        # Calculador de 7% legal
        if renta > 0:
            siete_calc = int(renta * 0.07)
            st.info(f"💡 **Tu 7% legal estimado de cotización:** ${siete_calc:,} CLP / mes.".replace(",", "."))

        notas = st.text_area("💬 ¿Qué buscas en tu plan? (Opcional)", placeholder="Ej: Cobertura en Clínica Alemana / Indisa, maternidad, etc.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        enviar = st.form_submit_button("🚀 SOLICITAR COTIZACIÓN DE PLANES POR WHATSAPP")

        if enviar:
            if nombre and rut and telefono:
                if "---" in prevision:
                    st.error("Por favor selecciona una opción de previsión válida.")
                else:
                    df = st.session_state.prospectos
                    nuevo_id = int(df["ID"].max() + 1) if not df.empty else 1
                    siete_calc = int(renta * 0.07) if renta > 0 else 0
                    
                    nuevo_registro = pd.DataFrame([{
                        "ID": nuevo_id,
                        "Nombre": nombre,
                        "RUT": rut,
                        "Teléfono": telefono,
                        "Fecha Nacimiento": str(fecha_nac),
                        "Previsión Actual": prevision,
                        "Situación Laboral": situacion,
                        "AFP": afp,
                        "Renta Imponible ($)": renta,
                        "Región": region,
                        "Comuna": comuna,
                        "Cargas": cargas,
                        "7% Estimado ($)": siete_calc,
                        "Estado": "📞 Por contactar",
                        "Notas": notas
                    }])
                    
                    st.session_state.prospectos = pd.concat([st.session_state.prospectos, nuevo_registro], ignore_index=True)
                    st.balloons()
                    st.success("🎉 ¡Solicitud enviada con éxito! Un asesor se pondrá en contacto a la brevedad.")
            else:
                st.error("Por favor completa los campos requeridos (*): Nombre, RUT y WhatsApp.")

# -----------------------------------------------------------------------------
# VISTA 2: CRM PRIVADO
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

    st.subheader("📋 Base de Datos de Clientes Recibidos")
    filtro_est = st.multiselect("Filtrar por estado:", ESTADOS, default=ESTADOS)
    df_filtrado = df[df["Estado"].isin(filtro_est)]
    
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

    st.sidebar.divider()
    st.sidebar.subheader("🔄 Cambiar Estado")
    if not df.empty:
        id_sel = st.sidebar.selectbox("Seleccionar Lead:", df["ID"].tolist(), format_func=lambda x: f"ID {x} - {df[df['ID']==x]['Nombre'].values[0]}")
        est_nuevo = st.sidebar.selectbox("Nuevo Estado:", ESTADOS)
        if st.sidebar.button("Actualizar"):
            st.session_state.prospectos.loc[st.session_state.prospectos["ID"] == id_sel, "Estado"] = est_nuevo
            st.sidebar.success("¡Estado actualizado!")
            st.rerun()
