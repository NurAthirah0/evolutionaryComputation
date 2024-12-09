import streamlit as st

# Sidebar inputs for genetic algorithm parameters
st.sidebar.header("Genetic Algorithm Parameters")
CO_R = st.sidebar.slider("Crossover Rate", min_value=0.0, max_value=0.95, value=0.8, step=0.01)
MUT_R = st.sidebar.slider("Mutation Rate", min_value=0.01, max_value=0.05, value=0.2, step=0.01)
GEN = st.sidebar.number_input("Generations", min_value=10, max_value=500, value=100, step=10)
POP = st.sidebar.number_input("Population Size", min_value=10, max_value=200, value=50, step=10)
EL_S = st.sidebar.number_input("Elitism Size", min_value=1, max_value=10, value=2, step=1)

# Display parameters
st.write("### Genetic Algorithm Parameters")
st.write(f"Crossover Rate: {CO_R}")
st.write(f"Mutation Rate: {MUT_R}")
st.write(f"Generations: {GEN}")
st.write(f"Population Size: {POP}")
st.write(f"Elitism Size: {EL_S}")
