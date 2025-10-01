import streamlit as st
from itertools import cycle

st.set_page_config(page_title="Traffic Light Simulator", layout="centered")

st.title("🚦 Traffic Light Simulator")

# Traffic light sequence (color, duration in refresh cycles)
lights = [
    ("Green", 4),   # 4 cycles
    ("Yellow", 2),  # 2 cycles
    ("Red", 4)      # 4 cycles
]

if "lights_cycle" not in st.session_state:
    st.session_state.lights_cycle = cycle(lights)
    st.session_state.color, st.session_state.cycles_left = next(st.session_state.lights_cycle)

# Auto-refresh every 1000 ms (1 sec)
count = st.experimental_autorefresh(interval=1000, key="traffic_refresh")

# Update cycle countdown
if st.session_state.cycles_left > 0:
    st.session_state.cycles_left -= 1
else:
    st.session_state.color, st.session_state.cycles_left = next(st.session_state.lights_cycle)

color = st.session_state.color

# Display traffic light
st.markdown(
    f"""
    <div style="text-align:center;">
        <div style="width:80px; height:80px; background-color:{'green' if color=='Green' else '#555'}; border-radius:50%; margin:5px auto;"></div>
        <div style="width:80px; height:80px; background-color:{'yellow' if color=='Yellow' else '#555'}; border-radius:50%; margin:5px auto;"></div>
        <div style="width:80px; height:80px; background-color:{'red' if color=='Red' else '#555'}; border-radius:50%; margin:5px auto;"></div>
    </div>
    """,  # 👈 properly closed
    unsafe_allow_html=True
)

# Road simulation
if color == "Green":
    traffic = "🚗 🏍️ 🚙 🚕 → moving"
    people = "🚶 🚶‍♀️ (waiting)"
elif color == "Yellow":
    traffic = "🚗 🏍️ slowing..."
    people = "🚶 🚶‍♀️ (waiting)"
else:  # Red
    traffic = "🚗 🚙 🚕 🏍️ (stopped)"
    people = "🚶 🚶‍♀️ 🚶 🚶‍♂️ crossing →"

# Display road and pedestrians
st.markdown(
    f"""
    <div style="text-align:center; font-size:30px; margin-top:20px;">
        <div><b>Road:</b> {traffic}</div>
        <div style="margin-top:20px;"><b>Pedestrians:</b> {people}</div>
    </div>
    """,  # 👈 also properly closed
    unsafe_allow_html=True
)
