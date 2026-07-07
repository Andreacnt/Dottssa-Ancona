import streamlit as st

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Biologa Nutrizionista",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); }
.block-container { background: rgba(255,255,255,0.92); border-radius: 20px; padding: 2rem 3rem; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-top: 1rem; }
header { background: transparent !important; }
h1, h2, h3 { color: #14532d; }
.stTabs [data-baseweb="tab-list"] { gap: 8px; }
.stTabs [data-baseweb="tab"] { font-weight: 500; }
.stButton button { background: #16a34a; color: white; border-radius: 50px; padding: 8px 32px; font-weight: 600; border: none; }
.stButton button:hover { background: #15803d; }
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("### 🥗 Dott.ssa Graziana Ancona")
    st.markdown("*Biologa Nutrizionista a Parma*")

st.markdown("---")

home, chisono, servizi, percorso, approccio, blog, contatti = st.tabs(["🏠 Home", "👩‍⚕️ Chi Sono", "📋 Di cosa mi occupo", "📊 Percorso", "🌿 Approccio", "📖 Blog", "📬 Contatti"])

with home:
    st.title("Dott.ssa Graziana Ancona — Biologa Nutrizionista")
    st.markdown("""
    Accompagno persone di ogni età in percorsi nutrizionali personalizzati,
    costruiti sulle esigenze individuali e basati sulle più recenti evidenze scientifiche.
    Il mio obiettivo è aiutare ogni persona a sviluppare un rapporto più sereno, consapevole
    e sostenibile con l'alimentazione, migliorando il proprio stato di salute e il benessere generale.
    """)

    st.markdown("""
    📍 **Consulenze in presenza:** sabato su appuntamento presso Centro Rigenesis, Parma

    💻 **Consulenze online:** su appuntamento
    """)

with chisono:
    st.title("Chi Sono")
    st.markdown("""
    Sono la **Dott.ssa Graziana Ancona**, Biologa Nutrizionista a Parma,
    laureata in Scienze della Nutrizione Umana e altamente formata in nutrizione
    sportiva e benessere femminile.

    ✨ Credo che la nutrizione non debba essere vissuta come una rinuncia, ma come uno strumento
    per prendersi cura di sé, ritrovare equilibrio e valorizzare il proprio benessere nel lungo termine.
    """)

    with st.expander("🎓 Formazione"):
        st.markdown("""
        - Laurea in Scienze della Nutrizione Umana
        - Formazione in nutrizione sportiva
        - Formazione in benessere femminile
        """)

    with st.expander("📜 Dati professionali"):
        st.markdown("""
        - **P. IVA:** 03425440736
        - **Iscrizione:** Ordine dei Biologi della Puglia e della Basilicata
        - **Sezione:** A
        - **Numero:** PuB_A5285
        - **Data iscrizione:** 29/07/2024
        """)

with servizi:
    st.title("Di cosa mi occupo")
    st.markdown("Mi occupo di consulenza nutrizionale personalizzata per:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ✅ Dimagrimento e ricomposizione corporea

        ✅ Nutrizione femminile:
        • PCOS (Sindrome dell'Ovaio Policistico)
        • Endometriosi
        • Gravidanza
        • Allattamento
        • Menopausa

        ✅ Patologie metaboliche diagnosticate

        ✅ Alimentazione vegetariana e vegana
        """)
    with col2:
        st.markdown("""
        ✅ Allergie e intolleranze alimentari

        ✅ Disturbi gastrointestinali:
        • Colon irritabile (IBS)
        • MICI
        • Disturbi digestivi e intestinali
        • Altre problematiche dell'apparato digerente

        ✅ Nutrizione sportiva

        ✅ Educazione alimentare e prevenzione
        """)

with percorso:
    st.title("Il percorso nutrizionale")
    st.markdown("""
    Ogni percorso inizia con una valutazione approfondita della persona e del suo stato di salute.

    Durante la prima consulenza vengono analizzati:

    🔹 Abitudini alimentari e stile di vita

    🔹 Obiettivi personali e bisogni specifici

    🔹 Storia clinica e nutrizionale

    🔹 **Composizione corporea** tramite:
    - Analisi bioimpedenziometrica (BIA)
    - Plicometria
    - Rilevazione delle circonferenze corporee

    Questi strumenti consentono di monitorare nel tempo massa muscolare, massa grassa,
    stato di idratazione e progressi del percorso, andando oltre il semplice numero
    indicato dalla bilancia.
    """)

with approccio:
    st.title("Il mio approccio")
    st.markdown("""
    La parola *dieta* deriva dal greco *dìaita* e significa **stile di vita**.

    Per questo motivo il mio lavoro non si basa su regole rigide o privazioni,
    ma sulla costruzione di abitudini alimentari realistiche, equilibrate e sostenibili nel tempo.

    Ogni piano nutrizionale viene personalizzato per adattarsi alla quotidianità,
    alle preferenze alimentari e agli obiettivi della persona.

    💚 Una corretta alimentazione non dovrebbe togliere, ma aggiungere:

    **Benessere — Energia — Consapevolezza — Salute — Qualità della vita**

    L'obiettivo non è seguire una dieta perfetta, ma trovare un equilibrio
    che possa essere mantenuto nel tempo.
    """)

with blog:
    st.title("Blog")
    st.info("Articoli in arrivo! Presto troverai qui consigli e approfondimenti sulla nutrizione.")

    col1, col2, col3 = st.columns(3)
    for col, emoji, title in zip(
        [col1, col2, col3],
        ["🥦", "📝", "📖"],
        ["Consigli alimentari", "Guide pratiche", "Mini Guide"]
    ):
        with col:
            st.markdown(f"### {emoji}")
            st.markdown(f"**{title}**")
            st.markdown("*Prossimamente*")

with contatti:
    st.title("Contatti")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📍 Dove sono")
        st.markdown("**In presenza:** Centro Rigenesis, Parma")
        st.markdown("**Online:** su appuntamento")

        st.markdown("### 🕐 Orari")
        st.markdown("Sabato su appuntamento")

        st.markdown("### 📞 Contattami")
        st.markdown("**Cell:** 334 2780151")
        st.markdown("**Email:** info@centrorigenesis.it")

    with col2:
        st.markdown("### 💬 Richiedi informazioni")
        with st.form("contatti_form"):
            nome = st.text_input("Nome e Cognome")
            email = st.text_input("Email")
            telefono = st.text_input("Telefono")
            messaggio = st.text_area("Messaggio", placeholder="Ciao, vorrei prenotare una consulenza perché...")
            inviato = st.form_submit_button("Invia richiesta")
            if inviato:
                st.success("Grazie! Ti ricontatterò al più presto.")

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6b7280;font-size:0.9rem'>© 2026 Dott.ssa Graziana Ancona — Biologa Nutrizionista — P.IVA 03425440736</div>", unsafe_allow_html=True)
