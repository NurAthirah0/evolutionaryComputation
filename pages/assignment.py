import streamlit as st

with col1:
  input_crossover = st.text_input("Crossover Rate", "range from 0 to 0.95", label_visibility = st.session_state.visibility, disabled = st.session_state.disabled, placeholder = st.session_state.placeholder,)
input_mutation = st.text_input("Mutation Rate", "0.2")
