# interesting_projects

**Собираю интересные проекты по машинному обучению в одном месте.**

## 1. Генерация картинок по текстовому запросу с помощью Stable Diffusion Model.

Для начала нам следует утановить следующие библиотеки за наш компьютер:
```
pip install diffusers
pip install invisible_watermark transformers safetensors
```
И если у вас нет базовых библиотек matplotlib и numpy, то их тоже нужно будет установить.

Мне еще понадобилась установка просто transformers:
```
pip install transformers
```

Но так как при каждом запуске программы будет происходить устаноновка диффузионной модели и контрольных точек, что занимает крайне много времени и очень сильно напрягает компьютер, то я решила переместиться на Google Colab.

В папке Stable Diffusion Model вы сможете найти файл .ipynb в нем есть все пояснения к работе с кодом и для его понимания.
>лучше его открывать по ссылке сверху - Open in Colab, там можно увидеть обновленные версии файла, запустить программу самостоятельно, а лучше скопировать файл себе на Google Drive и самостоятельно его модифицировать.

Так же в этой папке храняться все сгенерированные мной изображения, на данный момент.(папка images)

Русский текст очень плохо понимает, промты нужно писать на английском.

## 2. Создание интерактивной карты на Python.

Для этого нам понадбится установить библиотеку folium
```
pip install folium
```

**Файл drawing_in_map.py**

В данной программе реализуется карта, на которой:
 - С помощью плагина Choropleth реализутся визуализация уровня безработиты в США по штатам, данные по безработице: "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv", данные с координатами штатов США: https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json 

Далее в коде, при вызове LayerControl() на страницу добавляется легенда, показывающая соотношение процентов безработицы и цвета на карте.
 - Далее с помощью MousePosition реализуется вывод в верхний правый угол экрана значение ширины и долготы точки на карте, которая находится под курсором.
 - plugins.Geocoder() добавляет в правый верхний угол поиск по карте. И при поиске в строке, перенаправляет вас на карте к выбранному объекту.
 - plugins.Terminator() - данный плагин показывает солнечные сутки на поверхности Земли в реальном времени.
 - plugins.AntPath() - добавляет на карту анимированную линию по заданной матрице кооординат(wind_locations). В случае данной программы - схематично визуализированно движение теплого Южного Пассатного течения, переходящего в Гвианское.
 - Плагин MeasureControl() добавляет на страницу(в правый верхний угол) кнопку, при нажатии на которую можно измерить размеры и площади заданных вами на карте линий и фигур.
 - plugins.Fullscreen() - кнопка(добавляется в правый верхний угол) перехода в полноэкранный режим.
 - Плагин ClickForMarker() при нажатии на карту добавляет метку в выбранное место, а при нажатии на метку показывает ее точные мировые координаты.
 
Карту сохраняем в формате .html(**USA.html**) и открываем в браузере, также ее можно сохранить в формате .json.

**Файл Video_map.ipynb**

С помощью плагина raster_layers.VideoOverlay() добавляем на карту видео.
