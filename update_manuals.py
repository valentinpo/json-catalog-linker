import json
import re
import os

CATALOG_FILE = "catalog.json"
LINKS_FILE = "links.txt"
OUTPUT_FILE = "catalog_updated.json"

# 1. Загружаем каталог
with open(CATALOG_FILE, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# 2. Парсим файл со ссылками (формат: "23. BX-5Q1-U-E-75A;https://...")
links_dict = {}
with open(LINKS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.lower().startswith("name;"):
            continue
        # Убираем нумерацию "1. ", "23. " и т.д.
        line = re.sub(r'^\d+\.\s*', '', line)
        parts = line.split(";")
        if len(parts) >= 2:
            name = parts[0].strip().lower()
            url = parts[1].strip()
            if name and url:
                links_dict[name] = url

print(f"📥 Загружено ссылок: {len(links_dict)}")

# 3. Обновляем каталог
updated = 0
not_found = []

for ctrl in catalog:
    key = str(ctrl.get("name", "")).strip().lower()
    if key in links_dict:
        ctrl["manual_url"] = links_dict[key]
        updated += 1
        print(f"✓ {key}")
    else:
        not_found.append(key)

# 4. Сохраняем
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"\n✅ Обновлено: {updated} записей")
print(f"❌ Не найдено: {len(not_found)}")
if not_found:
    print("   Примеры:", not_found[:5])
print(f"📁 Результат: {os.path.abspath(OUTPUT_FILE)}")