import os
import collections
import json

words = []
lections = os.listdir('data/subtitles')
for file_name in lections:
    if file_name == '.keep':
        continue
    with open('data/subtitles/' + file_name) as lection_file:
        text = lection_file.read()
        # Оптимизируем программу, делая свою реализацию split
        word_buffer = ''
        for sym in text:
            if sym.lower() in 'йцукенгшщзхъфывапролджэёячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890':
                word_buffer += sym.lower()
            if sym == ' ' and word_buffer:
                words.append(word_buffer)
                word_buffer = ''
with open('data/word_count.json', 'w') as results_file:
    print(json.dumps(dict(collections.Counter(words))), file=results_file)
