import pandas as pd
import plotly.express as px
url = "https://raw.githubusercontent.com/owid/covid-19- data/master/public/data/latest/owid-covid-latest.csv"
df = pd.read_csv(url)
df = df[df['continent'].notna()]
df = df[['iso_code', 'location', 'total_cases', 'total_deaths', 'population']]
fig = px.choropleth(df,locations='iso_code', color='total_cases', hover_name='location',hover_data=['total_cases', 'total_deaths', 'population'], color_continuous_scale='Reds',title='COVID-19 Total Cases Worldwide')
fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.show()
