Разделим задание на две части. Необходимо найти, о каких темах больше всего говорят
спикеры, после чего выяснить какие темы больше нравятся (или вызывают другие эмоции)
у пользователей.

Начнем с первой части. Давайте сгрузим все субтитры, соединив субтритры
из каждого ролика в какой-то текст, затем запустим Word Count, после чего будем
аккуратно отфильтровывать слова, который нам не нужны. Скорее всего, этого будет
недостаточно, но зато у нас появится база для дальнейших исследований.

Напишем простой скрипт на Python, распаралеллим загрузку задач с помощью threading.
(scripts/download_subtitles.py)

Получившаяся папка data/subtitles содержит около двух тысяч файлов и занимает 46.7 МБ.
Закоммитим.

Теперь попробуем "в тупую" посчитать слова, скрипт - scripts/word_count.py
Для начала обойдемся без MapReduce, простым перебором файлов и слов.

Сделал словарь, который сохранил в JSON файл. Закоммитим.

Попробуем найти самые популярные слова.

```
('и', 110765), ('в', 99379), ('что', 64899), ('я', 56904), ('это', 53425), ('не', 46658), ('на', 46623), ('мы', 42515), ('с', 30713), ('как', 28271), ('но', 22371), ('вы', 20946), ('они', 19623), ('из', 17329), ('для', 16425), ('а', 16158), ('так', 15966), ('у', 15096), ('о', 14758), ('к', 14646), ('он', 14552), ('если', 13608), ('то', 13395), ('по', 12846), ('когда', 12504), ('чтобы', 12046), ('бы', 10790), ('или', 10612), ('их', 10606), ('есть', 10133), ('за', 9988), ('от', 9705), ('было', 9471), ('вот', 9370), ('же', 9336), ('все', 9096), ('очень', 9058), ('мне', 9015), ('его', 8930), ('которые', 8612), ('она', 8453), ('меня', 8450), ('нас', 8003), ('всё', 7479), ('потому', 7283), ('смех', 7278), ('нам', 7204), ('только', 6927), ('был', 6676), ('лет', 6514), ('эти', 6460), ('том', 6446), ('вам', 6265), ('может', 6072), ('того', 5976), ('людей', 5929), ('быть', 5926), ('чем', 5755), ('просто', 5593), ('до', 5572), ('этого', 5554), ('люди', 5519), ('можно', 5489), ('этот', 5262), ('этом', 5238), ('больше', 5230), ('который', 5081), ('были', 5072), ('ещё', 4940), ('вас', 4894), ('была', 4841), ('время', 4805), ('более', 4734), ('здесь', 4643), ('нет', 4640), ('где', 4602), ('будет', 4460), ('сейчас', 4458), ('них', 4402), ('её', 4370), ('ли', 4367), ('даже', 4270), ('аплодисменты', 4026), ('этой', 3998), ('во', 3919), ('нужно', 3870), ('уже', 3867), ('сделать', 3838), ('один', 3795), ('жизни', 3695), ('также', 3687), ('можем', 3597), ('всего', 3573), ('себя', 3535), ('много', 3492), ('об', 3473), ('ты', 3372), ('там', 3357), ('теперь', 3328), ('со', 3309), ('этих', 3227), ('поэтому', 3224), ('кто', 3179), ('которая', 3148), ('эта', 3131), ('самом', 3104), ('почему', 3084), ('думаю', 3076), ('могут', 3041), ('раз', 2999), ('всех', 2979), ('хочу', 2947), ('должны', 2937), ('тем', 2935), ('спасибо', 2932), ('деле', 2929), ('им', 2883), ('при', 2828), ('через', 2814), ('после', 2810), ('чтото', 2802), ('эту', 2788), ('можете', 2776), ('сегодня', 2746), ('итак', 2687), ('назад', 2668), ('сказал', 2642), ('да', 2636), ('несколько', 2614), ('себе', 2572), ('каждый', 2537), ('жизнь', 2528), ('именно', 2515), ('возможно', 2449), ('человек', 2440), ('делать', 2420), ('этим', 2391), ('день', 2368), ('ни', 2343), ('действительно', 2331), ('мой', 2328), ('мире', 2321), ('под', 2319), ('хорошо', 2310), ('тогда', 2299), ('например', 2235), ('которых', 2214), ('между', 2207), ('мир', 2195), ('конечно', 2163), ('времени', 2159), ('затем', 2154), ('вопрос', 2129), ('году', 2105), ('одна', 2078), ('образом', 2046), ('года', 2025), ('потом', 2019), ('происходит', 2018), ('сказать', 2014), ('два', 1971), ('таким', 1965), ('никогда', 1944), ('является', 1937), ('без', 1929), ('оно', 1920), ('которой', 1919), ('человека', 1911), ('те', 1903), ('знаете', 1895), ('над', 1894), ('всегда', 1892), ('наши', 1881), ('других', 1871), ('видите', 1866), ('тех', 1855), ('пока', 1854), ('лучше', 1854), ('могли', 1848), ('которую', 1846), ('вместе', 1840), ('детей', 1831), ('некоторые', 1827), ('такие', 1811), ('такой', 1807), ('которое', 1783), ('моя', 1772), ('часть', 1749), ('другой', 1747), ('нашей', 1742), ('могу', 1737), ('своей', 1737), ('тот', 1737), ('ничего', 1725), ('свою', 1712), ('него', 1701), ('будут', 1698), ('моей', 1696), ('10', 1683), ('ведь', 1669), ('три', 1651), ('давайте', 1651), ('еще', 1650), ('вещи', 1626), ('использовать', 1625), ('многие', 1604), ('знаю', 1595), ('такое', 1577), ('лишь', 1569), ('немного', 1558), ('момент', 1551), ('год', 1521), ('ему', 1515), ('мира', 1512), ('надо', 1509), ('другие', 1496), ('сша', 1487), ('самое', 1484), ('тоже', 1483), ('ну', 1480), ('около', 1478), ('одной', 1462), ('свои', 1460), ('понять', 1456), ('важно', 1456), ('наших', 1453), ('таких', 1444), ('истории', 1440), ('снова', 1430), ('друг', 1425), ('перед', 1399), ('знаем', 1392), ('проблема', 1391), ('долларов', 1377), ('всем', 1370), ('хотел', 1361), ('возможность', 1355), ('тут', 1337), ('тому', 1334), ('значит', 1321), ('кажется', 1321), ('изза', 1320), ('идея', 1315), ('найти', 1313), ('проблемы', 1308), ('ее', 1302), ('должен', 1298), ('помощью', 1292), ('дело', 1289), ('место', 1285), ('создать', 1280), ('работы', 1265)
```

