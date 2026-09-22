# FOGLIO DI STILE — qui si cambiano colori, font, card e layout.
# I testi vivono in content.py: non serve toccarli.

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  /* Palette unica: solo salvia/foresta + un accento caldo per le CTA */
  --forest: #3D5A3D;
  --sage: #5B7B55;
  --sage-light: #8A9A5B;
  --sage-pale: #E8EEE3;
  --cream: #F4F7F0;
  --ink: #2D3436;
  --muted: #636E72;
  --accent: #C9A15A;      /* oro/senape tenue, sostituisce il teal per bottoni "caldi" */
  --accent-dark: #A9843F;
  --wa-green: #25D366;    /* eccezione consentita: colore ufficiale WhatsApp */

  /* Scala ombre unica */
  --shadow-sm: 0 2px 12px rgba(61,90,61,0.08);
  --shadow-md: 0 8px 24px rgba(61,90,61,0.12);
  --shadow-lg: 0 16px 40px rgba(61,90,61,0.16);

  /* Raggi coerenti */
  --radius-card: 16px;
  --radius-pill: 999px;

  /* Scala spaziature */
  --sp-1: 0.5rem;
  --sp-2: 1rem;
  --sp-3: 1.5rem;
  --sp-4: 2rem;
  --sp-5: 3rem;
}

.stApp {
  background-color: #E7EEE1;
  background-image: radial-gradient(rgba(91,123,85,0.10) 1.2px, transparent 1.2px);
  background-size: 22px 22px;
}

.main > .block-container {
  max-width: 1080px; padding-top: 0 !important;
  background: rgba(255,255,255,0.62);
  border-radius: 0 0 28px 28px;
  padding-left: 2rem; padding-right: 2rem; padding-bottom: 2rem;
  box-shadow: 0 10px 40px rgba(61,90,61,0.10);
}

h1, h2, h3 { font-family: 'Playfair Display', serif; color: var(--forest); }
h1 { font-size: 2.2rem; }
h2 { font-size: 1.6rem; }
h3 { font-size: 1.25rem; }

p, li, .stMarkdown { font-family: 'Inter', sans-serif; color: var(--ink); line-height: 1.7; }

.page-wrap { padding: var(--sp-4) var(--sp-2); }

.kicker {
  display: inline-block;
  font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 700;
  color: var(--forest); text-transform: uppercase; letter-spacing: 2px;
  background: var(--sage-pale); border-radius: var(--radius-pill);
  padding: 6px 16px; margin-bottom: 0.8rem;
}

/* Animazioni: classi esplicite invece di nth-child, così l'ordine non si rompe
   se cambia la struttura HTML. Applica .delay-1, .delay-2 ecc. agli elementi. */
@keyframes rise {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: none; }
}
.rise { animation: rise 0.6s ease both; }
.delay-1 { animation-delay: 0.08s; }
.delay-2 { animation-delay: 0.16s; }
.delay-3 { animation-delay: 0.24s; }
.delay-4 { animation-delay: 0.32s; }
.delay-5 { animation-delay: 0.40s; }

.card, .post, .svc, .cta, .ig-box { animation: rise 0.55s ease both; }

section[data-testid="stSidebar"] { background: var(--forest); }
section[data-testid="stSidebar"] * { color: white; }
[data-testid="stSidebarNavItems"] a { padding: 10px 16px; border-radius: 12px; margin: 2px 0; }
[data-testid="stSidebarNavItems"] a[data-testid="stSidebarNavItemActive"] { background: rgba(255,255,255,0.15); border-left: 3px solid white; }

header[data-testid="stHeader"] {
  background: rgba(233,240,227,0.94); backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(91,123,85,0.28);
  box-shadow: 0 2px 12px rgba(61,90,61,0.08);
  min-height: 74px;
}
header[data-testid="stHeader"] nav a {
  font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.95rem;
  color: var(--forest); border-radius: var(--radius-pill); padding: 8px 16px;
}
header[data-testid="stHeader"] nav a:hover { background: var(--sage-pale); }
header[data-testid="stHeader"] nav a[aria-current="page"] { background: var(--forest); color: white; }

[data-testid="stLogo"] img { max-height: 62px !important; width: auto; object-fit: contain; }

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
.hero-inner { position: relative; z-index: 2; padding: var(--sp-5) var(--sp-3); max-width: 820px; }
.hero-inner .over { font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 300; letter-spacing: 3px; text-transform: uppercase; color: rgba(255,255,255,0.85); }
.hero-inner h1 { font-size: 3.2rem; color: white; margin: 0.4rem 0; line-height: 1.15; }
.hero-inner .sub { font-family: 'Playfair Display', serif; font-size: 1.5rem; color: white; margin-bottom: var(--sp-4); }
.btn-light {
  display: inline-block; background: white; color: var(--forest); font-family: 'Inter', sans-serif;
  font-weight: 700; padding: 14px 44px; border-radius: var(--radius-pill); text-decoration: none; font-size: 1.05rem;
  box-shadow: var(--shadow-lg);
}
.hero-social { margin-top: var(--sp-4); }
.hero-social a { color: rgba(255,255,255,0.8); text-decoration: none; font-size: 1.05rem; margin: 0 0.7rem; font-family: 'Inter', sans-serif; }

