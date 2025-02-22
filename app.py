import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

col1 , col2, col3 = st.columns([5,5,20])

with col3:
    st.title("Streamlit Demo")

year_col, continent_col, log_x_col = st.columns([5,5,5])

with year_col:
    year_choice = st.slider(
        "Year",
        min_value = 1952,
        max_value = 2007,
        step = 5,
        value = 2007
    )
with continent_col:
    continent_choice = st.selectbox(
        "Continent",
        ("All", "Asia", "Europa","Africa", "Americas", "Oceania")
    )
with log_x_col:
    log_x_choice = st.checkbox("Log X axis?")

df = px.data.gapminder()

filtered_df = df[df.year == year_choice]

if continent_choice != "All":
    filtered_df = filtered_df[filtered_df.continent == continent_choice]

fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x = log_x_choice,
    size_max=80,
)

fig.update_layout(title = "GDP per Capita vs. Life Expectancy")
st.plotly_chart(fig, use_container_width=True)
