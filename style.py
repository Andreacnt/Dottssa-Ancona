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
  overflow-x: clip;
}
.btn-prenota:active, .btn-wa:active, .btn-review:active, .ig-btn:active,
a[data-testid="stTopNavLink"]:active { transform: scale(0.94); }

div[data-testid="stMainBlockContainer"] {
  max-width: 1080px; margin-left: auto; margin-right: auto; padding-top: 5.5rem !important;
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

a, a:hover, a:active, a:visited { text-decoration: none; }

.page-wrap { padding: var(--sp-4) var(--sp-2); }

.kicker {
  display: inline-block;
  font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 700;
  color: var(--forest); text-transform: uppercase; letter-spacing: 2px;
  background: var(--sage-pale); border-radius: var(--radius-pill);
  padding: 6px 16px; margin-bottom: 0.8rem;
}

@keyframes rise {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: none; }
}

.card, .post, .svc, .ig-box { animation: rise 0.55s ease both; }

section[data-testid="stSidebar"] { background: var(--forest); }
section[data-testid="stSidebar"] * { color: white; }
[data-testid="stSidebarNavItems"] a { padding: 10px 16px; border-radius: 12px; margin: 2px 0; }
[data-testid="stSidebarNavItems"] a[aria-current="page"] { background: rgba(255,255,255,0.15); border-left: 3px solid white; }

header[data-testid="stHeader"] {
  background: rgba(255,255,255,0.96); backdrop-filter: blur(10px);
  border-bottom: 3px solid var(--sage);
  box-shadow: 0 2px 12px rgba(61,90,61,0.08);
  min-height: 80px;
}
a[data-testid="stTopNavLink"] { text-decoration: none; padding: 8px 14px; }
a[data-testid="stTopNavLink"] span:not([data-testid="stIconMaterial"]) {
  font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.85rem;
  text-transform: uppercase; letter-spacing: 1.5px; color: var(--ink);
}
a[data-testid="stTopNavLink"]:hover span:not([data-testid="stIconMaterial"]) { color: var(--sage); }
a[data-testid="stTopNavLink"][aria-current="page"] { border-bottom: 2px solid var(--accent); }
a[data-testid="stTopNavLink"][aria-current="page"] span:not([data-testid="stIconMaterial"]) { color: var(--forest); }
@media (min-width: 769px) {
  div:has(> div > div[data-testid="stTopNavLinkContainer"]) {
    margin-left: auto;
    margin-right: auto;
  }
}

a[data-testid="stLogoLink"] img { height: 68px !important; width: auto; object-fit: contain; }

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
  background: linear-gradient(135deg, #F6FAF2, #EFF4E6); border-radius: 12px; padding: 0.85rem 1rem; margin: 0.4rem 0;
  border-top: 3px solid var(--sage); box-shadow: var(--shadow-sm);
  font-family: 'Inter', sans-serif; font-size: 0.92rem; color: var(--ink);
  min-height: 104px; display: flex; flex-direction: column;
  align-items: center; justify-content: center; text-align: center;
}
.svc small { color: var(--muted); font-size: 0.8rem; }

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

.ig-btn, .btn-prenota, .btn-wa, .btn-review { transition: transform 0.2s ease, filter 0.2s ease; }
.ig-btn:hover, .btn-prenota:hover, .btn-wa:hover, .btn-review:hover { transform: translateY(-2px); filter: brightness(0.96); }
.btn-prenota, .btn-wa, .btn-review {
  display: inline-block; font-family: 'Inter', sans-serif; font-weight: 700;
  padding: 13px 34px; border-radius: var(--radius-pill); text-decoration: none; font-size: 1rem; margin: 0.3rem;
}
.btn-review { background: #F7ECD4; color: #4A3A1A; border: 2px solid var(--accent); }
.btn-prenota { background: #C9F2E6; color: #0B4B3F; }
.btn-wa { background: #DCF8C6; color: #1F2C34; }

img[src*="profilo.jpg"] { border-radius: 50% !important; aspect-ratio: 1 !important; object-fit: cover !important; object-position: top center !important; border: 4px solid var(--sage) !important; }

details[data-testid="stExpander"] > summary { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: var(--forest); background: #EFF4E6; border-radius: 12px; }

.banner-img { display: block; width: 100%; height: 320px; object-fit: cover; border-radius: 18px; box-shadow: var(--shadow-md); }
.banner-home { display: block; width: 100%; height: auto; border-radius: 18px; box-shadow: var(--shadow-md); }
.img-credit { text-align: center; font-size: 0.75rem; color: var(--muted); margin-top: 0.4rem; }

.sep { text-align: center; color: var(--sage); opacity: 0.65; font-size: 1.15rem; margin: 1.2rem 0; }

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
  div[data-testid="stMainBlockContainer"] { padding-left: 0.8rem; padding-right: 0.8rem; border-radius: 0 0 20px 20px; }
  [data-testid="stColumn"] { min-width: 100% !important; flex: 1 1 100% !important; }
  .banner-img { height: 200px; }

  .page-wrap { padding: 1.2rem 0.4rem; }
  h1 { font-size: 1.7rem; }
  h2 { font-size: 1.35rem; }
}
</style>
"""
