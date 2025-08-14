import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_data.csv")

columns = ["Total Population", "Median Household Income"]
column = st.selectbox("Data:", columns)

state = st.selectbox("State:", df["State"].unique())

# Create a graph of total population
df_state = df[df["State"] == state]
population_fig = px.line(
    df_state, x="Year", y="Total Population", title=f"Total Population of {state}"
)

# Create a graph of Median Household Income
df_state = df[df["State"] == state]

graph_tab, table_tab = st.tabs(["Graph", "Table"])
with graph_tab:
    income_fig = px.line(
        df_state, x="Year", y="Median Household Income", title=f"Median Household Income of {state}"
    )

    if column == 'Total Population':
        st.header("🏃 Changes in US State Demographics Over Time")
        st.plotly_chart(population_fig)
    else:
        st.header("💸 Median Household Income")
        st.plotly_chart(income_fig)

with table_tab:
    st.write("All Data")
    st.dataframe(df)


