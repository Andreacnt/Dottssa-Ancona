import streamlit as st
from datetime import datetime
import urllib.request

import content as C
from style import CUSTOM_CSS

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Biologa Nutrizionista",
    page_icon="img/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.logo("img/logo-bar.png", size="large")

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def banner(url, credit, cls="banner-img"):
    credit_html = f'<p class="img-credit">{credit}</p>' if credit else ""
    st.markdown(f"""
    <div>
      <img class="{cls}" src="{url}" alt="">
      {credit_html}
    </div>
    """, unsafe_allow_html=True)


def pagina_home():
    banner(*C.IMG_HOME, cls="banner-home")
    st.title("Dott.ssa Graziana Ancona — Biologa Nutrizionista")
    st.markdown(C.HOME_INTRO)

    st.markdown(f"""
    📍 **Consulenze in presenza:** {C.SEDE_GIORNI} presso {C.SEDE_NOME}, {C.SEDE_INDIRIZZO}

    💻 **Consulenze online:** {C.SEDE_ONLINE}
    """)


def pagina_chisono():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.title("Chi Sono")

    col_foto, col_testo = st.columns([1, 2])
    with col_foto:
        st.image(C.PROFILO_URL, width=260)
    with col_testo:
        st.markdown(C.CHISONO_BIO)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🎓 Formazione"):
            st.markdown("\n".join(f"- {voce}" for voce in C.FORMAZIONE))
    with col_b:
        with st.expander("📜 Dati professionali"):
            st.markdown("\n".join(f"- {voce}" for voce in C.DATI_PROFESSIONALI))
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_servizi():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    banner(*C.IMG_SERVIZI, cls="banner-home")
    st.title("Di cosa mi occupo")
    st.markdown(C.SERVIZI_INTRO)

    cols = st.columns(2)
    for i, (icona, titolo, dettaglio) in enumerate(C.servizi_card):
        with cols[i % 2]:
            extra = f"<br><small>{dettaglio}</small>" if dettaglio else ""
            st.markdown(f'<div class="svc">{icona} <strong>{titolo}</strong>{extra}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def pagina_percorso():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    banner(*C.IMG_PERCORSO, cls="banner-home")
    st.title("Il percorso nutrizionale")
    st.markdown(C.PERCORSO_TITOLO)
    st.markdown(C.PERCORSO_HTML, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_approccio():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    banner(*C.IMG_APPROCCIO, cls="banner-home")
    st.title("Il mio approccio")

    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        st.markdown(C.APPROCCIO_TESTO)
    with col_b:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
          <div style="font-size:2.6rem; margin-bottom:0.4rem;">💚</div>
          <p style="font-style:italic; color:#636E72;">
          {C.APPROCCIO_QUOTE}
          </p>
          <p>{C.APPROCCIO_VALORI}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)
    st.markdown("### I pilastri del metodo")

    cols = st.columns(3)
    for i, (icona, titolo, desc) in enumerate(C.pilastri):
        with cols[i]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
              <div class="card-icon">{icona}</div>
              <h3>{titolo}</h3>
              <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


@st.cache_data(ttl=6 * 3600)
def ig_embed_ok():
    try:
        req = urllib.request.Request(C.IG_EMBED, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            if r.status != 200:
                return False
            xfo = (r.headers.get("X-Frame-Options") or "").upper()
            csp = (r.headers.get("Content-Security-Policy") or "").lower()
            if "DENY" in xfo or "SAMEORIGIN" in xfo:
                return False
            if "frame-ancestors" in csp:
                return False
            return True
    except Exception:
        return False


def pagina_blog():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.title("Mini Guide dal Blog")
    st.markdown(C.BLOG_SOTTOTITOLO)

    st.markdown(f"### {C.BLOG_FEED_TITOLO}")
    if ig_embed_ok():
        st.markdown(
            f'<iframe src="{C.IG_EMBED}" width="100%" height="620" '
            'frameborder="0" scrolling="yes" style="border:0; border-radius:16px; background:white;"></iframe>',
            unsafe_allow_html=True,
        )
    elif C.mini_guide:
        cols = st.columns(3)
        for i, (titolo, descrizione, url) in enumerate(C.mini_guide):
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
      <div style="margin-bottom:0.6rem;"><img src="{C.IG_LOGO}" width="44" alt="Instagram" onerror="this.style.display='none'"></div>
      <h3>{C.BLOG_FOLLOW_TITOLO}</h3>
      <p style="color:#636E72; margin-bottom:1.2rem;">{C.IG_HANDLE} — consigli e approfondimenti</p>
      <a class="ig-btn" href="{C.IG_URL}" target="_blank"><img src="{C.IG_LOGO_WHITE}" width="18" style="vertical-align:-3px; margin-right:6px;" onerror="this.style.display='none'">{C.BLOG_FOLLOW_BTN}</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_contatti():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    banner(*C.IMG_CONTATTI, cls="banner-home")
    st.title("Contatti")

    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown(f"""
        <div class="card" style="margin-bottom:1rem;">
          <h3>📍 Dove sono</h3>
          <p><strong>In presenza:</strong> {C.SEDE_NOME}<br>
          {C.SEDE_INDIRIZZO}<br>
          <a href="{C.MAPS_URL}" target="_blank" style="color:#5B7B55;">Apri su Google Maps →</a></p>
          <p><strong>Online:</strong> {C.SEDE_ONLINE}</p>
        </div>
        <div class="card">
          <h3>🕐 Orari</h3>
          <p>{C.SEDE_GIORNI.capitalize()}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card" style="text-align:center; margin-bottom:1rem;">
          <h3>{C.BOX_PRENOTAZIONI_TITOLO}</h3>
          <p>Scegli il canale che preferisci e ti risponderò al più presto.</p>
          <div style="margin-top:1rem;">
            <a class="btn-prenota" href="{C.PRENOTA_URL}" target="_blank"><img src="{C.MIODOTTORE_LOGO}" width="18" style="vertical-align:-3px; margin-right:6px; border-radius:4px;" onerror="this.style.display='none'">{C.PRENOTA_BTN}</a>
            <a class="btn-wa" href="{C.WA_URL}" target="_blank"><img src="{C.WHATSAPP_LOGO}" width="18" style="vertical-align:-3px; margin-right:6px;" onerror="this.style.display='none'">{C.WHATSAPP_BTN}</a>
            <br><a class="btn-review" href="{C.RECENSIONI_URL}" target="_blank">⭐ Lascia una recensione</a>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(C.MAPS_EMBED, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


page_home = st.Page(pagina_home, title="Home", icon=":material/home:", default=True)
page_chisono = st.Page(pagina_chisono, title="Chi Sono", icon=":material/person:")
page_servizi = st.Page(pagina_servizi, title="Di cosa mi occupo", icon=":material/spa:")
page_percorso = st.Page(pagina_percorso, title="Percorso", icon=":material/route:")
page_approccio = st.Page(pagina_approccio, title="Approccio", icon=":material/eco:")
page_blog = st.Page(pagina_blog, title="Blog", icon=":material/menu_book:")
page_contatti = st.Page(pagina_contatti, title="Contatti", icon=":material/mail:", url_path="contatti")

pg = st.navigation(
    [page_home, page_chisono, page_servizi, page_percorso, page_approccio, page_blog, page_contatti],
    position="top",
)
pg.run()

st.markdown(f"""
<div class="footer">
  <h4>{C.HERO_NOME}</h4>
  <div class="footer-rule"></div>
  <p>Biologa Nutrizionista — Parma</p>
  <p>{C.SEDE_NOME} · {C.SEDE_INDIRIZZO}</p>
  <p>📞 {C.CELL} · ✉️ <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
  <p class="footer-social">
    <a href="{C.IG_URL}" target="_blank">Instagram</a> ·
    <a href="{C.LINKEDIN_URL}" target="_blank">LinkedIn</a> ·
    <a href="{C.WA_URL}" target="_blank">WhatsApp</a> ·
    <a href="{C.PRENOTA_URL}" target="_blank">MioDottore</a>
  </p>
  <p style="margin-top:0.8rem; font-size:0.8rem; opacity:0.6;">© {datetime.now().year} — P.IVA {C.P_IVA}</p>
</div>
""", unsafe_allow_html=True)
