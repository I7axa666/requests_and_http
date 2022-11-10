import requests
from settings import TOKEN

class YaUploader:

    base_host = 'https://cloud-api.yandex.net'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return{
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        uri = '/v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': '/Netology/HW_requests.txt', 'overwrite': True}
        response_get = requests.get(request_url, headers=self.get_headers(), params=params).json()['href']
        response_put = requests.put(response_get, data=open(file_path, 'rb'), headers=self.get_headers())



if __name__ == '__main__':
    path_to_file = r'C:\Users\pvsol\Desktop\Для ДЗ с requests.txt'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)