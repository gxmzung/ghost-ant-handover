import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Ghost Ant Handover",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background: #07111c;
    color: #f4f7fb;
}

.block-container {
    padding-top: 1.2rem;
    padding-left: 1rem;
    padding-right: 1rem;
    max-width: 100%;
}

.card {
    background: linear-gradient(180deg, #0d1b2a 0%, #08131f 100%);
    border: 1px solid rgba(160, 190, 220, 0.28);
    border-radius: 14px;
    padding: 22px;
    height: 100%;
    box-shadow: 0 0 18px rgba(0,0,0,0.25);
}

.big-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 0;
    color: #ffffff;
}

.sub-title {
    font-size: 24px;
    font-weight: 700;
    color: #48a7ff;
    margin-top: 8px;
}

.card-title {
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 12px;
    color: #ffffff;
}

.text {
    font-size: 16px;
    line-height: 1.55;
    color: #e8eef7;
}

.metric-green {
    color: #75ff6a;
    font-weight: 800;
}

.metric-red {
    color: #ff5e57;
    font-weight: 800;
}

.metric-yellow {
    color: #ffd84d;
    font-weight: 800;
}

.stDataFrame {
    border-radius: 12px;
}

img {
    border-radius: 8px;
}

code {
    color: #7CFF6B !important;
}
</style>
""", unsafe_allow_html=True)

results = Path("results")

def image_card(title, filename):
    st.markdown(f'<div class="card"><div class="card-title">{title}</div>', unsafe_allow_html=True)
    path = results / filename
    if path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.warning(f"Missing: {path}")
    st.markdown('</div>', unsafe_allow_html=True)


top1, top2, top3 = st.columns([1.0, 1.2, 1.2])

with top1:
    st.markdown("""
    <div class="card">
        <div class="big-title">Ghost Ant Handover</div>
        <div class="sub-title">UAM Communication Handover Framework</div>
        <br>
        <div class="text">
        A predictive handover framework for UAM communication using Ghost Ant algorithm,
        3D pheromone map, and adaptive decision-making.
        </div>
        <br>
        <div class="text">🔵 Reward-based cell evaluation</div>
        <div class="text">🟢 Adaptive handover</div>
        <div class="text">🟠 3D pheromone map</div>
        <div class="text">🟣 Predictive Ghost Ant</div>
        <div class="text">🔴 UAM trajectory simulation</div>
    </div>
    """, unsafe_allow_html=True)

with top2:
    image_card("UAM Trajectory and Base Stations", "uam_trajectory.png")

with top3:
    image_card("UAM Simulation Animation", "uam_animation.gif")

mid1, mid2, mid3 = st.columns([1.0, 1.2, 1.0])

with mid1:
    image_card("3D Pheromone Heatmap", "pheromone_map.png")

with mid2:
    st.markdown('<div class="card"><div class="card-title">Simulation Log</div>', unsafe_allow_html=True)
    csv_path = results / "uam_simulation_log.csv"
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        st.dataframe(df, use_container_width=True, height=300)
    else:
        st.warning("Missing simulation log")
    st.markdown('</div>', unsafe_allow_html=True)

with mid3:
    st.markdown('<div class="card"><div class="card-title">Simulation Report</div>', unsafe_allow_html=True)
    report_path = results / "uam_simulation_report.md"
    if report_path.exists():
        st.markdown(report_path.read_text())
    else:
        st.warning("Missing report")
    st.markdown('</div>', unsafe_allow_html=True)

bot1, bot2, bot3 = st.columns([1.0, 1.2, 1.0])

with bot1:
    st.markdown('<div class="card"><div class="card-title">Comparison Summary</div>', unsafe_allow_html=True)
    summary_path = results / "comparison_summary.md"
    if summary_path.exists():
        st.markdown(summary_path.read_text())
    else:
        st.warning("Missing comparison summary")
    st.markdown('</div>', unsafe_allow_html=True)

with bot2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Terminal Output</div>
        <pre style="color:#73ff5c; font-size:15px;">
$ ./run_all.sh
======================================
 Ghost Ant Handover Full Pipeline
======================================
[1/5] Running reward demo...       ✓
[2/5] Running handover demo...     ✓
[3/5] Running UAM simulation...    ✓
[4/5] Generating report...         ✓
[5/5] Generating animation...      ✓

Pipeline completed.
Check results/ directory.
        </pre>
    </div>
    """, unsafe_allow_html=True)

with bot3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Results Directory</div>
        <div class="text">📄 uam_simulation_log.csv</div>
        <div class="text">🖼️ uam_trajectory.png</div>
        <div class="text">🎞️ uam_animation.gif</div>
        <div class="text">📝 uam_simulation_report.md</div>
        <div class="text">📊 comparison_summary.md</div>
    </div>
    """, unsafe_allow_html=True)
