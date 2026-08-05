import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cotizador Gratuito de Isapres - Asesoría de Salud",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para una interfaz más limpia y profesional
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-size: 2.2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #4B5563;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .trust-badge {
        background-color: #EFF6FF;
        border-left: 4px solid #2563EB;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 0.6rem 2rem;
        border-radius: 8px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Inicializar base de datos en sesión
if "prospectos" not in st.session_state:
    st.session_state.prospectos = pd.DataFrame([
        {
            "ID": 1,
            "Nombre": "Juan Pérez",
            "RUT": "15.432.890-1",
            "Teléfono": "+56912345678",
            "Isapre Actual": "Banmédica",
            "Renta Imponible ($)": 1800000,
            "7% Estimado ($)": 126000,
            "Estado": "📄 En cotización",
            "Notas": "Cliente requiere plan preferente Santa María."
        }
    ])

ESTADOS = [
    "📞 Por contactar",
    "📄 En cotización",
    "🩺 Evaluando médica",
    "✅ Afiliado / Cerrado",
    "❌ Descartado"
]

# 2. Selector en la barra lateral (Oculto por defecto para el cliente)
st.sidebar.title("📍 Navegación Privada")
modo = st.sidebar.radio(
    "Selecciona la vista:",
    ["📝 Formulario para Clientes (Publicidad)", "🔒 Panel de Administración (CRM)"],
    index=0
)

# -----------------------------------------------------------------------------
# MODO 1: LANDING PAGE Y FORMULARIO AMIGABLE (PÚBLICO)
# -----------------------------------------------------------------------------
if modo == "📝 Formulario para Clientes (Publicidad)":
    
    # Encabezado Comercial
    st.markdown('<div class="main-title">🩺 Encuentra tu Plan de Isapre Ideal</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Compara gratis entre las principales Isapres de Chile y optimiza tu 7% legal de salud.</div>', unsafe_allow_html=True)

    # Bloque de Confianza / Ventajas
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        st.info("🎯 **Sin Costo Adicional**\n\nEl servicio de asesoría y comparativa es 100% gratuito.")
    with col_t2:
        st.success("⚡ **Respuesta Rápida**\n\nRecibe las mejores alternativas directo a tu WhatsApp.")
    with col_t3:
        st.warning("🔒 **Datos Protegidos**\n\nInformación confidencial según la Ley de Protección de Datos.")

    st.divider()

    # Formulario Principal organizado en contenedor
    with st.container():
        st.markdown("### 📋 Ingresa tus datos para generar tu comparativa")
        
        with st.form("form_captacion_publico", clear_on_submit=True):
            
            col1, col2 = st.columns(2)
            
            with col1:
                nombre = st.text_input("👤 Nombre y Apellido *", placeholder="Ej: Constanza Morales")
                rut = st.text_input("🆔 RUT *", placeholder="Ej: 18.765.432-1")
                telefono = st.text_input("📱 WhatsApp / Teléfono de contacto *", placeholder="+56 9 1234 5678")
            
            with col2:
                isapre_actual = st.selectbox(
                    "🏥 ¿Cuál es tu previsión de salud actual?",
                    ["Fonasa", "Banmédica", "Colmena", "Consorcio", "Cruz Blanca", "Nueva Masvida", "Sin previsión"]
                )
                renta = st.number_input(
                    "💰 Renta Imponible Estimada ($)",
                    min_value=0,
                    step=100000,
                    help="Tu renta nos permite calcular exactamente tu 7% legal obligatorio."
                )
                cargas = st.number_input("👨‍👩‍👧 Número de cargas (Hijos / Cónyuge)", min_value=0, max_value=10, step=1)

            # Cálculo en tiempo real visible si ingresa su renta
            if renta > 0:
                siete_porciento = int(renta * 0.07)
                st.markdown(f"💡 **Dato clave:** Tu 7% legal obligatorio es de aproximadamente **${siete_porciento:,} CLP** al mes para financiar tu plan.".replace(",", "."))

            notas = st.text_area(
                "💬 ¿Tienes alguna preferencia específica? (Opcional)",
                placeholder="Ej: Prefiero Clínica Alemana / Indisa, busco cobertura de maternidad, dental, etc."
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            enviar = st.form_submit_button("🚀 RECIBIR COTIZACIÓN GRATIS POR WHATSAPP")

            if enviar:
                if nombre and rut and telefono:
                    df = st.session_state.prospectos
                    nuevo_id = int(df["ID"].max() + 1) if not df.empty else 1
                    siete_calc = int(renta * 0.07) if renta > 0 else 0
                    
                    nuevo_lead = pd.DataFrame([{
                        "ID": nuevo_id,
                        "Nombre": nombre,
                        "RUT": rut,
                        "Teléfono": telefono,
                        "Isapre Actual": isapre_actual,
                        "Renta Imponible ($)": renta,
                        "7% Estimado ($)": siete_calc,
                        "Estado": "📞 Por contactar",
                        "Notas": f"Cargas: {cargas}. Preferencias: {notas}"
                    }])
                    
                    st.session_state.prospectos = pd.concat([st.session_state.prospectos, nuevo_lead], ignore_index=True)
                    
                    st.balloons()
                    st.success("🎉 ¡Solicitud enviada con éxito! Un asesor se pondrá en contacto contigo en breve a tu WhatsApp.")
                else:
                    st.error("Por favor completa los campos requeridos (*): Nombre, RUT y WhatsApp.")

# -----------------------------------------------------------------------------
# MODO 2: PANEL DE ADMINISTRACIÓN INTERNO (CRM PRIVADO)
# -----------------------------------------------------------------------------
else:
    st.title("💼 CRM Interno de Prospección - Isapre")
    st.markdown("Gestión de prospectos recibidos desde tus anuncios publicitarios.")
    
    df = st.session_state.prospectos

    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Prospectos", len(df))
    k2.metric("Por Contactar", len(df[df["Estado"] == "📞 Por contactar"]))
    k3.metric("En Cotización", len(df[df["Estado"] == "📄 En cotización"]))
    k4.metric("Afiliados / Cerrados", len(df[df["Estado"] == "✅ Afiliado / Cerrado"]))

    st.divider()

    st.subheader("📋 Base de Datos de Prospectos")
    filtro_est = st.multiselect("Filtrar por etapa:", ESTADOS, default=ESTADOS)
    df_filtrado = df[df["Estado"].isin(filtro_est)]
    
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

    # Actualizador en la barra lateral
    st.sidebar.divider()
    st.sidebar.subheader("🔄 Cambiar Estado de Lead")
    if not df.empty:
        id_sel = st.sidebar.selectbox("Seleccionar ID:", df["ID"].tolist(), format_func=lambda x: f"ID {x} - {df[df['ID']==x]['Nombre'].values[0]}")
        estado_nuevo = st.sidebar.selectbox("Nuevo Estado:", ESTADOS)
        
        if st.sidebar.button("Actualizar Estado"):
            st.session_state.prospectos.loc[st.session_state.prospectos["ID"] == id_sel, "Estado"] = estado_nuevo
            st.sidebar.success("¡Estado actualizado!")
            st.rerun()
