import streamlit as st

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Biologa Nutrizionista",
    page_icon="img/logo.jpg",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');
.stApp { background: linear-gradient(135deg, #E8F0E0 0%, #D4E0CC 100%); }
.block-container { background: rgba(255,255,255,0.92); border-radius: 20px; padding: 2rem 3rem; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-top: 1rem; font-size: 1.1rem; font-family: 'Inter', sans-serif; }
header { background: transparent !important; }
h1, h2, h3 { font-family: 'Playfair Display', serif; color: #5B7B55; }
h1 { font-size: 2rem; background: linear-gradient(135deg, #5B7B55, #8A9A5B); -webkit-background-clip: text; -webkit-text-fill-color: transparent; display: inline-block; }
h2 { font-size: 1.6rem; } h3 { font-size: 1.3rem; }
.stButton button { background: #8A9A5B; color: white; border-radius: 50px; padding: 8px 32px; font-weight: 600; border: none; transition: all 0.2s; font-family: 'Inter', sans-serif; }
.stButton button:hover { background: #6B7F5E; }
.stButton button:active { transform: scale(0.96); }
img[src*="profilo.jpg"] { border-radius: 50% !important; aspect-ratio: 1 !important; object-fit: cover !important; object-position: top !important; }
section[data-testid="stSidebar"] { background: #5B7B55; }
section[data-testid="stSidebar"] * { color: white; font-family: 'Inter', sans-serif; }
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 { color: white; }
[data-testid="stSidebarNavItems"] a { padding: 10px 16px; border-radius: 12px; margin: 2px 0; transition: all 0.2s; }
[data-testid="stSidebarNavItems"] a:hover { background: rgba(255,255,255,0.1); transform: translateX(3px); }
[data-testid="stSidebarNavItems"] a:active { transform: scale(0.96); background: rgba(255,255,255,0.2); }
[data-testid="stSidebarNavItems"] a[data-testid="stSidebarNavItemActive"] { background: rgba(255,255,255,0.15); border-left: 3px solid white; }
.servizio-card { background: #f5f9f2; border-radius: 16px; padding: 1.2rem 1.5rem; margin: 0.5rem 0; border-left: 4px solid #8A9A5B; }
.divider { text-align: center; color: #B2C9AB; font-size: 1.2rem; margin: 0.5rem 0; }
.footer { text-align: center; color: #6b7280; font-size: 0.9rem; padding-top: 1rem; border-top: 1px solid #e5e7eb; }
@media (max-width: 768px) {
  .block-container { padding: 0.8rem 1rem !important; font-size: 1rem !important; margin-top: 0.5rem !important; }
  h1 { font-size: 1.5rem !important; } h2 { font-size: 1.2rem !important; } h3 { font-size: 1.1rem !important; }
  img[src*="profilo.jpg"] { width: 160px !important; }
  [data-testid="column"] { min-width: 100% !important; flex: 0 0 100% !important; padding: 0.3rem 0 !important; }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="divider">✦ &#127793; ✦</p>', unsafe_allow_html=True)

mini_guide = [
    ("Latte, latti fermentati e yogurt: simili, ma non uguali",
     "Scopri le differenze tra questi alimenti e come sceglierli al meglio.",
     "https://www.instagram.com/p/DU5_E9BihXJ/"),
    ("Cereali: energia quotidiana e base della dieta mediterranea",
     "Il carburante giusto per affrontare la giornata con energia.",
     "https://www.instagram.com/p/DU0yDUJio73/"),
    ("Mangiare a colori è uno dei modi più semplici per prendersi cura della salute.",
     "Ogni colore sulla tavola porta benefici diversi al tuo organismo.",
     "https://www.instagram.com/p/DUK5SU8Cg4t/"),
    ("Parliamo di stagionalità: un elemento chiave per salute, gusto e sostenibilità.",
     "Un elemento chiave per fare la spesa in modo consapevole.",
     "https://www.instagram.com/p/DUDYE2pivoC/"),
    ("Frutta e verdura: un tripudio di salute e colore!",
     "Più ne mettete nel piatto, più il vostro corpo vi ringrazierà.",
     "https://www.instagram.com/p/DT-NU3zCu5w/"),
    ("Pizza: molto più di un piatto",
     "Si può inserire in un'alimentazione equilibrata? Certamente sì.",
     "https://www.instagram.com/p/DTm3eihCnPa/"),
    ("A Natale si sgarra",
     "Consigli per godersi le feste senza sensi di colpa.",
     "https://www.instagram.com/p/DS2INCSCjOj/"),
    ("I legumi: piccoli, ma potentissimi!",
     "Colorati, versatili e ricchi di nutrienti, da consumare almeno 4 volte a settimana.",
     "https://www.instagram.com/p/DRkNOkbig0P/"),
    ("I carboidrati dopo le 18 fanno ingrassare!",
     "Sfatiamo insieme uno dei miti più comuni sull'alimentazione.",
     "https://www.instagram.com/p/DOgk-NfCg5t/"),
    ("Il Piatto del Mangiar Sano",
     "Un metodo semplice e visivo per costruire pasti equilibrati.",
     "https://www.instagram.com/p/DOd3N62igRl/"),
    ("Le ferie sono finite e tornare alla routine non è sempre semplice.",
     "Consigli per riprendere le buone abitudini dopo le ferie.",
     "https://www.instagram.com/p/DN2llBd1Mx8/"),
    ("La parola dieta deriva dal greco e significa stile di vita.",
     "Il mio approccio alla nutrizione: equilibrio, non privazione.",
     "https://www.instagram.com/p/DNkhhUPsWlb/"),
]

def pagina_home():
    st.image("img/sfondo.jpg", use_container_width=True)
    st.title("Dott.ssa Graziana Ancona — Biologa Nutrizionista")
    st.markdown("""
    Accompagno persone di ogni età in percorsi nutrizionali personalizzati,
    costruiti sulle esigenze individuali e basati sulle più recenti evidenze scientifiche.
    Il mio obiettivo è aiutare ogni persona a sviluppare un rapporto più sereno, consapevole
    e sostenibile con l'alimentazione, migliorando il proprio stato di salute e il benessere generale.
    """)

    st.markdown("""
    📍 **Consulenze in presenza:** sabato su appuntamento presso Centro Rigenesis, Viale La Grola 5/B, Parma

    💻 **Consulenze online:** su appuntamento
    """)

def pagina_chisono():
    st.title("Chi Sono")
    col_foto, col_testo = st.columns([1, 2])
    with col_foto:
        st.image("https://raw.githubusercontent.com/Andreacnt/Dottssa-Ancona/main/img/profilo.jpg", width=200)
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
        st.markdown('<div class="servizio-card">⚖️ **Dimagrimento e ricomposizione corporea**</div>', unsafe_allow_html=True)
        st.markdown('<div class="servizio-card">🌸 **Nutrizione femminile**<br>• PCOS • Endometriosi • Gravidanza • Allattamento • Menopausa</div>', unsafe_allow_html=True)
        st.markdown('<div class="servizio-card">🩺 **Patologie metaboliche diagnosticate**</div>', unsafe_allow_html=True)
        st.markdown('<div class="servizio-card">🌱 **Alimentazione vegetariana e vegana**</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="servizio-card">🌾 **Allergie e intolleranze alimentari**</div>', unsafe_allow_html=True)
        st.markdown('<div class="servizio-card">🥗 **Disturbi gastrointestinali**<br>• Colon irritabile (IBS) • MICI • Disturbi digestivi e intestinali</div>', unsafe_allow_html=True)
        st.markdown('<div class="servizio-card">💪 **Nutrizione sportiva**</div>', unsafe_allow_html=True)
        st.markdown('<div class="servizio-card">📚 **Educazione alimentare e prevenzione**</div>', unsafe_allow_html=True)

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
        st.markdown("**In presenza:** Centro Rigenesis")
        st.markdown("Viale La Grola, 5/B — 43125 Parma")
        st.markdown("[Apri su Google Maps](https://maps.google.com/maps?q=Viale+La+Grola+5/B+Parma+43125)")
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
        st.markdown("### 💬 Scrivimi")
        st.markdown("Compila il form qui sotto e ti rispondo direttamente via email.")
        st.markdown(
            f'<a href="mailto:anconagraziana@gmail.com?subject=Richiesta%20consulenza&body=Ciao%20Dott.ssa%20Ancona%2C%0A%0AVorrei%20prenotare%20una%20consulenza%20perché...%0A%0ANome%3A%0ATelefono%3A" style="display:inline-block;background:#8A9A5B;color:white;border-radius:50px;padding:12px 32px;font-weight:600;text-decoration:none;margin-top:0.5rem;">✉️ Scrivimi via email</a>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown(
        '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2830.54132679946!2d10.311615611314664!3d44.810535470950065!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47806b8f8ab09825%3A0xa381d4de6169890f!2sRigenesis!5e0!3m2!1sit!2sit!4v1783455655720!5m2!1sit!2sit" width="100%" height="300" style="border:0;border-radius:16px;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>',
        unsafe_allow_html=True
    )

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
st.markdown("""
<div class="footer">
  <p><strong>Dott.ssa Graziana Ancona</strong> — Biologa Nutrizionista</p>
  <p>Centro Rigenesis · Viale La Grola 5/B, Parma · Sabato su appuntamento</p>
  <p>📞 327 0022153 · ✉️ anconagraziana@gmail.com</p>
  <p>🔗 <a href="https://linkedin.com/in/anconagraziana" style="color:#6b7280;">LinkedIn</a> · 📸 <a href="https://www.instagram.com/nutri_su_insta/" style="color:#6b7280;">Instagram</a></p>
  <p style="margin-top:0.5rem;font-size:0.8rem;">© 2026 — P.IVA 03425440736</p>
</div>
""", unsafe_allow_html=True)
