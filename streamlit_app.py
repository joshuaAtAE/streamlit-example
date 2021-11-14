from collections import namedtuple
from datetime import datetime
import altair as alt
import math
import pandas as pd
import streamlit as st
from pytz import timezone

ny_time_zone = timezone("America/New_York")

f"What time is it?"
f"{datetime.now().strftime('%h:%M')}"
f"What time is it in New York?"
f"Huh?"
f"What time is it in New York?"
time_in_new_york =  datetime.now(ny_time_zone)
f"{time_in_new_york.strftime('%h:%M')}"
"At night?"
hour = int(time_in_new_york.strftime('%H'))
if (hour < 4) or (hour > 17):
    "Yes."
else:
    "No."

