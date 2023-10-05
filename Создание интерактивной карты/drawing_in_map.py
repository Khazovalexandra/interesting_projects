import pandas as pd 
import folium
import requests
from folium.plugins import MiniMap
from folium.plugins import MousePosition
from folium.plugins import MeasureControl

state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()
state_data = pd.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)

wind_locations = [
    [15.15, -73.15],
    [13.766667, -70.25],
    [15.766667, -67.016667],
    [12.983333, -66.083333],
    [12.6, -61.25],
    [11.083333, -59.716667],
    [7.55, -54.9],
    [5.483333, -50.1],
    [3.566667, -46.133333],
    [2.583333, -40.133333],
    [-3.966667, -35.266667],
    [-5.116667, -30.15],
    [-2.633333, -27.6],
    [-0.6, -29.133333],
]

m = folium.Map(location=[48, -102], zoom_start=3, control_scale=True)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Уровень безработицы (%)",
).add_to(m)

#Этот плагин добавляет маленькую обзорную карту в низкий правый угол
MiniMap().add_to(m)

#Этот плагин захватывает движение вашего курсора по карте
#и с помощью его данных можно выводить над какой координатой находится ваш курсор
formatter = "function(num) {return L.Util.formatNum(num, 3) + ' &deg; ';};"

MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Координаты:",
    lat_formatter=formatter,
    lng_formatter=formatter,
).add_to(m)

#Этот плагин добавляет на страницу с картой поиск
folium.plugins.Geocoder().add_to(m)

folium.LayerControl().add_to(m)

#Этот плагин показывает солнечные сутки на Земле в реальном времени
folium.plugins.Terminator().add_to(m)

#Этот плагин добавляет анимированную линию на карту
#по заданной матрице мировых координат
folium.plugins.AntPath(
    locations=wind_locations, reverse="True", dash_array=[20, 30]
).add_to(m)

#Этот плагин добавляет возможность измерять 
#расстояние и площади прямо на карте
m.add_child(MeasureControl())

m.fit_bounds(m.get_bounds())

#Этот плагин добавляет в правый верхний угол возможность 
#зайти в полноэкранный режим
folium.plugins.Fullscreen(
    position="topright",
    title="Расширить карту",
    title_cancel="Закрыть",
    force_separate_button=True,
).add_to(m)

#Этот плагин добавляет возможность, нажав на карту, 
#поставить метку и нажав на нее, 
#увидеть точные координаты выбранной точки
m.add_child(folium.ClickForMarker("<b>Широта:</b> ${lat}<br /><b>Долгота:</b> ${lng}"))

m.save("interesting_projects/Создание интерактивной карты/USA.html")