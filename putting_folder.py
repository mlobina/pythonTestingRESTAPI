import requests

tokenY = ''


def put_folder(folder_name):
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources/',
                            headers={'authorization': tokenY},
                            params={'path': folder_name})
    print(f'status_code - "{response.status_code}"')
    return response.ok

