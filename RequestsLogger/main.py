import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')



sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    # ДОПОЛНИТЬ КОД ЗДЕСЬ
    logging.basicConfig(level=logging.INFO)

    success_logger = logging.getLogger('success_responses')
    success_handler = logging.getLogger('success_responses.log')
    success_handler.setLevel(logging.INFO)
    success_logger.addHandler('success_handler')

    response = rq.get(site, timeout=3)
    print(response)
