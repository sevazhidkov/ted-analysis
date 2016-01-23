import time
import random
import threading
import requests


def proccess_lection(lection_id):
    try:
        ted_url = 'http://www.ted.com/talks/subtitles/id/{}/lang/ru/format/srt'
        subtitles_url = ted_url.format(lection_id)
        subtitles = requests.get(subtitles_url).text
    except Exception:
        print('Trying again for', lection_id)
        time.sleep(2)
        proccess_lection(lection_id)
        return
    text = ''
    for string in subtitles.split('\n'):
        if (string == '\n' or string.isdigit() or
            '-->' in string):
            continue
        # Лишние пробелы (если они есть), будут отсеяны при Word Count
        text += ' ' + string
    # Обработаем ошибки, связанные с открытием файлов
    try:
        lection_file = open('data/subtitles/' + str(lection_id) + '.txt', 'w')
        lection_file.write(text)
        lection_file.close()
    except:
        print('Error with open file', lection_id)
        time.sleep(10 + random.randint(1, 40))
        lection_file = open('data/subtitles/' + str(lection_id) + '.txt', 'w')
        lection_file.write(text)
        lection_file.close()

threads = []

# Существует не более 2500 лекций
for i in range(1, 2500):
    # Обработаем ошибки, связанные с созданием потоков
    try:
        thread = threading.Thread(target=proccess_lection, args=(i, ))
        thread.start()
        threads.append(thread)
    except Exception:
        print('Error with starting thread', i)
        time.sleep(5)
        thread = threading.Thread(target=proccess_lection, args=(i, ))
        thread.start()
        threads.append(thread)

# Дождемся выполнения всех потоков
for thread in threads:
    thread.join()