Ерунда. Хотя, можно сказать, что смеются на лекциях TED, чаще чем апплодируют и
еще пару выводов.
Запишем в results.md.

Разбивать на категории - не вариант, слишком много слов и большинство из них может относиться
к нескольким темам. Даже введение коэффицента похожести на тему с помощью теории
вероятностей, скорее всего, даст неточный результат. Жаль. Признаем ошибку.

Внимательно изучаем страницу лекции на ted.com. Есть поле "Similar topics" с сразу
несколькими темами выступления, судя по всему, сортированные по приоритетности.
Там же есть оценки к выступлению. API у них есть, но регистрация закрыта. Придется парсить сайт.

Пишем скрипт на Python (scripts/scrape_lections.py). Расчехляем замечательный lxml.html.

К сожалению, TED ограничивает количество запросов в секунду, так что придется убрать threading
и просто подождать.

ОК, мы получили темы и рейтинги для 2125 лекций, положили все это в json файл
(data/lections.json).

Не могу придумать ничего умнее, чем распарсить его в Python shell
(можно было бы IPython Notebook сделать, но это будет избыточно для наших целей)
и просто делать выводы.

Начнем:
```
import json
lections = json.loads(open('data/lections.json').read())
RATINGS = ['Funny', 'Confusing', 'Unconvincing', 'Informative', 'Fascinating',
           'Persuasive', 'Obnoxious', 'Courageous', 'Beautiful', 'Longwinded',
           'Inspiring', 'Ingenious', 'Jaw-dropping', 'OK']
```

