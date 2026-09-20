import streamlit as st
from datetime import datetime

import content as C
from style import CUSTOM_CSS

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Biologa Nutrizionista",
    page_icon="img/logo.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def cta_box(titolo, testo):
    st.markdown(f"""
    <div class="cta">
      <h2>{titolo}</h2>
      <p>{testo}</p>
      <a href="{C.WA_URL}" target="_blank" class="btn-light">Prenota una visita</a>
    </div>
    """, unsafe_allow_html=True)


def pagina_home():
    st.markdown(f"""
    <div class="hero">
      <img class="hero-bg" src="{C.SFONDO_URL}" alt="">
      <div class="hero-veil"></div>
      <div class="hero-inner">
        <div class="over">{C.HERO_OVER}</div>
        <h1>{C.HERO_NOME}</h1>
        <div class="sub">{C.HERO_SUB}</div>
        <a href="{C.WA_URL}" target="_blank" class="btn-light">Prenota una visita</a>
        <div class="hero-social">
          <a href="{C.IG_URL}" target="_blank">Instagram</a>
          <a href="{C.LINKEDIN_URL}" target="_blank">LinkedIn</a>
          <a href="{C.MAIL_URL}">Email</a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Chi sono</div>', unsafe_allow_html=True)

    col_foto, col_testo = st.columns([1, 2.2])
    with col_foto:
        st.image(C.PROFILO_URL, width=250)
    with col_testo:
        st.markdown(f"{C.HOME_TITOLO}\n{C.HOME_INTRO}")

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Di cosa mi occupo</div>', unsafe_allow_html=True)
    st.markdown("### Aree di intervento")

    cols = st.columns(4)
    for i, (icona, titolo, _) in enumerate(C.servizi_card):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
              <div class="card-icon">{icona}</div>
              <h3>{titolo}</h3>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; margin:1.6rem 0; font-family:'Inter',sans-serif; color:#636E72;">
      📍 <strong style="color:#2D3436;">Consulenze in presenza:</strong> {C.SEDE_GIORNI} presso {C.SEDE_NOME}, {C.SEDE_INDIRIZZO}<br>
      💻 <strong style="color:#2D3436;">Consulenze online:</strong> {C.SEDE_ONLINE}
    </div>
    """, unsafe_allow_html=True)

    cta_box(*C.CTA_HOME)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_chisono():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Chi sono</div>', unsafe_allow_html=True)
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

    cta_box(*C.CTA_CHISONO)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_servizi():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Servizi</div>', unsafe_allow_html=True)
    st.title("Di cosa mi occupo")
    st.markdown(C.SERVIZI_INTRO)

    cols = st.columns(2)
    for i, (icona, titolo, dettaglio) in enumerate(C.servizi_card):
        with cols[i % 2]:
            extra = f"<br><small>{dettaglio}</small>" if dettaglio else ""
            st.markdown(f'<div class="svc">{icona} <strong>{titolo}</strong>{extra}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sep">✦ ✦ ✦</div>', unsafe_allow_html=True)
    st.markdown("### Il percorso in 4 passi")

    cols = st.columns(4)
    for i, (titolo, desc) in enumerate(C.passi):
        with cols[i]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
              <div class="step-n" style="margin:0 auto 0.8rem;">{i + 1}</div>
              <h3>{titolo}</h3>
              <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    cta_box(*C.CTA_SERVIZI)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_percorso():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Percorso</div>', unsafe_allow_html=True)
    st.title("Il percorso nutrizionale")
    st.markdown(C.PERCORSO_TITOLO)
    st.markdown(C.PERCORSO_HTML, unsafe_allow_html=True)

    cta_box(*C.CTA_PERCORSO)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_approccio():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Approccio</div>', unsafe_allow_html=True)
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

    cta_box(*C.CTA_APPROCCIO)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_blog():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Blog</div>', unsafe_allow_html=True)
    st.title("Mini Guide dal Blog")
    st.markdown(C.BLOG_SOTTOTITOLO)

    if not C.mini_guide:
        st.info("Aggiungi i tuoi post nella lista `mini_guide` in content.py per farli apparire qui.")
    else:
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
      <div style="font-size:2rem; margin-bottom:0.4rem;">📸</div>
      <h3>Seguimi su Instagram</h3>
      <p style="color:#636E72; margin-bottom:1.2rem;">{C.IG_HANDLE} — consigli e approfondimenti</p>
      <a class="ig-btn" href="{C.IG_URL}" target="_blank">Seguimi su Instagram</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def pagina_contatti():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">Contatti</div>', unsafe_allow_html=True)
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
        <div class="card" style="margin-bottom:1rem;">
          <h3>🕐 Orari</h3>
          <p>{C.SEDE_GIORNI.capitalize()}</p>
        </div>
        <div class="card">
          <h3>📞 Contattami</h3>
          <p><strong>Cell:</strong> {C.CELL}<br>
          <strong>Email:</strong> {C.EMAIL}</p>
          <p><strong>Social:</strong><br>
          🔗 <a href="{C.LINKEDIN_URL}" target="_blank" style="color:#5B7B55;">LinkedIn</a><br>
          📸 <a href="{C.IG_URL}" target="_blank" style="color:#5B7B55;">Instagram</a></p>
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
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(C.MAPS_EMBED, unsafe_allow_html=True)

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
  <h4>{C.HERO_NOME}</h4>
  <div class="footer-rule"></div>
  <p>Biologa Nutrizionista — Parma</p>
  <p>{C.SEDE_NOME} · {C.SEDE_INDIRIZZO}</p>
  <p>📞 {C.CELL} · ✉️ <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
  <p>{C.SEDE_GIORNI.capitalize()} · Online {C.SEDE_ONLINE}</p>
  <p class="footer-social">
    <a href="{C.IG_URL}" target="_blank">Instagram</a> ·
    <a href="{C.LINKEDIN_URL}" target="_blank">LinkedIn</a> ·
    <a href="{C.WA_URL}" target="_blank">WhatsApp</a>
  </p>
  <p style="margin-top:0.8rem; font-size:0.8rem; opacity:0.6;">© {datetime.now().year} — P.IVA {C.P_IVA}</p>
</div>
""", unsafe_allow_html=True)
