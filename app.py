import streamlit as st

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Nutrizionista",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); }
.block-container { background: rgba(255,255,255,0.92); border-radius: 20px; padding: 2rem 3rem; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-top: 1rem; }
header { background: transparent !important; }
.nav a { text-decoration: none; color: #374151; font-weight: 500; margin-right: 24px; font-size: 0.9rem; }
.nav a:hover { color: #16a34a; }
h1, h2, h3 { color: #14532d; }
.stButton button { background: #16a34a; color: white; border-radius: 50px; padding: 8px 32px; font-weight: 600; border: none; }
.stButton button:hover { background: #15803d; }
</style>
""", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("### 🥗")
    with col2:
        st.markdown("### Dott.ssa Graziana Ancona")
        st.markdown("*Biologa Nutrizionista*")

st.markdown("---")

home, chisono, servizi, blog, contatti = st.tabs(["🏠 Home", "👩‍⚕️ Chi Sono", "📋 Servizi", "📖 Blog", "📬 Contatti"])

with home:
    st.title("Raggiungi il tuo benessere con un'alimentazione su misura")
    st.markdown("Ti aiuto a ritrovare equilibrio e salute attraverso la nutrizione personalizzata.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🥗 Percorsi alimentari personalizzati**
        Piani nutrizionali su misura per le tue esigenze.

        **📊 Educazione alimentare**
        Impara a mangiare in modo consapevole.

        **🩺 Supporto a patologie**
        Alimentazione per diabete, colesterolo, intolleranze.
        """)
    with col2:
        st.markdown("""
        **👶 Nutrizione in ogni fase della vita**
        Adolescenza, gravidanza, terza età.

        **🧠 Benessere mentale e cibo**
        Il legame tra alimentazione e umore.

        **🏡 Consulenze online e in presenza**
        A Senigallia o da casa tua.
        """)

    st.markdown("---")
    st.markdown("📍 Senigallia (AN) · Consulenze online su tutta Italia")

with chisono:
    st.title("Chi Sono")
    st.markdown("Sono una **Biologa Nutrizionista**, iscritta all'Ordine dei Biologi.")
    st.markdown("Credo che non esista una dieta universale: ogni persona ha esigenze uniche. Il mio lavoro è ascoltare, capire e costruire insieme un percorso su misura.")

    with st.expander("🎓 Formazione"):
        st.markdown("""
        - Laurea Magistrale in Biologia
        - Master in Nutrizione e Dietetica Clinica
        - Iscrizione all'Albo dei Biologi
        """)

    with st.expander("💡 Come lavoro"):
        st.markdown("""
        1. Primo colloquio conoscitivo gratuito
        2. Analisi delle abitudini alimentari e dello stile di vita
        3. Piano alimentare personalizzato e flessibile
        4. Monitoraggio e adattamento nel tempo
        """)

with servizi:
    st.title("Servizi")

    servizi_list = [
        ("🥗", "Consulenza nutrizionale individuale", "Percorso one-to-one con piano alimentare personalizzato e follow-up."),
        ("📉", "Percorso dimagrimento", "Perdita di peso sana e duratura, senza diete drastiche."),
        ("🩺", "Nutrizione clinica", "Supporto per diabete, ipertensione, colesterolo, disturbi gastrointestinali."),
        ("🤰", "Gravidanza e allattamento", "Alimentazione per il benessere di mamma e bambino."),
        ("🏃", "Nutrizione sportiva", "Piani per ottimizzare performance e recupero."),
        ("👶", "Nutrizione pediatrica", "Educazione alimentare per bambini e adolescenti."),
        ("💻", "Consulenza online", "Stessa cura, comodamente da casa tua.")
    ]
    for icon, title, desc in servizi_list:
        with st.container():
            c1, c2 = st.columns([1, 5])
            with c1:
                st.markdown(f"### {icon}")
            with c2:
                st.markdown(f"**{title}**")
                st.markdown(f"{desc}")

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
        st.markdown("Senigallia (AN) — studio in centro")
        st.markdown("Consulenze online su tutta Italia")

        st.markdown("### 📞 Contattami")
        st.markdown("**Email:** graziana.ancona@gmail.com")
        st.markdown("**Cell:** +39 333 789 1234")

        st.markdown("### 🕐 Orari")
        st.markdown("Lun-Ven: 9:00 – 19:00")
        st.markdown("Sab: su appuntamento")

    with col2:
        st.markdown("### 💬 Richiedi informazioni")
        with st.form("contatti_form"):
            nome = st.text_input("Nome e Cognome")
            email = st.text_input("Email")
            telefono = st.text_input("Telefono (opzionale)")
            messaggio = st.text_area("Il tuo messaggio", placeholder="Ciao, vorrei prenotare una consulenza perché...")
            inviato = st.form_submit_button("Invia richiesta")
            if inviato:
                st.success("Richiesta inviata! Ti ricontatterò presto.")

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6b7280;font-size:0.9rem'>© 2026 Dott.ssa Graziana Ancona — Biologa Nutrizionista</div>", unsafe_allow_html=True)
