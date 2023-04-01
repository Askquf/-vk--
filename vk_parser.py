import requests

class VkParser:
    url = 'https://api.vk.com/method/'
    photo_size = 'z'
    def __init__(self, token, user_id, version = '5.131'):
        self.token = token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_user_info(self):
        method_url = self.url + 'users.get'
        response = requests.get(method_url, params=self.params)
        return response.json()

    def get_user_photos(self, album, photos_number=5):
        method_url = self.url + 'photos.get'
        response = requests.get(method_url, params={**self.params, \
                                                    'owner_id':  self.id, \
                                                    'album_id': album, 'extended': 1, \
                                                    'count': photos_number, 'rev': 1}).json()
        result = self.get_photos_url_likes(response['response']['items']) if 'error' not in response else response
        return result

    def get_photos_url_likes(self, response):
        return [{'size_inf': list(sorted(photo['sizes'], key=lambda size: size['height'] * size['width'], reverse=True)[0].values())[1:4:2], \
                 'photo_likes': photo['likes']['count']} for photo in response]