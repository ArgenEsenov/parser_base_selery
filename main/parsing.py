import time
import pandas as pd
import requests
import json
import asyncio
import httpx
import logging


'##### Келген баардык мааалыматтарды иреттеп база данныхка жуктоо ###'
def save_data_to_db(data):
        for a in data:
            cat_id = a['cat_id']
            title = a['title']
            price = a['price']
            description = a['description']
            phone = a['phone']
            city = a['city']
            image = a['images']
            imgs = {}
            for img in image:
                imgs['images'] = ("file.jpg", img, 'image/jpeg')
            try:
                nameseller = a['user']['username']
            except:
                nameseller = ''

            w = { 'user':1, 'category':cat_id,
                  'title': title, 'price': price,
                 'description': description, 'phone': phone,
                  'nameseller': nameseller, 'city':city  }
            requests.post('http://127.0.0.1:8000/create_ads/',data = w, files=imgs)


cats = {
    2043:18,
    2046: 19,
    5830: 20,
    5831: 21,
}
"""### Бизге берилген сайтка суроо (запрос) жонотуу####"""
"""### Асихронндук код менен да суроо (запрос) жонотуу ###"""
async def get_json(client, url, params,cat_id):
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc"
        }
        params['category_id'] = cat_id
        resp = await client.get(url, headers=headers, params=params)
        return resp.json()


def save_json(data):
    """### бизге келген маалыматтарды коруу учун 'json'json папкасына сактоо  ###"""
    with open('../lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        logging.info(f'Данные сохранены в lalafo_data.json')


def save_filter_json(data):
    with open('lalafo_filter_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        logging.info(f'Данные сохранены в lalafo_filter_data.json')


def get_data_from_json(data_json, category_id):
    """### бизге керектелуучу маалыматтарды  фильтирлоо   ###"""
    print(category_id)
    result = []
    for d in data_json['items']:
        post_id = d['id']
        title = d['title']
        phone = d['mobile']
        description = d['description']
        price = d['price']
        for image in d['images']:
            try:
                images = image['original_url']
            except:
                images  = 'без изображения'
        city = d['city']
        try:
            nameseller = d['user']['username']
        except:
            nameseller = ''

        result.append({
            'post_id': post_id,
            'city': city,
            'name_seller': nameseller,
            'phone': phone,
            'title': title,
            'price': price,
            'description': description,
            'images': images,
            "cat_id": category_id,
        })
    return result


"""### фИЛЬТИРЛЕНГЕН маалыматтарды "excel" файлына сактоо ###"""
def save_excel(data):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('../lalafo_result.xlsx')
    df.to_excel(writer, 'data')
    writer.save()
    logging.info('Все сохранено в lalafo_result.xlsx')



start = time.time()
result = []
params = {
        "expand": "url",
        'city_id': 103184,  # id города (пример: 103184 - Бишкек, 103209 - Джалал-Абад, 103218 - Ош и тд)
        'category_id': 0, # категория товара (пример: 1317 - Электроника, 1501 - Транспорт, 1484 - Животные и тд)
        'per-page':10, # количество результатов на странице
        'currency': 'KGS',   # валюта. Доступны: KGS, USD


}

def theand ():
        async def main():
            """### Жана асихрондук код менен бизге берилген сайтка суроо(запрос) жонотуу ###"""
            async with httpx.AsyncClient() as client:
                tasks = []
                for cat_id in cats:
                    url = f'https://lalafo.kg/api/search/v3/feed/search?&expand=url&{cat_id}'
                    tasks.append(asyncio.ensure_future(get_json(client,url, params,cat_id)))
                    d = await asyncio.gather(*tasks)
                    for a in d:
                        save_json(a)
                    result.extend(get_data_from_json(a, category_id=cats.get(cat_id)))



        asyncio.run(main())

theand()
# save_excel(result)
# save_filter_json(result)
# save_data_to_db(result)
# logging.info(len(result))
end = time.time()
print(end - start)