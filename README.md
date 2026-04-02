# json-catalog-linker
 Автоматически заполняет manual_url в JSON-каталоге контроллеров, сопоставляя name с внешним файлом со ссылками на Яндекс.Диск. Поддерживает TXT/CSV с нумерацией, игнорирует регистр и пробелы. Экономит часы ручной работы.

 json-catalog-linker
🔄 Скрипт для автоматического обновления поля manual_url в JSON-каталоге контроллеров, используя внешний файл со ссылками на Яндекс.Диск.
💡 Зачем это нужно?
У тебя есть:
catalog.json — каталог контроллеров с полями name, manual_url и другими
links.txt — файл со списком имя_контроллера;ссылка_на_папку
Скрипт находит совпадения по name и подставляет актуальные ссылки в manual_url. Идеально для поддержки актуальности документации в проектах по учёту LED-оборудования.

Формат входных файлов
catalog.json

[
  {
    "name": "BX-5Q1-U-E-75A",
    "category": "fullcolor_controllers",
    "manual_url": "",
    "url": "http://...",
    "specs": { ... }
  }
]

links.txt

name;manual_url
1. BX-5A0-WIFI;https://disk.yandex.ru/d/abc123
23. BX-5Q1-U-E-75A;https://disk.yandex.ru/d/xyz789

Поддерживается:
Нумерация строк (1., 23.) — автоматически удаляется
Заголовок name;manual_url — пропускается
Разделитель ; (точка с запятой)
Любой регистр имён (сравнение нечувствительно к регистру)


Быстрый старт
# 1. Клонируй репо
git clone https://github.com/твой-ник/json-catalog-linker.git
cd json-catalog-linker

# 2. Положи рядом файлы:
#    - catalog.json
#    - links.txt

# 3. Запусти
python update_manuals.py

# 4. Готово! Результат в:
#    → catalog_updated.json

