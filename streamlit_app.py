import streamlit as st
from itertools import cycle
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Traffic Light Simulator", layout="centered")
st.title("🚦 Traffic Light Simulator")

lights = [
    ("Green", 4),
    ("Yellow", 2),
    ("Red", 4)
]

if "lights_cycle" not in st.session_state:
    st.session_state.lights_cycle = cycle(lights)
    st.session_state.color, st.session_state.cycles_left = next(st.session_state.lights_cycle)

# Use st_autorefresh instead of experimental_autorefresh
count = st_autorefresh(interval=1000, key="traffic_refresh")

if st.session_state.cycles_left > 0:
    st.session_state.cycles_left -= 1
else:
    st.session_state.color, st.session_state.cycles_left = next(st.session_state.lights_cycle)

color = st.session_state.color

# (The rest of your display logic ...)
