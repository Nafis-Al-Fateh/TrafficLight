import streamlit as st
from itertools import cycle

st.set_page_config(page_title="Traffic Light Simulator", layout="centered")

st.title("🚦 Traffic Light Simulator")

# Traffic light sequence (color, duration ms)
lights = [
    ("Green", 2000),
    ("Yellow", 1000),
    ("Red", 2000)
]

if "lights_cycle" not in st.session_state:
    st.session_state.lights_cycle = cycle(lights)
    st.session_state.color, st.session_state.delay = next(st.session_state.lights_cycle)
    st.session_state.step = 0

# Cycle through lights
if st.session_state.step >= st.session_state.delay // 500:
    st.session_state.color, st.session_state.delay = next(st.session_state.lights_cycle)
    st.session_state.step = 0
else:
    st.session_state.step += 1

color = st.session_state.color

# Display traffic light
st.markdown(
    f"""
    <div style="text-align:center;">
        <div style="width:80px; height:80px; background-color:{'green' if color=='Green' else '#555'}; border-radius:50%; margin:5px auto;"></div>
        <div style="width:80px; height:80px; background-color:{'yellow' if color=='Yellow' else '#555'}; border-radius:50%; margin:5px auto;"></div>
        <div style="width:80px; height:80px; background-color:{'red' if color=='Red' else '#555'}; border-radius:50%; margin:5px auto;"></div>
    </div>
    """, unsafe_allow_html=True
)

# Road simulation
if color == "Green":
    traffic = "🚗 🏍️ 🚙 🚕 →"
    people = "🚶 🚶‍♀️ (waiting)"
elif color == "Yellow":
    traffic = "🚗 🏍️ (slowing)"
    people = "🚶 🚶‍♀️ (waiting)"
else:  # Red
    traffic = "🚗 🚙 🚕 🏍️ (stopped)"
    people = "🚶 🚶‍♀️ 🚶 🚶‍♂️ crossing →"

st.markdown(
    f"""
    <div style="text-align:center; font-size:30px; margin-top:20px;">
        <div>Road: {traffic}</div>
        <div style="margin-top:20px;">Pedestrians: {people}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Auto-refresh every 500ms
st.experimental_rerun() if st.session_state.step < st.session_state.delay // 500 else None
