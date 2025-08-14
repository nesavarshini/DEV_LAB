import pandas as pd
import plotly.express as px
import geopandas as gpd
import folium
df_world = px.data.gapminder().query("year == 2007")
fig_world = px.choropleth(df_world,locations="iso_alpha", color="gdpPercap", hover_name="country",color_continuous_scale=px.colors.sequential.Plasma,title = "World GDP per Capita (2007)")
fig_world.show()
india_states = gpd.read_file("https://raw.githubusercontent.com/datameet/maps/master/States/Admi  n2/india_states.geojson")
india_states["state_name"] = india_states["STATE"]
state_data = pd.DataFrame({'state_name': ['Tamil Nadu', 'Maharashtra', 'Karnataka', 'Kerala', 'Uttar Pradesh'], 'population': [75000000, 112000000, 65000000, 35000000, 200000000]})
merged_states = india_states.merge(state_data, on="state_name")
fig_states = px.choropleth(merged_states,geojson=merged_states.geometry, locations=merged_states.index, color="population", hover_name="state_name", title="IN Population by Indian States", projection="mercator")
fig_states.update_geos(fitbounds="locations", visible=False)

fig_states.show()
districts = gpd.read_file("https://raw.githubusercontent.com/datameet/maps/master/Districts/in  dia_districts.geojson")
m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)
folium.Choropleth(geo_data=districts, data=districts,columns=["DISTRICT", "DISTRICT"],key_on="feature.properties.DISTRICT", fill_color="YlGnBu",fill_opacity=0.7, line_opacity=0.2, legend_name="Districts of India").add_to(m)
m.save("india_districts.html")
print(" India District Map saved as: india_districts.html")