Посчитаем среднее количество оценок в процентном соотношении для всех выстулений.
```
>>> ratings_sum = 0
>>> emotions_sum = {}
>>> for lection in lections:
...     for rating in lection['ratings']:
...         ratings_sum += lection['ratings'][rating]
...         emotions_sum[rating] = emotions_sum.get(rating, 0) + lection['ratings'][rating]
>>> ratings_sum
4905317
>>> emotions_sum
{'Unconvincing': 114769, 'Longwinded': 72438, 'Jaw-dropping': 334078, 'Confusing': 44186, 'Courageous': 318225, 'Persuasive': 450626, 'OK': 170385, 'Obnoxious': 55945, 'Informative': 670675, 'Funny': 311804, 'Inspiring': 1035835, 'Ingenious': 318702, 'Fascinating': 642287, 'Beautiful': 365362}
>>> for (rating, value) in emotions_sum.items():
...     print(rating, value / ratings_sum * 100, '%')
```
Результаты:
```
Unconvincing 2.339685692076577 %
Longwinded 1.476724134240458 %
Jaw-dropping 6.810528249244646 %
Confusing 0.900777666356731 %
Courageous 6.487348320200305 %
Persuasive 9.186480710624819 %
OK 3.4734758222557276 %
Obnoxious 1.1404971381054476 %
Informative 13.672408939116472 %
Funny 6.3564495424047 %
Inspiring 21.1165761560364 %
Ingenious 6.497072462391319 %
Fascinating 13.09368996947598 %
Beautiful 7.448285197470418 %
```
Запишем выводы в results.md.

Теперь к сути задания. Попробуем сделать то же самое для каждой темы лекции.

```
>>> topics = {}
>>> topics_sum = {}
>>> for lection in lections:
...     for topic in lection['topics']:
...         topics[topic] = topics.get(topic, {})
...         topics_sum[topic] = topics_sum.get(topic, 0)
...         for rating in lection['ratings']:
...             topics[topic][rating] = topics[topic].get(rating, 0) + lection['ratings'][rating]
...             topics_sum[topic] += lection['ratings'][rating]
...
```

