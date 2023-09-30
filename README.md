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
