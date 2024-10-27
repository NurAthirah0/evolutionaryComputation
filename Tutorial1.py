import streamlit as st
st.set_page_config(
    page_title="Genetic Algorithm"
)

st.header("Genetic Algorithm", divider="gray")

import random

#POP_SIZE: Number of Chromosomes in our list.
POP_SIZE = 500

#TARGET: Our goal.
TARGET = st.text_input("Enter your name")

#GENES: Options from which our population would be created.
GENES = ' abcdefghijklmnopqrstuvwxyz'

#MUT_RATE: Rate at which our string will be changed.
MUT_RATE = st.number_input("Enter your mutation rate")

