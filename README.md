**Веб-сайт для раскрашивания изображений**

Работает с помощью нейросети, описанной тут: https://github.com/jantic/DeOldify

## Как запустить?

Создание виртуального окружения:

```bash
# Создание venv
python -m venv venv
# Активация venv
venv\Scripts\activate
# Обновление pip
python -m pip install --upgrade pip
# Установка зависимостей
python -m pip install -r requirements.txt
```

Скачать модель отсюда: https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth и поместить ее в папку models.

```bash
# Запуск модели
python webserver.py
```

Теперь можно открыть окно в браузере и проверить модель в действии по адресу *localhost:1024*
