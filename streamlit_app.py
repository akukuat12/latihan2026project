import streamlit as st

st.title("🎈 HIDUP JOKOWI")
import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)
import streamlit as st

@st.fragment
def fragment_function():
    if st.button("Hi!"):
        st.write("SAYA AKAN LAWAN!")

fragment_function()
