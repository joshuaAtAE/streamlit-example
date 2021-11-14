from collections import namedtuple
from datetime import datetime
import altair as alt
import math
import pandas as pd
import streamlit as st
from pytz import timezone

ny_time_zone = timezone("America/NewYork")

f"What time is it?"
f"{datetime.now().strftime('%H:%M')}"
f"What time is it in New York?"
f"Huh?"
f"What time is it in New York?"
f"{datetime.now(ny_time_zone).strftime('%H:%M')}"