У нас что-то получилось.
```
>>> topics_sum
{'TEDx': 764892, 'urban': 776, 'rocket science': 4295, 'nuclear weapons': 2515, 'activism': 132524, 'security': 21302, 'memory': 31690, 'cloud': 1479, 'arts': 358809, 'natural disaster': 6189, 'leadership': 171484, 'war': 130377, 'meme': 13199, 'data': 93488, 'primates': 8984, 'pollution': 19415, 'language': 85703, 'nuclear energy': 7403, 'oil': 6263, 'science': 1066835, 'materials': 20900, 'TED Books': 36886, 'Latin America': 14669, 'media': 100790, 'humor': 167372, 'theater': 13734, 'microfinance': 1830, 'morality': 38429, 'simplicity': 32564, 'evil': 12982, 'visualizations': 121259, 'global issues': 899390, 'water': 21875, 'ancient world': 13159, 'plastic': 15707, 'literature': 26622, 'animals': 159042, 'history': 125997, 'composing': 3864, 'philanthropy': 55027, 'medical research': 38430, 'climate change': 68723, 'religion': 131649, 'politics': 284288, 'dinosaurs': 10046, 'biology': 280055, 'violence': 68624, 'performance art': 18993, 'spoken word': 36638, 'mining': 5158, 'violin': 10285, 'potential': 37645, 'cello': 1298, 'pain': 10561, 'poverty': 81930, 'piano': 16191, 'gender': 40147, 'cognitive science': 56763, 'personal growth': 68901, 'books': 85987, 'cosmos': 25703, 'privacy': 19742, 'microsoft': 21020, 'medicine': 218709, 'God': 57883, 'nanoscale': 12381, 'goal-setting': 101933, 'crime': 72199, 'disease': 62519, 'nature': 75984, 'computers': 146644, 'race': 41465, 'vocals': 1597, 'exoskeleton': 13359, 'empathy': 12799, 'state-building': 4679, 'atheism': 29895, 'identity': 68797, 'TED Fellows': 143007, 'dance': 136154, 'singer': 9544, 'sociology': 24773, 'china': 33307, 'urban planning': 16600, 'terrorism': 38340, 'feminism': 48588, 'neurology': 27737, 'TED-Ed': 14760, 'wikipedia': 13524, 'interface design': 52771, 'communication': 194674, 'wind energy': 5777, 'food': 126873, 'mindfulness': 10405, 'collaboration': 134710, 'big bang': 18540, 'disaster relief': 19724, 'Autism spectrum disorder': 18682, 'solar energy': 9430, 'sex': 80261, 'biomechanics': 21841, 'Egypt': 11864, 'submarine': 15251, 'failure': 32942, 'cyborg': 6356, 'One Laptop Per Child': 3604, 'trees': 13099, 'disability': 34235, 'jazz': 4506, 'map': 14866, 'Christianity': 16974, 'software': 56365, 'curiosity': 19140, 'robots': 62556, 'biomimicry': 21557, 'garden': 31316, 'magic': 66284, 'suicide': 46469, 'extraterrestrial life': 9270, 'NASA': 18976, 'prediction': 9222, 'museums': 7869, 'prison': 28919, 'work': 174674, 'democracy': 34446, 'photography': 177511, 'novel': 10731, 'sight': 21680, 'Debate': 3001, 'military': 33965, 'testing': 8166, 'behavioral economics': 18491, 'sports': 49008, 'cancer': 48059, 'time': 39457, 'entertainment': 683645, 'entrepreneur': 113164, 'inequality': 86695, 'virus': 7147, 'travel': 12762, 'sound': 32572, 'beauty': 39903, 'fish': 57141, 'faith': 51557, 'statistics': 100115, 'intelligence': 47204, 'alternative energy': 43808, 'art': 199846, 'third world': 21736, 'AI': 38395, 'youth': 60068, 'energy': 74504, 'monkeys': 11333, 'student': 17792, 'chautauqua': 1503, 'compassion': 34531, 'marketing': 43557, 'wunderkind': 14845, 'women in business': 47356, 'children': 298090, 'TEDYouth': 26213, 'community': 96392, 'social media': 60321, 'hack': 28287, 'vulnerability': 821, 'india': 31973, 'skateboarding': 898, 'mental health': 158171, 'origami': 3215, 'Buddhism': 46564, 'TED Prize': 38795, 'consumerism': 48985, 'life': 169596, 'speech': 21552, 'journalism': 55565, 'shopping': 5928, 'biodiversity': 56399, 'biotech': 34730, 'adventure': 41730, 'web': 57444, 'Surgery': 5853, 'yesallwomen': 25336, 'mobility': 1334, 'Transgender': 9012, 'future': 89930, 'flight': 11758, 'design': 681221, 'psychology': 502600, 'Senses': 26621, 'transportation': 42872, 'anthropology': 21147, 'business': 884955, 'DNA': 19894, 'development': 115052, 'law': 63349, 'Bioethics': 18321, 'insects': 41907, 'green': 98363, 'MacArthur grant': 24811, 'brain': 465587, 'product design': 23900, 'United States': 15883, 'math': 92547, 'oceans': 93268, 'TED Brain Trust': 221140, 'conducting': 38282, 'human origins': 16107, 'philosophy': 135670, 'mission blue': 18884, 'String theory': 30431, 'biosphere': 17486, 'exploration': 104193, 'environment': 143474, 'performance': 160897, 'painting': 366, 'online video': 50550, 'Islam': 10066, 'ebola': 4166, 'relationships': 74036, 'society': 147439, 'health': 339156, 'corruption': 18787, 'news': 18429, 'poetry': 110845, 'self': 205815, 'Brand': 4015, 'cars': 24784, 'money': 49718, 'depression': 103718, 'fashion': 24691, 'ants': 4848, 'apes': 13030, 'agriculture': 40994, 'public health': 25242, 'storytelling': 243955, 'policy': 42460, 'industrial design': 17068, 'big problems': 19894, 'heart health': 12366, 'aging': 56219, 'peace': 97004, 'Africa': 140314, 'family': 28203, 'film': 91016, 'social change': 212842, 'iraq': 21122, 'meditation': 10405, 'smell': 9770, 'choice': 82871, 'Google': 47403, 'neuroscience': 75830, 'education': 545166, 'geology': 3213, 'demo': 175147, 'writing': 138108, 'mind': 81530, 'immigration': 5674, 'toy': 21542, 'happiness': 244067, 'Vaccines': 5666, 'music': 210596, 'economics': 274479, 'typography': 7549, 'engineering': 63070, 'world cultures': 26498, 'culture': 1472658, 'government': 68786, 'women': 161682, 'fear': 70174, 'charter for compassion': 4727, 'consciousness': 107824, 'space': 71961, 'motivation': 93973, 'love': 98182, 'Internet': 91672, 'AIDS': 14280, 'astronomy': 50807, 'Gender spectrum': 7014, 'Planets': 27066, 'comedy': 89468, 'chemistry': 11313, 'complexity': 34533, 'guitar': 9207, 'presentation': 26729, 'bacteria': 26565, 'genetics': 43664, 'success': 168486, 'sustainability': 81961, 'technology': 1217553, 'LGBT': 25924, 'Moon': 4128, 'Brazil': 13505, 'population': 7872, 'open-source': 60243, 'dark matter': 10886, 'aircraft': 6201, 'prosthetics': 42767, 'gaming': 68492, 'botany': 5827, 'universe': 66775, 'advertising': 25275, 'decision-making': 55755, 'obesity': 37893, 'interview': 8869, 'live music': 87928, 'illness': 102921, 'body language': 90424, 'trafficking': 9691, 'play': 34498, 'Middle East': 39707, 'paleontology': 7792, 'illusion': 63461, 'innovation': 142850, 'death': 73398, 'health care': 132380, 'New York': 5101, 'cooperation': 9775, 'deextinction': 9518, 'physics': 110517, 'invention': 172505, 'glacier': 2776, 'algorithm': 13171, 'pandemic': 868, 'solar': 5582, 'cities': 153449, 'Europe': 13990, 'humanity': 92843, 'Foreign Policy': 21033, 'protests': 8929, 'men': 19010, 'extreme sports': 9658, 'telecom': 10994, 'epidemiology': 2807, 'Slavery': 13868, 'library': 22334, 'creativity': 471551, 'microbiology': 22187, 'productivity': 38968, 'bees': 17701, 'birds': 10654, 'Iran': 10906, 'bullying': 16110, 'evolution': 184083, 'finance': 12407, 'parenting': 123337, 'weather': 5062, 'investment': 23965, 'drones': 25335, 'architecture': 104226, 'sanitation': 9711, 'Asia': 76927}
```

