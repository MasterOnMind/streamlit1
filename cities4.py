import streamlit as st
import pydeck as pdk

# --- Data ---
cities = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Tokyo": {"lat": 35.6895, "lon": 139.6917},
    "Berlin": {"lat": 52.5200, "lon": 13.4050},
    "Sydney": {"lat": -33.8688, "lon": 151.2093},
    "Rio de Janeiro": {"lat": -22.9068, "lon": -43.1729},
    "Cairo": {"lat": 30.0444, "lon": 31.2357},
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
}

map_styles = {
    "Dark (Carto)": "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
    "Light (Carto)": "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
    "Voyager (Carto)": "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
    "Watercolor (Stamen)": "http://tile.stamen.com/watercolor/{z}/{x}/{y}.jpg",
    "Toner (Stamen)": "http://tile.stamen.com/toner/{z}/{x}/{y}.png",
}

st.set_page_config(layout="wide")
st.sidebar.header("⚙️ Controls")
city_choice = st.sidebar.selectbox("Choose a city", list(cities.keys()))
style_choice = st.sidebar.selectbox("Choose a map style", list(map_styles.keys()))
lat, lon = cities[city_choice]["lat"], cities[city_choice]["lon"]
chosen_style = map_styles[style_choice]

st.title("🌍 Geospatial Data Explorer")
st.write(f"🗺️ Showing map for: **{city_choice}** with style: **{style_choice}**")

view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=11, pitch=0, bearing=0)

if style_choice in ["Watercolor (Stamen)", "Toner (Stamen)"]:
    layers = [
        pdk.Layer(
            "BitmapLayer",
            data=None,
            image=chosen_style,
            bounds=[-180, -85, 180, 85]
        )
    ]
    map_chart = pdk.Deck(
        map_style=None,  # Use Streamlit's built-in base for raster overlays
        initial_view_state=view_state,
        layers=layers
    )
else:
    map_chart = pdk.Deck(
        map_style=chosen_style,
        initial_view_state=view_state,
        layers=[]
    )

st.pydeck_chart(map_chart)
