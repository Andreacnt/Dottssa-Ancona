import streamlit as st

st.markdown("# 👩‍⚕️ Chi Sono")
st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("foto.jpg", width=200)
with col2:
    st.markdown(
        """
        ### Dott.ssa Graziana Ancona
        **Biologa Nutrizionista** | Iscritta all'Ordine dei Biologi n. PuB_A5285
        **Ordine dei Biologi della Puglia e della Basilicata**

        Laureata in Scienze della Nutrizione con specializzazione in
        **Nutrizione Collettiva e Sicurezza Alimentare**.

        ### 📋 Cosa offro:
        - Piani alimentari personalizzati
        - Educazione alimentare
        - Esame bioimpedenziometrico
        - Plicometria e circonferenze corporee
        - Supporto nel raggiungimento dei tuoi obiettivi
        """
    )

st.markdown("---")
st.markdown("## 📍 Dove Trovarmi")

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        ### Studio
        📪 Viale la Grola, 5 - Parma
        📞 320 319 0704
        ✉️ anconagraziana@gmail.com

        **Orari:**
        - Sabato mattina (solo su appuntamento)
        """
    )
with col2:
    st.markdown(
        """
        ### Social
        - 📸 Instagram: @nutri_su_insta
        - 🔗 LinkedIn: /in/anconagraziana
        """
    )

st.markdown("### 🗺️ Mappa")
st.markdown("Sostituisci il placeholder con l'indirizzo del tuo studio:")
st.code(
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!..." width="100%" height="300" style="border:0;" allowfullscreen></iframe>',
    language="html",
)
st.info("Vai su maps.google.com, cerca il tuo indirizzo, clicca 'Condividi' → 'Incorpora una mappa' e copia il codice qui sopra.")
