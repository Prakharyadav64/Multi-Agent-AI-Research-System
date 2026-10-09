
import streamlit as st
from pipeline import run_research_pipeline

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Research Studio",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
/* Main page */
.stApp {
    background:
        radial-gradient(ellipse at 50% 0%, #10213b 0%, transparent 55%),
        linear-gradient(135deg, #050914, #080b16 60%, #101020);
    color: #edf3ff;
}

.stApp > header {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
    position: relative;
    z-index: 2;
}

/* Animated space background */
.space-bg {
    position: fixed;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
    background-image:
        radial-gradient(2px 2px at 15% 25%, #ffffffaa 50%, transparent 100%),
        radial-gradient(1px 1px at 75% 18%, #a9d7ffcc 50%, transparent 100%),
        radial-gradient(2px 2px at 45% 75%, #ffffff99 50%, transparent 100%),
        radial-gradient(1px 1px at 85% 65%, #8dbaffcc 50%, transparent 100%),
        radial-gradient(1px 1px at 25% 85%, #ffffff99 50%, transparent 100%);
    background-size: 240px 240px, 310px 310px,
                     270px 270px, 360px 360px, 200px 200px;
    animation: starDrift 100s linear infinite;
}

.space-bg::before,
.space-bg::after {
    content: "";
    position: absolute;
    width: min(65vw, 700px);
    aspect-ratio: 1;
    border: 1px solid #4c8cff22;
    border-radius: 50%;
    left: 50%;
    top: 45%;
    transform: translate(-50%, -50%);
}

.space-bg::before {
    box-shadow:
        0 0 80px #2563eb0b,
        inset 0 0 70px #2563eb0b;
    animation: orbitSpin 80s linear infinite;
}

.space-bg::after {
    width: min(82vw, 900px);
    border-color: #38bdf822;
    animation: orbitSpin 120s linear infinite reverse;
}

/* Orbiting planets */
.planet {
    position: absolute;
    border-radius: 50%;
    will-change: transform;
}

.planet-blue {
    width: 18px;
    height: 18px;
    left: calc(50% + min(32vw, 340px));
    top: 44%;
    background: radial-gradient(circle at 30% 30%,
        #d4f5ff, #38bdf8 35%, #1d4ed8 75%, #090d25);
    box-shadow: 0 0 22px #38bdf877;
    animation: blueOrbit 24s linear infinite;
}

.planet-purple {
    width: 12px;
    height: 12px;
    left: calc(50% - min(36vw, 380px));
    top: 45%;
    background: radial-gradient(circle at 30% 30%,
        #f5d0fe, #a855f7 50%, #4c1d95);
    box-shadow: 0 0 20px #a855f766;
    animation: purpleOrbit 32s linear infinite;
}

.planet-ringed {
    width: 28px;
    height: 28px;
    left: calc(50% + min(40vw, 440px));
    top: 20%;
    background: radial-gradient(circle at 30% 30%,
        #fde68a, #d97706 60%, #713f12);
    box-shadow: 0 0 28px #f59e0b44;
}

.planet-ringed::after {
    content: "";
    position: absolute;
    width: 48px;
    height: 13px;
    left: -10px;
    top: 7px;
    border: 2px solid #fbbf8077;
    border-radius: 50%;
    transform: rotate(-25deg);
}

@keyframes starDrift {
    from { background-position: 0 0, 0 0, 0 0, 0 0, 0 0; }
    to   { background-position: 240px 180px, -310px 200px,
                           270px -270px, -360px 360px, 200px -200px; }
}

@keyframes orbitSpin {
    from { rotate: 0deg; }
    to   { rotate: 360deg; }
}

@keyframes blueOrbit {
    0%   { transform: translate(0, 0); }
    25%  { transform: translate(-100px, 80px); }
    50%  { transform: translate(-280px, 10px); }
    75%  { transform: translate(-100px, -80px); }
    100% { transform: translate(0, 0); }
}

@keyframes purpleOrbit {
    0%   { transform: translate(0, 0); }
    25%  { transform: translate(120px, -65px); }
    50%  { transform: translate(300px, 20px); }
    75%  { transform: translate(120px, 85px); }
    100% { transform: translate(0, 0); }
}

/* Glass-style report header */
.hero {
    padding: 1.8rem;
    border-radius: 18px;
    border: 1px solid #7da8ff30;
    background: linear-gradient(135deg,
        #101c30bb, #11142699);
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 40px #00000020;
    margin-bottom: 1.5rem;
}

.hero h1 {
    margin-bottom: 0.4rem;
    background: linear-gradient(90deg, #ffffff, #93c5fd, #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.muted {
    color: #b8c5dc;
}

/* Keep app content above background */
[data-testid="stAppViewContainer"],
[data-testid="stSidebar"] {
    background: transparent;
}

@media (prefers-reduced-motion: reduce) {
    .space-bg, .planet, .space-bg::before,
    .space-bg::after {
        animation: none !important;
    }
}
</style>
""", unsafe_allow_html=True)



# ---------------- SOLAR SYSTEM BACKGROUND ----------------

st.markdown("""
<div class="space-bg">
    <div class="planet planet-blue"></div>
    <div class="planet planet-purple"></div>
    <div class="planet planet-ringed"></div>
</div>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.title("🔎 Research Studio")
    st.caption("Multi-agent research system")

    st.divider()

    st.markdown("### How it works")
    st.markdown("""
    1. **Search Agent** — finds web sources
    2. **Reader Agent** — scrapes relevant content
    3. **Writer Chain** — creates the report
    4. **Critic Chain** — reviews the report
    """)

    st.divider()

    if st.button("Clear current results", use_container_width=True):
        st.session_state.research_result = None
        st.session_state.research_topic = ""
        st.rerun()

    st.caption("Powered by LangChain, Groq, Tavily and Streamlit.")

# ---------------- MAIN HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>AI Research Studio</h1>
    <p class="muted">
        Research any topic using specialized AI agents.
        Generate reports, inspect evidence, and review AI feedback.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- RESEARCH INPUT ----------------

st.subheader("What do you want to research?")

with st.form("research_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Latest advances in multi-agent AI systems",
        help="Enter a clear topic for better search results.",
    )

    submitted = st.form_submit_button(
        "🚀 Start Research",
        type="primary",
        use_container_width=True,
    )

if submitted:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        st.session_state.research_result = None
        st.session_state.research_topic = topic.strip()

        try:
            with st.spinner(
                "Researching the web, reading sources, writing the report "
                "and reviewing the results..."
            ):
                result = run_research_pipeline(topic.strip())

            st.session_state.research_result = result
            st.success("Research completed successfully!")

        except Exception as exc:
            st.error(f"Research failed: {type(exc).__name__}: {exc}")
            st.info(
                "Check the terminal for the traceback and verify your API keys."
            )

# ---------------- DISPLAY RESULTS ----------------

result = st.session_state.research_result

if result:
    st.divider()

    st.subheader("Research Results")
    st.caption(f"Topic: {st.session_state.research_topic}")

    report = result.get("report", "")
    feedback = result.get("feedback", "")
    search_results = result.get("search_results", "")
    scraped_content = result.get("scraped_content", "")

    # Download report
    st.download_button(
        label="⬇️ Download Report",
        data=report,
        file_name="research_report.md",
        mime="text/markdown",
        use_container_width=False,
    )

    # Main result tabs
    report_tab, critic_tab, sources_tab = st.tabs([
        "📄 Research Report",
        "🧠 Critic Review",
        "🔗 Research Evidence",
    ])

    with report_tab:
        st.markdown(report if report else "No report was generated.")

    with critic_tab:
        st.markdown(feedback if feedback else "No critic feedback available.")

    with sources_tab:
        st.markdown("### Web Search Results")
        st.text(search_results or "No search results available.")

        st.divider()

        st.markdown("### Scraped Page Content")
        st.text(scraped_content or "No scraped content available.")

else:
    st.info(
        "Enter a topic above and start your first research run. "
        "Your report and review will appear here."
    )
