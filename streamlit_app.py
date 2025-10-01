import streamlit as st
import time
from itertools import cycle

# Page config
st.set_page_config(page_title="Traffic Light Simulator", layout="centered")

st.title("🚦 Traffic Light Simulator")

# Define traffic light sequence
lights = [
    ("Green", 2),
    ("Yellow", 0.5),
    ("Red", 2)
]

colors_cycle = cycle(lights)

# Placeholder for the traffic light display
placeholder = st.empty()

while True:
    color, delay = next(colors_cycle)
    
    # Display traffic light
    placeholder.markdown(
        f"""
        <div style="text-align:center;">
            <div style="width:80px; height:80px; background-color:{'green' if color=='Green' else '#555'}; border-radius:50%; margin:5px auto;"></div>
            <div style="width:80px; height:80px; background-color:{'yellow' if color=='Yellow' else '#555'}; border-radius:50%; margin:5px auto;"></div>
            <div style="width:80px; height:80px; background-color:{'red' if color=='Red' else '#555'}; border-radius:50%; margin:5px auto;"></div>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Wait for the specified duration
    time.sleep(delay)
