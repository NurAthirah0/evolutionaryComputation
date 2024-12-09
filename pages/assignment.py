import streamlit as st

CO_R = st.number_input("Crossover Rate (range from 0.0 to 0.95)", min_value = 0.0, max_value = 0.95, 
                       value = 0.8, step= 0.01)

MUT_R = st.number_input("Mutation Rate (range from 0.01 to 0.05)", min_value = 0.01, max_value = 0.05,
                        value = 0.02, step = 0.01)
