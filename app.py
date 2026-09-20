import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Biologa Nutrizionista",
    page_icon="img/logo.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SFONDO_URL = "https://raw.githubusercontent.com/Andreacnt/Dottssa-Ancona/main/img/sfondo.jpg"
PROFILO_URL = "https://raw.githubusercontent.com/Andreacnt/Dottssa-Ancona/main/img/profilo.jpg"
WA_URL = "https://wa.me/393203190704?text=Ciao%20Dott.ssa%20Ancona%2C%20vorrei%20informazioni%20per%20una%20consulenza"
MAIL_URL = "mailto:anconagraziana@gmail.com?subject=Richiesta%20consulenza&body=Ciao%20Dott.ssa%20Ancona%2C%0A%0AVorrei%20prenotare%20una%20consulenza%20perch%C3%A9...%0A%0ANome%3A%0ATelefono%3A"
IG_URL = "https://www.instagram.com/nutri_su_insta/"
LINKEDIN_URL = "https://linkedin.com/in/anconagraziana"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

.stApp { background: #F4F7F0; }

.main > .block-container { max-width: 1080px; padding-top: 0 !important; }

h1, h2, h3 { font-family: 'Playfair Display', serif; color: #3D5A3D; }
h1 { font-size: 2.2rem; }
h2 { font-size: 1.6rem; }
h3 { font-size: 1.25rem; }

p, li, .stMarkdown { font-family: 'Inter', sans-serif; color: #2D3436; line-height: 1.7; }

.page-wrap { padding: 2rem 1rem; }

.kicker {
  font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 700;
  color: #8A9A5B; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.4rem;
}

section[data-testid="stSidebar"] { background: #3D5A3D; }
section[data-testid="stSidebar"] * { color: white; }
[data-testid="stSidebarNavItems"] a { padding: 10px 16px; border-radius: 12px; margin: 2px 0; }
[data-testid="stSidebarNavItems"] a[data-testid="stSidebarNavItemActive"] { background: rgba(255,255,255,0.15); border-left: 3px solid white; }

.hero {
  position: relative; width: 100vw; margin-left: calc(-50vw + 50%);
  min-height: 78vh; display: flex; align-items: center; justify-content: center;
  overflow: hidden; text-align: center;
}
.hero-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 30%; }
.hero-veil {
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(61,90,61,0.90), rgba(91,123,85,0.75) 45%, rgba(138,154,91,0.50));
}
.hero-inner { position: relative; z-index: 2; padding: 3rem 1.5rem; max-width: 820px; }
.hero-inner .over { font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 300; letter-spacing: 3px; text-transform: uppercase; color: rgba(255,255,255,0.85); }
.hero-inner h1 { font-size: 3.2rem; color: white; margin: 0.4rem 0; line-height: 1.15; }
.hero-inner .sub { font-family: 'Playfair Display', serif; font-size: 1.5rem; color: white; margin-bottom: 2rem; }
.btn-light {
  display: inline-block; background: white; color: #3D5A3D; font-family: 'Inter', sans-serif;
  font-weight: 700; padding: 14px 44px; border-radius: 50px; text-decoration: none; font-size: 1.05rem;
  box-shadow: 0 4px 25px rgba(0,0,0,0.18);
}
.hero-social { margin-top: 2rem; }
.hero-social a { color: rgba(255,255,255,0.8); text-decoration: none; font-size: 1.05rem; margin: 0 0.7rem; font-family: 'Inter', sans-serif; }

.card {
  background: white; border-radius: 16px; padding: 1.6rem;
  box-shadow: 0 2px 20px rgba(0,0,0,0.06); border: 1px solid rgba(91,123,85,0.08); height: 100%;
}
.card-icon { font-size: 2rem; margin-bottom: 0.4rem; }
.card h3 { margin-bottom: 0.4rem; }
.card p { font-size: 0.95rem; color: #636E72; }

.svc {
  background: white; border-radius: 16px; padding: 1.2rem 1.4rem; margin: 0.5rem 0;
  border-left: 4px solid #5B7B55; box-shadow: 0 2px 20px rgba(0,0,0,0.06);
  font-family: 'Inter', sans-serif; color: #2D3436;
}
.svc small { color: #636E72; }

.cta {
  background: linear-gradient(135deg, #3D5A3D, #5B7B55 55%, #8A9A5B);
  border-radius: 16px; padding: 3rem 2rem; text-align: center; margin: 2.2rem 0;
}
.cta h2 { color: white; font-size: 1.8rem; margin-bottom: 0.6rem; }
.cta p { color: rgba(255,255,255,0.9); max-width: 620px; margin: 0 auto 1.6rem; font-size: 1.05rem; }

.step-n {
  display: inline-flex; align-items: center; justify-content: center;
  width: 42px; height: 42px; border-radius: 50%;
  background: linear-gradient(135deg, #5B7B55, #8A9A5B);
  color: white; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 1.15rem;
}

.post {
  background: white; border-radius: 16px; box-shadow: 0 2px 20px rgba(0,0,0,0.06);
  border: 1px solid rgba(91,123,85,0.08); height: 100%;
  display: flex; flex-direction: column;
}
.post-body { padding: 1.4rem; flex: 1; display: flex; flex-direction: column; }
.post-body h3 { font-size: 1.1rem; margin-bottom: 0.4rem; }
.post-body p { font-size: 0.9rem; color: #636E72; flex: 1; }
.post-link { color: #5B7B55; font-weight: 700; text-decoration: none; font-size: 0.92rem; font-family: 'Inter', sans-serif; margin-top: 0.8rem; }

.ig-box {
  background: white; border-radius: 16px; padding: 2.2rem 1.5rem;
  box-shadow: 0 2px 20px rgba(0,0,0,0.06); border: 1px solid rgba(91,123,85,0.08);
  margin: 2rem 0; text-align: center;
}
.ig-btn {
  display: inline-block; background: linear-gradient(135deg, #5B7B55, #8A9A5B); color: white;
  font-family: 'Inter', sans-serif; font-weight: 700; padding: 13px 38px;
  border-radius: 50px; text-decoration: none; font-size: 1rem;
}

.btn-mail, .btn-wa {
  display: inline-block; font-family: 'Inter', sans-serif; font-weight: 700;
  padding: 13px 34px; border-radius: 50px; text-decoration: none; font-size: 1rem; margin: 0.3rem;
}
.btn-mail { background: #8A9A5B; color: white; }
.btn-wa { background: #25D366; color: white; }

img[src*="profilo.jpg"] { border-radius: 50% !important; aspect-ratio: 1 !important; object-fit: cover !important; object-position: top center !important; border: 4px solid #5B7B55 !important; }

.streamlit-expanderHeader { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: #3D5A3D; background: white; border-radius: 12px; }

.sep { text-align: center; color: #8A9A5B; opacity: 0.45; font-size: 1.15rem; margin: 1.2rem 0; }

.footer {
  background: #3D5A3D; text-align: center; padding: 3rem 1.5rem;
  width: 100vw; margin-left: calc(-50vw + 50%); margin-top: 3rem;
}
.footer h4 { font-family: 'Playfair Display', serif; color: white; font-size: 1.3rem; margin-bottom: 0.4rem; }
.footer p { color: rgba(255,255,255,0.78); font-size: 0.95rem; margin: 0.25rem 0; }
.footer a { color: #B2C9AB; text-decoration: none; }
.footer-rule { width: 44px; height: 2px; background: #8A9A5B; margin: 1rem auto; opacity: 0.6; }
.footer-social a { font-size: 1.05rem; margin: 0 0.6rem; }

@media (max-width: 768px) {
  .hero { min-height: 68vh; }
  .hero-inner h1 { font-size: 2rem; }
  .hero-inner .sub { font-size: 1.15rem; }
  .page-wrap { padding: 1.2rem 0.4rem; }
  h1 { font-size: 1.7rem; }
  h2 { font-size: 1.35rem; }
  .cta { padding: 2.2rem 1.2rem; }
  .cta h2 { font-size: 1.4rem; }
}
</style>
""", unsafe_allow_html=True)

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

servizi_card = [
    ("⚖️", "Dimagrimento e ricomposizione corporea", ""),
    ("🌸", "Nutrizione femminile", "PCOS · Endometriosi · Gravidanza · Allattamento · Menopausa"),
    ("🩺", "Patologie metaboliche diagnosticate", ""),
    ("🌱", "Alimentazione vegetariana e vegana", ""),
    ("🌾", "Allergie e intolleranze alimentari", ""),
    ("🥗", "Disturbi gastrointestinali", "Colon irritabile (IBS) · MICI · Disturbi digestivi e intestinali"),
    ("💪", "Nutrizione sportiva", ""),
    ("📚", "Educazione alimentare e prevenzione", ""),
]


def cta_box(titolo, testo):
    st.markdown(f"""
    <div class="cta">
      <h2>{titolo}</h2>
      <p>{testo}</p>
      <a href="{WA_URL}" target="_blank" class="btn-light">Prenota una visita</a>
    </div>
    """, unsafe_allow_html=True)


def pagina_home():
    st.markdown(f"""
    <div class="hero">
      <img class="hero-bg" src="{SFONDO_URL}" alt="">
      <div class="hero-veil"></div>
      <div class="hero-inner">
        <div class="over">Biologa Nutrizionista</div>
        <h1>Dott.ssa Graziana Ancona</h1>
        <div class="sub">Nutrizione personalizzata per il tuo benessere</div>
        <a href="{WA_URL}" target="_blank" class="btn-light">Prenota una visita</a>
        <div class="hero-social">
          <a href="{IG_URL}" target="_blank">Instagram</a>
          <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
          <a href="{MAIL_URL}">Email</a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Chi sono</div>', unsafe_allow_html=True)

    col_foto, col_testo = st.columns([1, 2.2])
    with col_foto:
        st.image(PROFILO_URL, width=250)
    with col_testo:
        st.markdown("""
        ### Accompagnarti verso il tuo benessere
        Ogni corpo ha una storia e ogni età ha le sue esigenze. Per questo non credo nelle soluzioni universali, ma in percorsi nutrizionali personalizzati e basati su solide basi scientifiche. Il mio obiettivo non è darti una dieta rigida, ma aiutarti a sviluppare un rapporto sereno, consapevole e sostenibile con il cibo. Insieme, trasformeremo l'alimentazione nel tuo strumento principale per vivere meglio e ritrovare il tuo equilibrio naturale.
        """)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Di cosa mi occupo</div>', unsafe_allow_html=True)
    st.markdown("### Aree di intervento")

    cols = st.columns(4)
    for i, (icona, titolo, _) in enumerate(servizi_card):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
              <div class="card-icon">{icona}</div>
              <h3>{titolo}</h3>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin:1.6rem 0; font-family:'Inter',sans-serif; color:#636E72;">
      📍 <strong style="color:#2D3436;">Consulenze in presenza:</strong> sabato su appuntamento presso Centro Rigenesis, Viale La Grola 5/B, Parma<br>
      💻 <strong style="color:#2D3436;">Consulenze online:</strong> su appuntamento
    </div>
    """, unsafe_allow_html=True)

    cta_box(
        "Inizia il tuo percorso",
        "Prenota una consulenza personalizzata e scopri come raggiungere i tuoi obiettivi di benessere con un metodo scientifico e sostenibile.",
    )
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_chisono():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Chi sono</div>', unsafe_allow_html=True)
    st.title("Chi Sono")

    col_foto, col_testo = st.columns([1, 2])
    with col_foto:
        st.image(PROFILO_URL, width=260)
    with col_testo:
        st.markdown("""
        Sono la **Dott.ssa Graziana Ancona**, **Biologa Nutrizionista**. Dopo la laurea in Scienze della Nutrizione Umana, ho focalizzato le mie competenze e la mia formazione nell'ambito della **salute della donna** in ogni fase della vita e della **nutrizione per lo sport**. ✨ Metto le mie competenze al tuo servizio per dimostrarti che mangiare bene è un atto di cura, non di sacrificio. Il mio obiettivo è darti gli strumenti scientifici e pratici per valorizzare il tuo corpo, trovare la tua energia migliore e investire sulla tua salute.
        """)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🎓 Formazione"):
            st.markdown("""
            - Scienze gastronomiche
            - Scienze della Nutrizione Umana
            - Scuola di nutrizione e integrazione nello sport (sanis)
            - Esperta in Benessere e salute della donna
            """)
    with col_b:
        with st.expander("📜 Dati professionali"):
            st.markdown("""
            - **P. IVA:** 03425440736
            - **Iscrizione:** Ordine dei Biologi della Puglia e della Basilicata
            - **Sezione:** A
            - **Numero:** PuB_A5285
            - **Data iscrizione:** 29/07/2024
            """)

    cta_box(
        "Vuoi conoscermi meglio?",
        "Prenota una prima consulenza: ti ascolterò e costruiremo insieme il percorso più adatto a te.",
    )
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_servizi():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Servizi</div>', unsafe_allow_html=True)
    st.title("Di cosa mi occupo")
    st.markdown("Mi occupo di consulenza nutrizionale personalizzata per:")

    cols = st.columns(2)
    for i, (icona, titolo, dettaglio) in enumerate(servizi_card):
        with cols[i % 2]:
            extra = f"<br><small>{dettaglio}</small>" if dettaglio else ""
            st.markdown(f'<div class="svc">{icona} <strong>{titolo}</strong>{extra}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)
    st.markdown("### Il percorso in 4 passi")

    passi = [
        ("Colloquio iniziale", "Abitudini, obiettivi e storia clinica"),
        ("Valutazione", "BIA, plicometria e circonferenze"),
        ("Piano personalizzato", "Realistico e sostenibile nel tempo"),
        ("Monitoraggio", "Follow-up e aggiustamenti del percorso"),
    ]
    cols = st.columns(4)
    for i, (titolo, desc) in enumerate(passi):
        with cols[i]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
              <div class="step-n" style="margin:0 auto 0.8rem;">{i + 1}</div>
              <h3>{titolo}</h3>
              <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    cta_box(
        "Pronto per iniziare?",
        "Contattami per una prima consulenza: valuteremo insieme il percorso più adatto alle tue esigenze.",
    )
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_percorso():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Percorso</div>', unsafe_allow_html=True)
    st.title("Il percorso nutrizionale")
    st.markdown("### Cosa faremo insieme: la prima consulenza")
    st.markdown("""
    <p>Ogni percorso nutrizionale è un viaggio che parte da te. Nel nostro primo incontro effettueremo una valutazione approfondita della tua storia e del tuo stato di salute attuale, analizzando ogni dettaglio per costruire un piano davvero personalizzato.</p>
    <p>Durante la prima consulenza valuteremo:</p>
    <ul style="list-style:none; padding-left:0;">
      <li style="margin-bottom:0.9rem;">• <strong>Abitudini e Stile di Vita:</strong> Per capire i tuoi ritmi quotidiani e adattare il piano alla tua routine.</li>
      <li style="margin-bottom:0.9rem;">• <strong>Obiettivi e Bisogni:</strong> I traguardi che desideri raggiungere e le tue necessità specifiche.</li>
      <li style="margin-bottom:0.9rem;">• <strong>Storia Clinica e Nutrizionale:</strong> Il tuo punto di partenza medico e i percorsi già affrontati.</li>
      <li style="margin-bottom:0.9rem;">• <strong>Composizione Corporea Avanzata:</strong> Una fotografia precisa del tuo corpo che eseguiamo attraverso:
        <ul style="list-style:none; padding-left:1.5rem; margin-top:0.5rem;">
          <li>◦ <strong>Analisi Bioimpedenziometrica (BIA)</strong></li>
          <li>◦ <strong>Plicometria</strong></li>
          <li>◦ <strong>Rilevazione delle circonferenze corporee</strong></li>
        </ul>
      </li>
    </ul>
    <p>🎯 <strong>Oltre la Bilancia:</strong> Questi strumenti scientifici ci permettono di monitorare con precisione la massa muscolare, la massa grassa e lo stato di idratazione. In questo modo vedremo i tuoi reali progressi nel tempo, andando ben oltre il semplice numero sulla bilancia.</p>
    """, unsafe_allow_html=True)

    cta_box(
        "Inizia il tuo percorso nutrizionale",
        "Ogni giorno è quello giusto per prenderti cura di te.",
    )
    st.markdown('</div>', unsafe_allow_html=True)

def pagina_approccio():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Approccio</div>', unsafe_allow_html=True)
    st.title("Il mio approccio")

    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        st.markdown("""
        La parola *dieta* deriva dal greco *dìaita* e significa **stile di vita**.

        Per questo motivo il mio lavoro non si basa su regole rigide o privazioni,
        ma sulla costruzione di abitudini alimentari realistiche, equilibrate e sostenibili nel tempo.

        Ogni piano nutrizionale viene personalizzato per adattarsi alla quotidianità,
        alle preferenze alimentari e agli obiettivi della persona.

        L'obiettivo non è seguire una dieta perfetta, ma trovare un equilibrio
        che possa essere mantenuto nel tempo.
        """)
    with col_b:
        st.markdown("""
        <div class="card" style="text-align:center;">
          <div style="font-size:2.6rem; margin-bottom:0.4rem;">💚</div>
          <p style="font-style:italic; color:#636E72;">
          Una corretta alimentazione non dovrebbe togliere, ma aggiungere.
          </p>
          <p><strong>Benessere — Energia — Consapevolezza — Salute — Qualità della vita</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)
    st.markdown("### I pilastri del metodo")

    cols = st.columns(3)
    pilastri = [
        ("🧠", "Educazione alimentare", "Scelte consapevoli, senza regole impositive"),
        ("🌿", "Sostenibilità", "Abitudini mantenibili nel tempo"),
        ("❤️", "Benessere globale", "Energia, salute, rapporto sereno col cibo"),
    ]
    for i, (icona, titolo, desc) in enumerate(pilastri):
        with cols[i]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
              <div class="card-icon">{icona}</div>
              <h3>{titolo}</h3>
              <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    cta_box(
        "Trova il tuo equilibrio",
        "Contattami per una consulenza: troveremo insieme la strada giusta per te.",
    )
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_blog():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Blog</div>', unsafe_allow_html=True)
    st.title("Mini Guide dal Blog")
    st.markdown("Segui i miei consigli su Instagram e trovali qui raccolti per te.")

    if not mini_guide:
        st.info("Aggiungi i tuoi post nell'array `mini_guide` in cima al file per farli apparire qui.")
    else:
        cols = st.columns(3)
        for i, (titolo, descrizione, url) in enumerate(mini_guide):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="post">
                  <div class="post-body">
                    <h3>📌 {titolo}</h3>
                    <p>{descrizione}</p>
                    <a class="post-link" href="{url}" target="_blank">Apri su Instagram →</a>
                  </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="ig-box">
      <div style="font-size:2rem; margin-bottom:0.4rem;">📸</div>
      <h3>Seguimi su Instagram</h3>
      <p style="color:#636E72; margin-bottom:1.2rem;">@nutri_su_insta — consigli e approfondimenti</p>
      <a class="ig-btn" href="{IG_URL}" target="_blank">Seguimi su Instagram</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_contatti():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Contatti</div>', unsafe_allow_html=True)
    st.title("Contatti")

    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("""
        <div class="card" style="margin-bottom:1rem;">
          <h3>📍 Dove sono</h3>
          <p><strong>In presenza:</strong> Centro Rigenesis<br>
          Viale La Grola, 5/B — 43125 Parma<br>
          <a href="https://maps.google.com/maps?q=Viale+La+Grola+5/B+Parma+43125" target="_blank" style="color:#5B7B55;">Apri su Google Maps →</a></p>
          <p><strong>Online:</strong> su appuntamento</p>
        </div>
        <div class="card" style="margin-bottom:1rem;">
          <h3>🕐 Orari</h3>
          <p>Sabato su appuntamento</p>
        </div>
        <div class="card">
          <h3>📞 Contattami</h3>
          <p><strong>Cell:</strong> 320 3190704<br>
          <strong>Email:</strong> anconagraziana@gmail.com</p>
          <p><strong>Social:</strong><br>
          🔗 <a href="https://linkedin.com/in/anconagraziana" target="_blank" style="color:#5B7B55;">LinkedIn</a><br>
          📸 <a href="https://www.instagram.com/nutri_su_insta/" target="_blank" style="color:#5B7B55;">Instagram</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card" style="text-align:center; margin-bottom:1rem;">
          <h3>💬 Scrivimi subito</h3>
          <p>Scegli il canale che preferisci e ti risponderò al più presto.</p>
          <div style="margin-top:1rem;">
            <a class="btn-mail" href="{MAIL_URL}">✉️ Scrivimi via email</a>
            <a class="btn-wa" href="{WA_URL}" target="_blank">💬 Scrivimi su WhatsApp</a>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2830.54132679946!2d10.311615611314664!3d44.810535470950065!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47806b8f8ab09825%3A0xa381d4de6169890f!2sRigenesis!5e0!3m2!1sit!2sit!4v1783455655720!5m2!1sit!2sit" width="100%" height="300" style="border:0;border-radius:16px;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


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

st.markdown(f"""
<div class="footer">
  <h4>Dott.ssa Graziana Ancona</h4>
  <div class="footer-rule"></div>
  <p>Biologa Nutrizionista — Parma</p>
  <p>Centro Rigenesis · Viale La Grola 5/B · 43125 Parma</p>
  <p>📞 320 3190704 · ✉️ <a href="mailto:anconagraziana@gmail.com">anconagraziana@gmail.com</a></p>
  <p>Sabato su appuntamento · Online su appuntamento</p>
  <p class="footer-social">
    <a href="{IG_URL}" target="_blank">Instagram</a> ·
    <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a> ·
    <a href="{WA_URL}" target="_blank">WhatsApp</a>
  </p>
  <p style="margin-top:0.8rem; font-size:0.8rem; opacity:0.6;">© {datetime.now().year} — P.IVA 03425440736</p>
</div>
""", unsafe_allow_html=True)
