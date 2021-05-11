import folium

#list of the places to visit
bucket_list = {
    1: [19.0760, 72.8777],
    2: [35.9078, 127.7669]
}
# create a map
map = folium.Map(style="OpenStreetMap")

# create a marker
for i in range(1,3):
    folium.Marker(location=bucket_list[i],popup=f"my {i} location").add_to(map)

map.save("map.html")
