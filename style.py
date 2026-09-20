# FOGLIO DI STILE — qui si cambiano colori, font, card e layout.
# I testi vivono in content.py: non serve toccarli.

CUSTOM_CSS = """
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
"""
