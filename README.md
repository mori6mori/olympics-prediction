# Olympic Maniac

"Olympic Maniac" is an interactive platform for Olympic enthusiasts to engage with a comprehensive dataset spanning over the past 120 years. The platform features dynamic filtering, a Folium map, and an ML predictor that estimates YOUR chance of winning Olympic medals.

## Motivation

The project aims to provide a robust and interactive tool for exploring historical Olympic data, understanding trends, and making predictions. It offers users the ability to delve into the rich history of the Olympics and gain insights into country performances over time.

## Build Status

![Build Status](https://travis-ci.org/yourusername/olympic-maniac.svg?branch=master)
![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/yourusername/olympic-maniac?branch=master&svg=true)

## Code Style

This project adheres to the PEP 8 code style guidelines.

## Screenshots

<img width="488" alt="Screenshot 2024-07-14 at 6 20 26 PM" src="https://github.com/user-attachments/assets/60d3226e-ab13-46fe-b0f4-7fe615096929">



## Tech/Framework Used

Built with:
- Python
- Pandas
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Folium

## Features

- Data collection and cleaning with standardized country names using NOC codes
- Dynamic filtering capabilities for ‘Country Name’ using the Streamlit framework
- Geospatial visualization with Folium and GeoJSON data
- Machine learning model to predict medal counts

## Challenges

1. **Data Collection and Cleaning**:
    - Handling missing values
    - Standardizing country names using NOC codes
    - Ensuring consistent formatting across different time periods
2. **Dynamic Filtering and Interactivity**:
    - Integrated dynamic filtering capabilities for ‘Country Name’ using Streamlit
    - Enhanced filtering with the `streamlit_dynamic_filters` library
3. **Geospatial Visualization**:
    - Created an interactive choropleth map with Folium
    - Utilized GeoJSON data for accurate country boundaries
4. **Performance Optimization**:
    - Ensured smooth application performance with large datasets and complex visualizations
    - Optimized data processing and visualization performance with efficient libraries

## Findings

1. **Top Performing Countries**:
    - Highlighted the top countries (USA, Russia, China) with the most accumulated Olympic medals over the years
2. **Medal Trends Over Time**:
    - Observed trends correlating with economic growth and sports infrastructure investment
3. **Geospatial Insights**:
    - Geographical patterns in medal distributions with clusters of high-performing countries
4. **Interactive Exploration**:
    - Personalized insights through detailed filtering of medal counts by user interests



