import time
import random
import json
import re
import requests
import lxml.html

RATINGS = ['Funny', 'Confusing', 'Unconvincing', 'Informative', 'Fascinating',
           'Persuasive', 'Obnoxious', 'Courageous', 'Beautiful', 'Longwinded',
           'Inspiring', 'Ingenious', 'Jaw-dropping', 'OK']
LECTION_TOPICS_REGEX = re.compile(r'<meta content="(.+)" name="keywords" />')

lections = []


def proccess_lection(lection_id):
    global lections
    try:
        ted_url = 'http://www.ted.com/talks/{}'
        response = requests.get(ted_url.format(lection_id))
        assert response.status_code != 429
        html = response.text
    except Exception:
        print('Trying again for', lection_id)
        time.sleep(2 + random.randint(1, 10))
        proccess_lection(lection_id)
        return


    lection_page = lxml.html.document_fromstring(html)
    lection = {'id': lection_id, 'topics': [], 'ratings': {}}

    # Получим рейтинг лекции по разным параметрам
    for rating in RATINGS:
        # Создадим регулярное выражение для поиска рейтинга
        regex = re.compile(r'"name":"{}","count":(\d+)'.format(rating))
        match = re.search(regex, lection_page.text_content())
        if match is None:
            print('No rating for', rating, 'in', lection_id)
            return
        rating_count = match.group(1)
        lection['ratings'][rating] = int(rating_count)

    # Получаем список тем лекции
    match = re.search(LECTION_TOPICS_REGEX, html)
    if match is None:
        print('No topics for', lection_id)
        return
    topics_list = match.group(1)
    for topic in topics_list.split(', '):
        # Убираем ненужные категории
        if topic not in ['TED', 'talks', 'TED Conference']:
            lection['topics'].append(topic)
    lections.append(lection)

threads = []

# Существует не более 2500 лекций
for i in range(1, 2500):
    proccess_lection(i)
    if i % 10 == 0:
        print(i, 'lections done.')

print(len(lections))

result_file = open('data/lections.json', 'w')
result_file.write(json.dumps(lections))
result_file.close()