Для компактности не привожу содержание topics. Сделаем подобную прошлой статистике.
```
>>> for topic in topics:
...     print()
...     print(topic.upper())
...     for rating in topics[topic]:
...        print(rating, topics[topic][rating] / topics_sum[topic] * 100, '%')
...     print()
```

Результат положил в data/topics.txt, он фактически является ответом на задание.
Тем не менее, получить данные - еще не все. Нужно сделать по ним выводы. Чуть-чуть изменим
предыдущий код, чтобы данные были сохранены в список, который мы в дальнейшем будем сортировать.

```
>>> result = []
>>> for topic in topics:
...     topic_result = []
...     topic_result.append(topic)
...     for rating in topics[topic]:
...         topic_result.append((rating, topics[topic][rating] / topics_sum[topic] * 100))
...     result.append(topic_result)
...
>>> result[0]
['TEDx', ('Unconvincing', 2.2656793377365694), ('Longwinded', 1.39326859216726), ('Jaw-dropping', 4.444941246607364), ('Confusing', 0.7275536938548187), ('Courageous', 7.549693290033102), ('Persuasive', 10.49102356934051), ('OK', 3.162537979217981), ('Obnoxious', 1.0507365745752342), ('Informative', 13.842738582701871), ('Funny', 6.4810456901105), ('Inspiring', 24.81526803784064), ('Ingenious', 5.849061043912082), ('Fascinating', 11.153470032370583), ('Beautiful', 6.772982329531489)]
```

