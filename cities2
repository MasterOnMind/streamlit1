import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

# A dictionary to hold the data for the 10 largest US cities by population.
# The salary data is a simplified representation based on publicly available
# information, meant for demonstration purposes.
cities_data = {
    'New York': {'lat': 40.7128, 'lon': -74.0060, 'salary': 90000},
    'Los Angeles': {'lat': 34.0522, 'lon': -118.2437, 'salary': 85000},
    'Chicago': {'lat': 41.8781, 'lon': -87.6298, 'salary': 75000},
    'Houston': {'lat': 29.7604, 'lon': -95.3698, 'salary': 68000},
    'Phoenix': {'lat': 33.4484, 'lon': -112.0740, 'salary': 65000},
    'Philadelphia': {'lat': 39.9526, 'lon': -75.1652, 'salary': 69000},
    'San Antonio': {'lat': 29.4241, 'lon': -98.4936, 'salary': 60000},
    'San Diego': {'lat': 32.7157, 'lon': -117.1611, 'salary': 82000},
    'Dallas': {'lat': 32.7767, 'lon': -96.7970, 'salary': 72000},
    'San Jose': {'lat': 37.3382, 'lon': -121.8863, 'salary': 105000}
}

# Create a DataFrame from the city data
df = pd.DataFrame.from_dict(cities_data, orient='index')
df.index.name = 'city'
df.reset_index(inplace=True)

# Normalize the salary data to a 0-255 scale for color mapping
df['norm_salary'] = 255 * (df['salary'] - df['salary'].min()) / (df['salary'].max() - df['salary'].min())

st.title('U.S. City Salary Map')
st.subheader('Exploring Average Salaries in the 10 Largest Cities')
st.write("This map displays the relative average salary for the 10 largest U.S. cities. The color of each point corresponds to the average salary, with a darker red indicating a higher salary.")

# Use st.selectbox to allow the user to select a city to zoom in on
selected_city = st.selectbox(
    'Choose a city to center the map on:',
    df['city'].tolist(),
    index=df.index[df['city'] == 'New York'].tolist()[0]
)

# Get the latitude and longitude of the selected city
center_lat = df[df['city'] == selected_city]['lat'].values[0]
center_lon = df[df['city'] == selected_city]['lon'].values[0]
zoom_level = 9

# Create a pydeck scatterplot layer
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=['lon', 'lat'],
    get_radius=10000,
    get_fill_color='[norm_salary, 0, 0, 160]', # Use normalized salary for red intensity
    pickable=True,
    auto_highlight=True,
)

# Set the view state for the map, centered on the selected city
view_state = pdk.ViewState(
    latitude=center_lat,
    longitude=center_lon,
    zoom=zoom_level,
    pitch=50,
)

# Create the pydeck chart and display it in Streamlit
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[layer],
    tooltip={"text": "City: {city}\nAvg. Salary: ${salary:,}"}
))

st.markdown("""
<style>
.stSelectbox div[role="button"] {
    background-color: #f0f2f6;
    border-radius: 8px;
    padding: 10px;
}
.stSelectbox div[role="button"]:hover {
    border-color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)
