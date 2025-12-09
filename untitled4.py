import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page configuration
st.set_page_config(page_title="Simply Supported Beam Calculator", layout="wide")

st.title("Simply Supported Beam Calculator")
st.write("Uniformly Distributed Load (UDL)")

# Sidebar inputs
unit_system = st.sidebar.radio("Unit System", ["Metric (SI)", "Imperial"])

if unit_system == "Metric (SI)":
    L_label = "Beam length L (m)"
    w_label = "Load intensity w (kN/m)"
else:
    L_label = "Beam length L (ft)"
    w_label = "Load intensity w (lb/ft)"

L = st.sidebar.number_input(L_label, min_value=0.1, value=5.0)
w = st.sidebar.number_input(w_label, min_value=0.1, value=1.0)

# Calculations
R = w * L / 2
Mmax = w * L**2 / 8
x_vals = np.linspace(0, L, 200)
M_vals = w * x_vals * (L - x_vals) / 2
V_vals = w * (L/2 - x_vals)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Maximum Moment")
    st.metric("M_max", f"{Mmax:.3f}")

with col2:
    st.subheader("Reaction at Supports")
    st.metric("Reaction (each)", f"{R:.3f}")

# Moment Plot
st.subheader("Bending Moment Diagram")
fig1, ax1 = plt.subplots()
ax1.plot(x_vals, M_vals)
ax1.set_xlabel("Position x")
ax1.set_ylabel("Moment M(x)")
st.pyplot(fig1)

# Data Table
df = pd.DataFrame({
    "x": x_vals,
    "Moment M(x)": M_vals,
    "Shear V(x)": V_vals
})

st.subheader("Values Table")
st.dataframe(df)

# Instructions
with st.expander("How to use this calculator"):
    st.markdown("""
    **How to Use**
    - Select your preferred unit system
    - Enter the beam length (L)
    - Enter the uniformly distributed load intensity (w)
    - Review the calculated results, diagrams, and table

    **Assumptions**
    - Linear elastic behavior  
    - Small deflections  
    - Homogeneous material  
    - Simply supported ends  
    """)
