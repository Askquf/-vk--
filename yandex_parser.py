import datetime
import requests
import time
import pyprind


class YandexParser:
    url = 'https://cloud-api.yandex.net/'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Authorization': self.token}

    def post_photos(self, photos):
        method_url = self.url + 'v1/disk/resources'
        folder_name = self.get_folder_name()
        response = requests.put(url=method_url, headers=self.get_headers(), params={'path': f'/{folder_name}'})
        method_url = self.url + 'v1/disk/resources/upload'
        #with Bar('Счетчик', max=len(photos)) as bar:
        bar = pyprind.ProgBar(len(photos))
        for photo in photos:
            response = requests.post(url=method_url, headers=self.get_headers(),
                                     params={'path': f'/{folder_name}/{photo["photo_likes"]}.jpg',
                                             'url': photo['size_inf'][1]})
            time.sleep(0.34)
            bar.update()
        return response.status_code

    def get_folder_name(self):
        return f'{str(datetime.date.today())}-' \
               f'{str(datetime.datetime.today().hour)}' \
               f'-{str(datetime.datetime.today().minute)}' \
               f'-{str(datetime.datetime.today().second)}'