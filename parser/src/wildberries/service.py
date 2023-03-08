import time

import requests


async def get_wildberries_post_data_by_url(url: str) -> list[str | list[str]]:
    post_id = url.split('/')[4]

    link = f'https://wbx-content-v2.wbstatic.net/ru/{post_id}.json'
    r = requests.get(link)
    createdAt = time.time()
    data = r.json()

    status = r.status_code
    name = data['imt_name']
    description = data['description']
    category = data['subj_root_name']

    option = data['options']
    options = []
    for opt in option:
        options.append(str(f'''{opt['name']}: {opt['value']}'''))

    size = data['sizes_table']['values']
    sizes = []
    for siz in size:
        sizes.append(str(f'''{siz['tech_size']}'''))

    brand = data['selling']['brand_name']

    media = data['media']['photo_count']

    special_id = str(post_id)
    a = []

    for i in range(len(special_id)):
        a.append(special_id[i])

    a[-1] = 0
    a[-2] = 0
    a[-3] = 0
    a[-4] = 0

    special_id = ''
    for i in range(len(a)):
        special_id += str(a[i])

    photos = []
    for i in range(media):
        # photos.append(f'https://images.wbstatic.net/c246x328/new/{special_id}/{post_id}-{i + 1}.jpg')
        photos.append(f'https://images.wbstatic.net/big/new/{special_id}/{post_id}-{i + 1}.jpg')

    r = requests.get(f'https://card.wb.ru/cards/detail?spp=0&regions=68,64,83,4,38,80,33,70,82,86,30,69,22,66,31,40,1,48&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,7,3,6,5,18,21&dest=-1216601,-337422,-1114902,-1198055&nm={post_id}')
    data = r.json()
    price = data['data']['products'][0]['priceU']
    salePrice = data['data']['products'][0]['salePriceU']
    color = []
    for i in range(len(data['data']['products'][0]['colors'])):
        color.append(data['data']['products'][0]['colors'][i]['name'])

    updatedAt = time.time()

    link = f'https://www.wildberries.ru/catalog/{post_id}/detail.aspx?targetUrl=MI'

    price = float(price) // 100
    salePrice = float(salePrice) // 100

    return {
        'post_id': post_id,
        'created_at': createdAt,
        'updated_at': updatedAt,
        'post_url': link,
        'name': name,
        'description': description,
        'price': price,
        'sale_price': salePrice,
        'category': category,
        'photos': photos,
        'options': options,
        'colors': color,
        'sizes': sizes,
        'brand': brand
    }