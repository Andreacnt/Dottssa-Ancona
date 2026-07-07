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

home, chisono, servizi, blog, contatti = st.tabs(["🏠 Home", "👩‍⚕️ Chi Sono", "📋 Servizi", "📖 Blog", "📬 Contatti"])

with home:
    st.title("Dott.ssa Graziana Ancona — Biologa Nutrizionista")
    st.markdown("""
    Accompagno persone di ogni età in percorsi nutrizionali personalizzati,
    costruiti sulle esigenze individuali e basati sulle più recenti evidenze scientifiche.
    Il mio obiettivo è aiutare ogni persona a sviluppare un rapporto più sereno, consapevole
    e sostenibile con l'alimentazione, migliorando il proprio stato di salute e il benessere generale.
    """)

    st.markdown("📍 Consulenze in presenza presso **Centro Rigenesis, Parma** · Online su appuntamento")
    st.markdown("🕐 Sabato su appuntamento")

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

    with st.expander("🌿 Il mio approccio"):
        st.markdown("""
        La parola *dieta* deriva dal greco *dìaita* e significa **stile di vita**.

        Il mio lavoro non si basa su regole rigide o privazioni, ma sulla costruzione
        di abitudini alimentari realistiche, equilibrate e sostenibili nel tempo.

        💚 Una corretta alimentazione non dovrebbe togliere, ma aggiungere:
        **Benessere, Energia, Consapevolezza, Salute, Qualità della vita**.

        L'obiettivo non è seguire una dieta perfetta, ma trovare un equilibrio
        che possa essere mantenuto nel tempo.
        """)

with servizi:
    st.title("Servizi")

    servizi_list = [
        ("🥗", "Consulenza nutrizionale individuale", "Percorso personalizzato con piano alimentare su misura e follow-up periodici."),
        ("📉", "Dimagrimento e ricomposizione corporea", "Perdita di peso sana con monitoraggio BIA, plicometria e circonferenze."),
        ("👩", "Nutrizione femminile", "Supporto per PCOS, endometriosi, gravidanza, allattamento e menopausa."),
        ("🩺", "Patologie metaboliche", "Alimentazione mirata per diabete, colesterolo, ipertensione, sindrome metabolica."),
        ("🌱", "Alimentazione vegetariana e vegana", "Piani bilanciati per chi sceglie un'alimentazione a base vegetale."),
        ("🤧", "Allergie e intolleranze", "Educazione alimentare per gestire allergie e intolleranze senza rinunce."),
        ("🫀", "Disturbi gastrointestinali", "Supporto per IBS, MICI, disturbi digestivi e intestinali."),
        ("🏃", "Nutrizione sportiva", "Piani per ottimizzare performance, recupero e composizione corporea."),
        ("👶", "Educazione alimentare", "Prevenzione e corretta alimentazione per tutte le età."),
        ("💻", "Consulenza online", "Stessa cura, comodamente da casa tua.")
    ]

    cols = st.columns(2)
    for i, (icon, title, desc) in enumerate(servizi_list):
        with cols[i % 2]:
            st.markdown(f"**{icon} {title}**")
            st.markdown(f"{desc}")
            st.markdown("")

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
