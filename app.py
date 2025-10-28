
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

DATA_DIR = Path(".")
@st.cache_data
def load():
    logs = pd.read_csv(DATA_DIR / "well_logs.csv")
    prod = pd.read_csv(DATA_DIR / "production_timeseries.csv")
    wells = pd.read_csv(DATA_DIR / "wells_meta.csv")
    return logs, prod, wells

logs, prod, wells = load()

st.title("Reservoir Characterization & Decline Analysis — Demo")
well = st.sidebar.selectbox("Choose a well", ["All"] + sorted(wells["Well_ID"].unique().tolist()))
if well != "All":
    st.subheader(f"Production - {well}")
    p = prod[prod["Well_ID"] == well].copy()
    p["Date"] = pd.to_datetime(p["Date"])
    fig = px.line(p, x="Date", y="Oil_bopd", title=f"Oil Rate for {well}")
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Log snippets (top 50 rows)")
    st.dataframe(logs[logs["Well_ID"]==well].head(50))
else:
    st.subheader("Field production summary")
    summary = prod.groupby("Date")[["Oil_bopd","Water_bwpd"]].sum().reset_index()
    summary["Date"] = pd.to_datetime(summary["Date"])
    fig = px.line(summary, x="Date", y="Oil_bopd", title="Field total oil rate")
    st.plotly_chart(fig, use_container_width=True)