Для начала, посмотрим, какие темы пользователи считают наиболее скучными.
```
>>> sorted(result, key=lambda x: x[2], reverse=True)[0]
['mobility', ('Unconvincing', 11.319340329835082), ('Longwinded', 10.569715142428786), ('Jaw-dropping', 1.424287856071964), ('Confusing', 0.8995502248875562), ('Courageous', 3.523238380809595), ('Persuasive', 13.718140929535233), ('OK', 8.920539730134932), ('Obnoxious', 2.998500749625187), ('Informative', 22.038980509745127), ('Funny', 0.0), ('Inspiring', 14.317841079460269), ('Ingenious', 3.373313343328336), ('Fascinating', 6.296851574212893), ('Beautiful', 0.5997001499250375)]
>>> sorted(result, key=lambda x: x[2], reverse=True)[1]
['extraterrestrial life', ('Unconvincing', 4.196332254584681), ('Longwinded', 5.382955771305286), ('Jaw-dropping', 2.7292340884573894), ('Confusing', 1.3592233009708738), ('Courageous', 2.38403451995685), ('Persuasive', 4.47680690399137), ('OK', 6.235167206040993), ('Obnoxious', 1.7907227615965482), ('Informative', 11.014023732470335), ('Funny', 20.733549083063647), ('Inspiring', 12.696871628910463), ('Ingenious', 5.458468176914779), ('Fascinating', 13.53829557713053), ('Beautiful', 8.004314994606258)]
>>> sorted(result, key=lambda x: x[2], reverse=True)[2]
['charter for compassion', ('Unconvincing', 3.7021366617304845), ('Longwinded', 4.67526972709964), ('Jaw-dropping', 1.650095197799873), ('Confusing', 1.7770255976306326), ('Courageous', 3.6809815950920246), ('Persuasive', 11.085254918552993), ('OK', 4.63295959382272), ('Obnoxious', 2.094351597207531), ('Informative', 8.440871588745505), ('Funny', 1.692405331076793), ('Inspiring', 33.14998942246668), ('Ingenious', 2.1366617304844513), ('Fascinating', 6.8330865242225505), ('Beautiful', 14.44891051406812)]
```
По-моему, неплохо. Дальше - по аналогии. Запишем в results.md.

Забыл про рейтинг тем, на которые обращают внимание выступающие. Просто перебираем
все лекции и их темы.

```
>>> topics_rating = {}
>>> for lection in lections:
...     for topic in lection['topics']:
...         topics_rating[topic] = topics_rating.get(topic, 0) + 1
```

Одной строчкой сортируем:
```
>>> sorted(topics_rating.items(), key=lambda x: x[1], reverse=True)[:5]
[('technology', 599), ('culture', 461), ('science', 452), ('global issues', 431), ('design', 351)]
```

Запишем результаты в results.md. Закоммитим. Отправляем.
