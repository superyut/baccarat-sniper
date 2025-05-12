import streamlit as st
from pattern_memory_engine import check_pattern_memory
from support_resistance import detect_support_resistance
from signal_engine import generate_simple_bet_signal

st.set_page_config(page_title="The Secret Edge", layout="centered")

st.markdown(
    """
    <style>
        body { background-color: #0d0d0d; color: #f2f2f2; }
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        .stButton button {
            background-color: #1f1f1f;
            color: gold;
            border: 1px solid gold;
            border-radius: 10px;
            font-weight: bold;
            width: 100%;
            height: 3rem;
        }
        .stButton button:hover {
            background-color: gold;
            color: black;
        }
        .signal-box {
            background-color: #111;
            color: white;
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            font-size: 1.3rem;
            border: 2px solid gold;
        }
        .signal-green {
            color: #00FF00;
            font-weight: bold;
        }
        .signal-red {
            color: red;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("THE SECRET EDGE")
st.markdown("#### The Baccarat System Casinos Fear")

if "results" not in st.session_state:
    st.session_state.results = []

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Player"):
        st.session_state.results.append("P")
with col2:
    if st.button("Banker"):
        st.session_state.results.append("B")
with col3:
    if st.button("Undo") and st.session_state.results:
        st.session_state.results.pop()

# Calculate momentum
momentum = []
value = 0
for r in st.session_state.results:
    value += 1 if r == "P" else -1
    momentum.append(value)

# Detect patterns
pattern_hit = check_pattern_memory(st.session_state.results)

# Detect support and resistance
highs, lows = detect_support_resistance(momentum)

# Signal logic
signal = generate_simple_bet_signal(st.session_state.results, momentum, highs, lows)

# Display chart
st.subheader("Momentum Chart")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(momentum, marker="o", linestyle="-", color="gold")
ax.axhline(0, color="gray", linestyle="--")
ax.set_ylabel("Momentum")
ax.set_xlabel("Hand #")
ax.grid(True)
for i, val in highs:
    ax.plot(i, val, "ro")
for i, val in lows:
    ax.plot(i, val, "go")
st.pyplot(fig)

# Result history
st.subheader("Result History")
st.code(" → ".join(st.session_state.results), language="text")

# Signal display box
st.markdown(f'<div class="signal-box">SIGNAL: <span class="{ "signal-green" if "BET" in signal else "signal-red" }">{signal}</span></div>', unsafe_allow_html=True)

# Pattern match reminder
if pattern_hit is not None:
    st.markdown(f"<br/><i>Pattern matched from hand #{pattern_hit + 1}</i>", unsafe_allow_html=True)