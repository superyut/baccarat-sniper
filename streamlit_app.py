import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Baccarat Sniper", layout="centered")
st.title("Baccarat Momentum Tracker")

# Store results
if "results" not in st.session_state:
    st.session_state.results = []

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Player"):
        st.session_state.results.append("P")
with col2:
    if st.button("Banker"):
        st.session_state.results.append("B")
with col3:
    if st.button("Undo"):
        if st.session_state.results:
            st.session_state.results.pop()

# Calculate momentum
momentum = []
value = 0
for r in st.session_state.results:
    value += 1 if r == "P" else -1
    momentum.append(value)

# Plot chart
st.subheader("Momentum Chart")
fig, ax = plt.subplots()
ax.plot(momentum, marker="o", linestyle="-", linewidth=2, color="royalblue")
ax.axhline(0, color="gray", linestyle="--")
ax.set_ylabel("Momentum (+1 P / –1 B)")
ax.set_xlabel("Hand Number")
ax.grid(True)
st.pyplot(fig)

# Show raw history
st.subheader("Result History")
st.write(" → ".join(st.session_state.results))
