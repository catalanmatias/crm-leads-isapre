import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Simulador Multi-Isapre | Asesoría Independiente",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS inspirados en tonos azul, cian y naranja (estilo Nueva Masvida)
# con sellos de independencia técnica.
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Header Principal */
    .main-header {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 50%, #1E3A8A 100%);
        padding: 2.2rem 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.3);
    }
    
    /* Insignia de Independencia */
    .neutral-badge {
        background-color: #FFEDD5;
        border: 1px solid #FDBA74;
        color: #C2410C;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.88rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 0.8rem;
    }

    /* Tarjeta de métricas */
    .metric-card {
        background-color: #FFFFFF;
        border: 2px solid #38BDF8;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #0284C7;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #475569;
        font-weight: 600;
    }

    /* Botón Naranja Destacado (Call To Action) */
    .stButton>button {
        background: linear-gradient(135deg, #EA580C 0%, #C2410C 100%) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 800 !important;
        padding: 0.85rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 6px 15px -3px rgba(234, 88, 12, 0.4);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px -3px rgba(234, 88, 12, 0.5);
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
            "7% Legal ($)": 126000,
            "Región": "Región Metropolitana",
            "Comuna": "Providencia",
            "Estado": "📄 En cotización"
        }
    ])

ESTADOS = ["📞 Por contactar", "📄 En cotización", "🩺 Evaluando médica", "✅ Afiliado / Cerrado", "❌ Descartado"]

# Navegación Privada
st.sidebar.title("📍 Navegación Privada")
modo = st.sidebar.radio("Selecciona vista:", ["💡 Simulador e Interactivo (Publicidad)", "🔒 CRM Interno Ventas"], index=0)

# -----------------------------------------------------------------------------
# VISTA 1: SIMULADOR INTERACTIVO PÚBLICO
# -----------------------------------------------------------------------------
if modo == "💡 Simulador e Interactivo (Publicidad)":
    
    # Encabezado Comercial con Aclaración de Independencia
    st.markdown("""
        <div class="main-header">
            <div class="neutral-badge">🛡️ Consultoría Privada e Independiente</div>
            <h1 style="font-size: 2.4rem; font-weight: 800; margin-bottom: 0.4rem;">Simulador de Planes de Salud e Isapre</h1>
            <p style="font-size: 1.15rem; opacity: 0.95; max-width: 800px; margin: 0 auto;">
                Calcula tu 7% legal en tiempo real y compara de forma neutral las mejores alternativas entre todas las Isapres del mercado chileno.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN INTERACTIVA 1: CÁLCULO EN TIEMPO REAL
    st.subheader("⚡ Paso 1: Calcula tu 7% legal aportable")
    st.caption("Desliza el monto de tu sueldo bruto imponible para calcular tu capacidad de cotización.")
    
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
        cargas_sim = st.number_input("👨‍👩‍👧 ¿Cuántas cargas familiares vas a incluir?", min_value=0, max_value=8, value=0)

    # Cálculos en Vivo
    siete_pesos = int(renta_sim * 0.07)
    uf_estimada = 38000  # Valor aproximado UF
    siete_uf = round(siete_pesos / uf_estimada, 2)

    with col_s2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Tu 7% Legal Obligatorio</div>
                <div class="metric-value">${siete_pesos:,} CLP</div>
                <div style="font-size: 1rem; color: #0284C7; font-weight: 700;">Equivalente a ~ {siete_uf} UF / mes</div>
            </div>
        """, unsafe_allow_html=True)

    # Diagnóstico amigable dinámico
    st.markdown("<br>", unsafe_allow_html=True)
    if renta_sim >= 1200000:
        st.success(f"✅ **Perfil Óptimo:** Con tu aportación legal de **${siete_pesos:,} CLP**, accedes a planes completos en Isapres abiertas con cobertura en clínicas privadas.")
    elif renta_sim >= 800000:
        st.info(f"💡 **Perfil Apto:** Tu 7% (**${siete_pesos:,} CLP**) permite evaluar convenios de Isapre o combinaciones estratégicas de salud.")
    else:
        st.warning("ℹ️ **Sugerencia:** Analizaremos las opciones preferentes de Isapre o esquemas Fonasa + Seguro que mejor aprovechen tu presupuesto.")

    st.divider()

    # SECCIÓN 2: FORMULARIO DE CONTACTO
    st.subheader("📩 Paso 2: Recibe la comparativa completa de Isapres")
    st.caption("Ingresa tus datos para procesar tu simulación y enviarte una tabla comparativa a tu WhatsApp.")

    with st.form("form_interactivo_cliente", clear_on_submit=True):
        c1, c2 = st.columns(2)
        
        with c1:
            nombre = st.text_input("👤 Nombre y Apellido *", placeholder="Ej: Constanza Morales")
            rut = st.text_input("🆔 RUT *", placeholder="Ej: 18.765.432-1")
            telefono = st.text_input("📱 WhatsApp para enviar la comparativa *", placeholder="+56 9 1234 5678")
            fecha_nac = st.date_input("🎂 Fecha de Nacimiento", value=date(1992, 1, 1), min_value=date(1940, 1, 1))

        with c2:
            prevision = st.selectbox("🏥 Previsión Actual *", LISTA_PREVISION)
            situacion = st.selectbox("💼 Situación Laboral *", SITUACION_LABORAL)
            afp = st.selectbox("🏦 AFP Actual", LISTA_AFPS)
            region = st.selectbox("🗺️ Región de Residencia", LISTA_REGIONES, index=6)
            comuna = st.text_input("🏙️ Comuna", placeholder="Ej: Las Condes, Concepción")

        notas = st.text_area("💬 Preferencias de clínicas o cobertura (Opcional)", placeholder="Ej: Busco Clínica Indisa / Alemana, cobertura dental, plan con parto, etc.")
        
        # Nota legal al pie del formulario
        st.caption("🔒 *Servicio de asesoría libre e independiente. Respetamos la privacidad de tus datos bajo la legislación vigente.*")
        
        st.markdown("<br>", unsafe_allow_html=True)
        enviar = st.form_submit_button("🚀 SOLICITAR COMPARATIVA MULTI-ISAPRE POR WHATSAPP")

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
                    "Cargas": cargas_sim,
                    "Estado": "📞 Por contactar",
                    "Notas": notas
                }])
                
                st.session_state.prospectos = pd.concat([st.session_state.prospectos, nuevo_registro], ignore_index=True)
                st.balloons()
                st.success("🎉 ¡Simulación procesada con éxito! Un asesor independiente revisará las opciones y te escribirá por WhatsApp en breve.")
            else:
                st.error("Por favor completa los campos requeridos (*): Nombre, RUT y WhatsApp.")

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
