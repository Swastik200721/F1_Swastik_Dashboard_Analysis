
import streamlit as st
import streamlit.components.v1 as components

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="F1 Race Intelligence",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- KEEP YOUR EXISTING LINKS ----------------
DASHBOARD_PAGE = (
    "https://public.tableau.com/app/profile/swastik.tare/"
    "viz/F1RaceIntelligence/F1DashBoard?publish=yes"
)

STORY_PAGE = (
    "https://public.tableau.com/app/profile/swastik.tare/"
    "viz/F1Story_17931756631930/Story1?publish=yes"
)

DASHBOARD_URL = (
    "https://public.tableau.com/views/F1RaceIntelligence/F1DashBoard"
    "?:showVizHome=no&:embed=true&:toolbar=yes"
)

STORY_URL = (
    "https://public.tableau.com/views/F1Story_17931756631930/Story1"
    "?:showVizHome=no&:embed=true&:toolbar=yes"
)

# ---------------- RETRO RACING THEME ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;700;800;900&family=IBM+Plex+Mono:wght@400;600;700&display=swap');

:root {
    --red: #e1262f;
    --cream: #f3ead7;
    --black: #171717;
    --yellow: #f5d547;
}

.stApp {
    background-color: var(--cream);
    color: var(--black);
    font-family: 'IBM Plex Mono', monospace;
}

header[data-testid="stHeader"] {
    background: var(--cream);
}

