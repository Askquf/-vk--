from tokens import vk_token, yandex_token
from vk_parser import VkParser
from yandex_parser import YandexParser
import json

def vk_check(response):
    if 'error' in response:
        print(response['error']['error_msg'])
        return False
    else:
        return True

def json_dump(data):
    file_name = 'file_info.json'
    with open(file_name, 'w') as f:
        json.dump([{'file_name': f'{photo["photo_likes"]}.jpg', 'size': photo["size_inf"][0]} for photo in data], f)

def main():
    id = int(input('Введите айди пользователя:\n'))
    photos_number = int(input('Введите количество фотографий:\n'))
    album = input('Введите альбом:\n')
    vk = VkParser(vk_token, id)
    response = vk.get_user_photos(photos_number, album)
    if vk_check(response):
        yandex = YandexParser(yandex_token)
        yandex_result = yandex.post_photos(response)
        if (yandex_result >= 400):
            print('Возникла ошибка при сохранении файлов на Яндекс-диск')
        else:
            json_dump(response)

if __name__ == '__main__':
    main()