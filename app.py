import streamlit as st

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Biologa Nutrizionista",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #E8F0E0 0%, #D4E0CC 100%); }
.block-container { background: rgba(255,255,255,0.92); border-radius: 20px; padding: 2rem 3rem; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-top: 1rem; font-size: 1.1rem; }
header { background: transparent !important; }
h1 { font-size: 2rem; } h2 { font-size: 1.6rem; } h3 { font-size: 1.3rem; } h1, h2, h3 { color: #5B7B55; }
.stButton button { background: #8A9A5B; color: white; border-radius: 50px; padding: 8px 32px; font-weight: 600; border: none; }
.stButton button:hover { background: #6B7F5E; }
section[data-testid="stSidebar"] { background: #5B7B55; }
section[data-testid="stSidebar"] * { color: white; }
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 { color: white; }
.st-emotion-cache-1gv3huu { color: white !important; }
[data-testid="stSidebarNav"] span { color: white !important; }
.st-emotion-cache-1v0mbdj { color: white !important; }
[data-testid="stSidebarNavItems"] a { padding: 10px 16px; border-radius: 12px; margin: 2px 0; transition: all 0.2s; }
[data-testid="stSidebarNavItems"] a:hover { background: rgba(255,255,255,0.1); }
[data-testid="stSidebarNavItems"] a[data-testid="stSidebarNavItemActive"] { background: rgba(255,255,255,0.15); border-left: 3px solid white; }
</style>
""", unsafe_allow_html=True)

mini_guide = [
    # Aggiungi qui i tuoi post: (titolo, descrizione, url_instagram)
    # Esempio:
    # ("Colazione sana", "Idee per una colazione equilibrata", "https://www.instagram.com/p/..."),
]

def pagina_home():
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

def pagina_chisono():
    st.title("Chi Sono")
    col_foto, col_testo = st.columns([1, 2])
    with col_foto:
        st.image("img/profilo.jpg", width=250)
    with col_testo:
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

def pagina_servizi():
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

def pagina_percorso():
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

def pagina_approccio():
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

def pagina_blog():
    st.title("Mini Guide dal Blog")
    st.markdown("Segui i miei consigli su Instagram e trovali qui raccolti per te.")

    if not mini_guide:
        st.info("Aggiungi i tuoi post nell'array `mini_guide` in cima al file per farli apparire qui.")
    else:
        cols = st.columns(2)
        for i, (titolo, descrizione, url) in enumerate(mini_guide):
            with cols[i % 2]:
                st.markdown(f"### 📌 {titolo}")
                st.markdown(descrizione)
                st.link_button("Apri su Instagram \u2192", url)
                st.markdown("---")

def pagina_contatti():
    st.title("Contatti")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📍 Dove sono")
        st.markdown("**In presenza:** Centro Rigenesis, Parma")
        st.markdown("**Online:** su appuntamento")

        st.markdown("### 🕐 Orari")
        st.markdown("Sabato su appuntamento")

        st.markdown("### 📞 Contattami")
        st.markdown("**Cell:** 327 0022153")
        st.markdown("**Email:** anconagraziana@gmail.com")
        st.markdown("""
        **Social:**
        🔗 [LinkedIn](https://linkedin.com/in/anconagraziana)
        📸 [Instagram](https://www.instagram.com/nutri_su_insta/)
        """)

    with col2:
        st.markdown("### 💬 Richiedi informazioni")
        with st.form("contatti_form"):
            nome = st.text_input("Nome e Cognome")
            email = st.text_input("Email")
            telefono = st.text_input("Telefono")
            messaggio = st.text_area("Messaggio", placeholder="Ciao, vorrei prenotare una consulenza perché...")
            inviato = st.form_submit_button("Invia richiesta")
            if inviato:
                import urllib.parse, urllib.request
                data = urllib.parse.urlencode({
                    "nome": nome,
                    "email": email,
                    "telefono": telefono,
                    "messaggio": messaggio
                }).encode()
                try:
                    urllib.request.urlopen(
                        "https://formspree.io/f/ILTUO_ENDPOINT_QUI",
                        data=data
                    )
                    st.success("Grazie! Ti ricontatterò al più presto.")
                except:
                    st.error("Errore nell'invio. Scrivimi direttamente a anconagraziana@gmail.com")

pg = st.navigation([
    st.Page(pagina_home, title="Home", icon="🏠", default=True),
    st.Page(pagina_chisono, title="Chi Sono", icon="👩‍⚕️"),
    st.Page(pagina_servizi, title="Di cosa mi occupo", icon="📋"),
    st.Page(pagina_percorso, title="Percorso", icon="📊"),
    st.Page(pagina_approccio, title="Approccio", icon="🌿"),
    st.Page(pagina_blog, title="Blog", icon="📖"),
    st.Page(pagina_contatti, title="Contatti", icon="📬"),
])
pg.run()

st.markdown("---")
st.markdown("<div style='text-align:center;color:#6b7280;font-size:0.9rem'>© 2026 Dott.ssa Graziana Ancona — Biologa Nutrizionista — P.IVA 03425440736</div>", unsafe_allow_html=True)
