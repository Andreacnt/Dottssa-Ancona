import streamlit as st

st.set_page_config(
    page_title="Dott.ssa Graziana Ancona - Nutrizionista",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="expanded",
)

with open("background.jpg", "rb") as f:
    bg_bytes = f.read()
import base64
bg_b64 = base64.b64encode(bg_bytes).decode()

st.markdown(
    f"""
<style>
.stApp {{
    background-image: url(data:image/png;base64,{bg_b64});
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
.block-container {{
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 20px;
    padding: 2rem 3rem;
    margin-top: 1rem;
}}
</style>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image("https://img.icons8.com/color/96/healthy-food--v1.png", width=80)
    st.markdown("### Dott.ssa Graziana Ancona")
    st.markdown("---")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/01_Chi_Sono.py", label="Chi Sono", icon="👩‍⚕️")
    st.page_link("pages/02_Richiedi_Appuntamento.py", label="Richiedi Appuntamento", icon="📅")
    st.page_link("pages/03_Mini_Guide.py", label="Mini Guide", icon="📖")

st.title("🥗 Benvenuto!")
st.subheader("Dott.ssa Graziana Ancona - Biologa Nutrizionista")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("foto.jpg", width=200)
with col2:
    st.markdown(
        """
        Ciao! Sono la **Dott.ssa Graziana Ancona**, biologa nutrizionista.

        Ti aiuto a raggiungere i tuoi obiettivi di salute e benessere
        attraverso un'alimentazione personalizzata e sostenibile.

        ### 📍 Cosa trovi qui:
        - **Chi Sono** - La mia storia e dove trovarmi
        - **Richiedi Appuntamento** - Prenota una consulenza
        - **Mini Guide** - Consigli e articoli sulla nutrizione
        """
    )

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        © 2026 Dott.ssa Graziana Ancona - Biologa Nutrizionista
    </div>
    """,
    unsafe_allow_html=True,
)
