import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = pd.read_csv("sales_data.csv")

st.title("📊 Sales Analytics Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

# KPI Metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales}")
col2.metric("Total Profit", f"${total_profit}")
col3.metric("Orders", total_orders)

# Revenue by Category
fig1 = px.bar(
    filtered_df,
    x="Category",
    y="Sales",
    color="Category",
    title="Sales by Category"
)

st.plotly_chart(fig1)

# Regional Sales
fig2 = px.pie(
    filtered_df,
    names="Region",
    values="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig2)

# Monthly Trend
fig3 = px.line(
    filtered_df,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3)