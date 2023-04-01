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

    def get_user_photos(self, photos_number, album):
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

# 474796397
#	https://login.vk.com/?act=grant_access&client_id=51586655&settings=65536&response_type=token&group_ids=&token_type=0&v=&display=page&ip_h=3532ce545631ee3c17&hash=1679309835_f103b5589abe1105e0&https=1&state=&redirect_uri=&cancel=1#error=access_denied&error_reason=user_denied&error_description=User%20denied%20your%20request