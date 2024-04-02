from my_module import parse_news, save_to_json

# Посилання на сайт новин, який будемо парсити
news_url = 'https://www.bbc.com'

parsed_news = parse_news(news_url)

# Збереження даних у JSON-файл
save_to_json(parsed_news, 'news_data.json')
