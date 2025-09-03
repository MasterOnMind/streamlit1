# This script creates an interactive, animated choropleth map using Plotly Express.
# It visualizes various metrics from the Gapminder dataset over time.

import pandas as pd
import plotly.express as px

# Import data from GitHub
try:
    data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    # Exit if data cannot be loaded to prevent script failure
    exit()

# Create an animated choropleth map using Plotly Express.
# The `animation_frame` parameter automatically generates an animation slider.
# The `animation_group` ensures that the same countries are tracked across frames.
fig = px.choropleth(
    data, 
    locations='iso_alpha', 
    color='gdpPercap', 
    hover_name='country',
    animation_frame='year', 
    animation_group='country',
    color_continuous_scale=px.colors.sequential.Plasma,
    projection='natural earth', 
    title='<br>GDP per Capita by Country (1952-2007)',
    labels={'gdpPercap': 'GDP per Capita ($)'},
)

# Customize the layout for a cleaner look
fig.update_layout(
    title_font_size=24,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth'
    )
)

# Show the interactive figure. The animation controls will be part of the output.
fig.show()

# To view the animation, run this script in an environment that supports interactive Plotly figures,
# such as a Jupyter Notebook or a local server.
