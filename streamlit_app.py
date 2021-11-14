from collections import namedtuple
from datetime import datetime
import altair as alt
import math
import pandas as pd
import streamlit as st
from pytz import timezone

xanadu_zone = timezone("America/New_York")
ny_time_zone = timezone("America/New_York")

st.header("Time in Xanadu and New York")
st.image("Pasted Graphic 14.png")
f"Q: What time is it?"
st.image("Pasted Graphic 12.png")
f"A: {datetime.now(ny_time_zone).strftime('%-I:%M')}"
f"Q: What time is it in New York?"
f"A: Huh?"
f"Q: What time is it in New York?"
time_in_new_york =  datetime.now(ny_time_zone)
f"A: {time_in_new_york.strftime('%-I:%M')}"
"Q: At night?"
hour = int(time_in_new_york.strftime('%H'))
st.image("Pasted Graphic 17.png")
if (hour < 4) or (hour > 17):
    "Q: Yes."
else:
    "A: No."