.card {
  background: #F6FAF2; border-radius: var(--radius-card); padding: 1.6rem;
  box-shadow: var(--shadow-sm); border: 1px solid rgba(91,123,85,0.16); height: 100%;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover, .post:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.card-icon {
  display: inline-flex; align-items: center; justify-content: center;
  width: 54px; height: 54px; border-radius: 50%;
  background: var(--sage-pale); font-size: 1.6rem; margin-bottom: 0.6rem;
}
.card h3 { margin-bottom: 0.4rem; }
.card p { font-size: 0.95rem; color: var(--muted); }

.svc {
  background: linear-gradient(135deg, #F6FAF2, #EFF4E6); border-radius: var(--radius-card); padding: 1.4rem 1.2rem; margin: 0.5rem 0;
  border-top: 4px solid var(--sage); box-shadow: var(--shadow-sm);
  font-family: 'Inter', sans-serif; color: var(--ink);
  min-height: 122px; display: flex; flex-direction: column;
  align-items: center; justify-content: center; text-align: center;
}
.svc small { color: var(--muted); }

.cta {
  background: linear-gradient(135deg, var(--forest), var(--sage) 55%, var(--sage-light));
  border-radius: var(--radius-card); padding: var(--sp-5) var(--sp-4); text-align: center; margin: 2.2rem 0;
}
.cta h2 { color: white; font-size: 1.8rem; margin-bottom: 0.6rem; }
.cta p { color: rgba(255,255,255,0.9); max-width: 620px; margin: 0 auto 1.6rem; font-size: 1.05rem; }

.step-n {
  display: inline-flex; align-items: center; justify-content: center;
  width: 42px; height: 42px; border-radius: 50%;
  background: linear-gradient(135deg, var(--sage), var(--sage-light));
  color: white; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 1.15rem;
}

.post {
  background: #F6FAF2; border-radius: var(--radius-card); box-shadow: var(--shadow-sm);
  border: 1px solid rgba(91,123,85,0.16); height: 100%;
  display: flex; flex-direction: column;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.post-body { padding: 1.4rem; flex: 1; display: flex; flex-direction: column; }
.post-body h3 { font-size: 1.1rem; margin-bottom: 0.4rem; }
.post-body p { font-size: 0.9rem; color: var(--muted); flex: 1; }
.post-link { color: var(--sage); font-weight: 700; text-decoration: none; font-size: 0.92rem; font-family: 'Inter', sans-serif; margin-top: 0.8rem; }

.ig-box {
  background: linear-gradient(135deg, #F6FAF2, #EAF1E2); border-radius: var(--radius-card); padding: 2.2rem 1.5rem;
  box-shadow: var(--shadow-sm); border: 1px solid rgba(91,123,85,0.16);
  margin: var(--sp-4) 0; text-align: center;
}
.ig-btn {
  display: inline-block; background: linear-gradient(135deg, var(--sage), var(--sage-light)); color: white;
  font-family: 'Inter', sans-serif; font-weight: 700; padding: 13px 38px;
  border-radius: var(--radius-pill); text-decoration: none; font-size: 1rem;
}

.btn-light, .ig-btn, .btn-prenota, .btn-wa { transition: transform 0.2s ease, filter 0.2s ease; }
.btn-light:hover, .ig-btn:hover, .btn-prenota:hover, .btn-wa:hover { transform: translateY(-2px); filter: brightness(1.06); }
.btn-prenota, .btn-wa {
  display: inline-block; font-family: 'Inter', sans-serif; font-weight: 700;
  padding: 13px 34px; border-radius: var(--radius-pill); text-decoration: none; font-size: 1rem; margin: 0.3rem;
}
/* "Prenota" ora usa l'accento caldo della palette: coerente col brand,
   ma comunque distinto dai bottoni verdi secondari */
.btn-prenota { background: var(--accent); color: #4A3A1A; }
.btn-prenota:hover { background: var(--accent-dark); color: white; }
.btn-wa { background: var(--wa-green); color: white; }

img[src*="profilo.jpg"] { border-radius: 50% !important; aspect-ratio: 1 !important; object-fit: cover !important; object-position: top center !important; border: 4px solid var(--sage) !important; }

.streamlit-expanderHeader { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: var(--forest); background: #EFF4E6; border-radius: 12px; }

[data-testid="stImage"] img { border-radius: 18px; box-shadow: var(--shadow-md); }

.sep { text-align: center; color: var(--sage); opacity: 0.65; font-size: 1.15rem; margin: 1.2rem 0; }

.hero-cta { font-size: 1.1rem; padding: 15px 46px; }

.footer {
  background: var(--forest); text-align: center; padding: var(--sp-5) var(--sp-3);
  width: 100vw; margin-left: calc(-50vw + 50%); margin-top: var(--sp-5);
}
.footer h4 { font-family: 'Playfair Display', serif; color: white; font-size: 1.3rem; margin-bottom: 0.4rem; }
.footer p { color: rgba(255,255,255,0.78); font-size: 0.95rem; margin: 0.25rem 0; }
.footer a { color: var(--sage-light); text-decoration: none; }
.footer-rule { width: 44px; height: 2px; background: var(--sage-light); margin: 1rem auto; opacity: 0.6; }
.footer-social a { font-size: 1.05rem; margin: 0 0.6rem; }

@media (max-width: 768px) {
  .main > .block-container { padding-left: 0.8rem; padding-right: 0.8rem; border-radius: 0 0 20px 20px; }

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
"""