.block-container {
    max-width: 1350px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* Subtle racing-car pattern throughout the background */
.stApp::before {
    content: "🏎️     🏁       🏎️       🏎️     🏁";
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
    opacity: 0.07;
    font-size: 42px;
    line-height: 2.8;
    word-spacing: 22px;
    white-space: normal;
}

/* Keep page content above the decoration */
[data-testid="stAppViewContainer"] > .main {
    position: relative;
    z-index: 1;
}

.topbar {
    background: var(--black);
    color: var(--yellow);
    padding: 12px 18px;
    font-size: 11px;
    letter-spacing: 2px;
    border-bottom: 4px solid var(--red);
}

.brand {
    padding: 24px 0;
    border-bottom: 2px solid var(--black);
    display: flex;
    align-items: center;
    gap: 15px;
}

.brand-icon {
    font-size: 43px;
}

.brand-title {
    font: 900 27px 'Barlow Condensed', sans-serif;
    letter-spacing: 2px;
}

.brand-subtitle {
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 4px;
}

.hero {
    background: var(--black);
    color: var(--cream);
    padding: 45px 30px;
    margin-top: 22px;
    border-bottom: 8px solid var(--red);
}

.hero-label {
    color: var(--yellow);
    font-size: 11px;
    letter-spacing: 3px;
}

.hero h1 {
    font: 900 clamp(55px, 9vw, 105px)/0.95 'Barlow Condensed', sans-serif;
    margin: 20px 0;
    color: var(--cream);
}

.hero h1 span {
    color: var(--red);
}

.hero p {
    color: #ded7ca;
    line-height: 1.8;
    max-width: 680px;
    font-size: 13px;
}

.section-title {
    margin: 42px 0 15px;
    padding-left: 14px;
    border-left: 6px solid var(--red);
}

.section-title small {
    color: #70695d;
    letter-spacing: 2px;
    font-size: 10px;
}

.section-title h2 {
    font: 800 clamp(30px, 5vw, 48px) 'Barlow Condensed', sans-serif;
    margin: 4px 0;
}

.info-card {
    background: rgba(243, 234, 215, 0.94);
    border: 1px solid #b9ad98;
    border-top: 4px solid var(--red);
    padding: 18px;
    min-height: 95px;
}

div.stButton > button,
div.stLinkButton > a {
    background: var(--red);
    color: white;
    border: 2px solid var(--black);
    border-radius: 0;
    font: 700 12px 'IBM Plex Mono', monospace;
    padding: 12px 18px;
}

div.stButton > button:hover,
div.stLinkButton > a:hover {
    background: var(--yellow);
    color: var(--black);
    border-color: var(--black);
}

.tableau-link {
    background: #e8ddc7;
    padding: 14px;
    border-left: 4px solid var(--red);
    overflow-wrap: anywhere;
    font-size: 12px;
    line-height: 1.8;
}

.tableau-link a {
    color: #a3131b !important;
    text-decoration: underline !important;
}

.footer {
    margin-top: 40px;
    background: var(--black);
    color: var(--cream);
    padding: 28px;
    text-align: center;
    border-top: 7px solid var(--red);
}

.footer h2 {
    color: var(--yellow);
    font: 900 clamp(35px, 7vw, 65px) 'Barlow Condensed', sans-serif;
}

hr {
    border-color: #b9ad98;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="topbar">
    🏁 F1 RACE INTELLIGENCE
    &nbsp; | &nbsp; RETRO MOTORSPORT ARCHIVE
    &nbsp; | &nbsp; EST. RACING SPIRIT
</div>

<div class="brand">
    <div class="brand-icon">🏎️</div>
    <div>
        <div class="brand-title">F1 RACE INTELLIGENCE</div>
        <div class="brand-subtitle">
            THE GRAND PRIX DATA ARCHIVE
        </div>
    </div>
</div>

<div class="hero">
    <div class="hero-label">SPEED • STRATEGY • STATISTICS</div>
    <h1>BACK TO<br><span>THE GRID.</span></h1>
    <p>
        Explore the world of Formula 1 through driver performance,
        team results, race strategy and championship data.
        A classic racing look meets interactive data storytelling.
    </p>
    <div class="hero-label">🏁 START YOUR ENGINES — VOL. 01 🏁</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PROJECT INTRO ----------------
st.markdown("""
<div class="section-title">
    <small>01 / THE MISSION</small>
    <h2>MORE THAN JUST SPEED.</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "Discover the numbers behind the noise. Use the interactive "
    "Tableau dashboard and story to explore drivers, constructors, "
    "race outcomes and the data that shapes Formula 1."
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        '<div class="info-card">🏎️ <b>DRIVERS</b><br>'
        '<small>Points & performance</small></div>',
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        '<div class="info-card">🏆 <b>TEAMS</b><br>'
        '<small>Constructor results</small></div>',
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        '<div class="info-card">📊 <b>STRATEGY</b><br>'
        '<small>Race trends & outcomes</small></div>',
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        '<div class="info-card">🏁 <b>RACE DATA</b><br>'
        '<small>History & reliability</small></div>',
        unsafe_allow_html=True,
    )

# ---------------- DASHBOARD ----------------
st.markdown("""
<div class="section-title">
    <small>02 / THE CONTROL ROOM</small>
    <h2>RACE DASHBOARD.</h2>
</div>
""", unsafe_allow_html=True)

st.caption("🏎️ INTERACTIVE TABLEAU PUBLIC DASHBOARD")

components.iframe(
    DASHBOARD_URL,
    height=760,
    scrolling=True,
)

st.markdown(
    f'<div class="tableau-link">'
    f'<b>🏁 DASHBOARD LINK</b><br>'
    f'<a href="{DASHBOARD_PAGE}" target="_blank">'
    f'{DASHBOARD_PAGE}</a></div>',
    unsafe_allow_html=True,
)

st.link_button("OPEN FULL DASHBOARD ↗", DASHBOARD_PAGE)

# ---------------- STORY ----------------
st.markdown("---")

st.markdown("""
<div class="section-title">
    <small>03 / BEYOND THE NUMBERS</small>
    <h2>EVERY RACE HAS A STORY.</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "Explore the bigger picture through the Tableau Story. "
    "Move beyond individual charts and discover the patterns "
    "and comparisons within the racing data."
)

st.caption("🏁 INTERACTIVE TABLEAU STORY")

components.iframe(
    STORY_URL,
    height=760,
    scrolling=True,
)

st.markdown(
    f'<div class="tableau-link">'
    f'<b>📖 STORY LINK</b><br>'
    f'<a href="{STORY_PAGE}" target="_blank">'
    f'{STORY_PAGE}</a></div>',
    unsafe_allow_html=True,
)

st.link_button("OPEN FULL TABLEAU STORY ↗", STORY_PAGE)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div>🏎️ END OF TRANSMISSION 🏁</div>
    <h2>DATA NEVER LIFTS.</h2>
    <div>INDEPENDENT STUDENT PROJECT • TABLEAU PUBLIC</div>
</div>
""", unsafe_allow_html=True)
