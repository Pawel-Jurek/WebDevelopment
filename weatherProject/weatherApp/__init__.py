import os

from weatherProject import settings

cityList = []

with open(os.path.join(settings.BASE_DIR, 'staticfiles', 'cityList.txt'), 'r', encoding='utf-8') as file:
    data = file.read().split("\n")

for line in data:
    cityList.append(line[0].upper() + line[1::])



