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
f"What time is it?"
f"{datetime.now(ny_time_zone).strftime('%-I:%M')}"
f"What time is it in New York?"
f"Huh?"
f"What time is it in New York?"
time_in_new_york =  datetime.now(ny_time_zone)
f"{time_in_new_york.strftime('%-I:%M')}"
"At night?"
hour = int(time_in_new_york.strftime('%H'))
if (hour < 4) or (hour > 17):
    "Yes."
else:
    "No."

