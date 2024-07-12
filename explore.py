import streamlit as st
import pandas as pd
import numpy as np
from streamlit_dynamic_filters import DynamicFilters
import folium
from streamlit_folium import folium_static
import json





def show_explore_page():
    st.title("Olympic Maniac")
    st.subheader('###Country Medal Progression by Year')
    def display_top_country(df):
    # Sum medals for each country over the years
        total = df.sum(axis=0)
        max_name = df.sum(axis=0).idxmax()
        # Display the country name and the total medals
        st.metric("Country with Most total Medals", max_name, f"{int(total[max_name])} Medals")

    def modify_df(df):
        df_melted = df.melt(id_vars='Country', var_name='Year', value_name='total_medal')
        # Convert 'Year' column to integer type
        df_melted['Year'] = df_melted['Year'].astype(int)
        # Pivot the DataFrame to wide format
        df_pivot = df_melted.pivot(index='Year', columns='Country', values='total_medal')
        return df_pivot
    # Load Dataframe
    df = pd.read_csv('/Users/mori/Desktop/Summer 2024/olympics-prediction/cumulative_medals.csv')

    col1, col2, col3 = st.columns(3)
    with col1:
        display_top_country(modify_df(df))

    dynamic_filters = DynamicFilters(df, filters=['Country'])
    dynamic_filters.display_filters()
    dynamic_filters.display_df()

    df_filtered = pd.DataFrame(dynamic_filters.filter_df())
    st.line_chart(modify_df(df_filtered))

    st.subheader('Wondering how GDP affects medal amounts?')
    total_df = pd.read_csv('/Users/mori/Desktop/Summer 2024/olympics-prediction/medal_by_country.csv')
    st.write(total_df)

    # Create a Folium map
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Load the GeoJSON data
    with open('/Users/mori/Desktop/Summer 2024/olympics-prediction/countries.geo.json') as f:
        geojson_data = json.load(f)

    # Create a dictionary of medal counts
    medal_dict = total_df.set_index('Country')['Total'].to_dict()

    # Add medal data to GeoJSON
    for feature in geojson_data['features']:
        country_name = feature['properties']['name']
        feature['properties']['Medal_Count'] = medal_dict.get(country_name, 0)

    # Save the modified GeoJSON
    with open('countries_with_medals.geojson', 'w') as f:
        json.dump(geojson_data, f)

    # Add GeoJSON to the map
    folium.Choropleth(
        geo_data=geojson_data,
        name='choropleth',
        data=total_df,
        columns=['Country', 'Total'],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Medal Count'
    ).add_to(m)

    st.title('Olympic Medal Counts by Country')
    # Display the map in Streamlit
    folium_static(m)


