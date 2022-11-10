import requests

def superhero_api_read(url='https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'):
    response = requests.get(url).json()
    s_h_dict = {}
    for item in response:
        s_h_dict[item['name']] = item['powerstats']['intelligence']
    return(s_h_dict)

def who_the_smartest(some_list):
    s_h_dict = superhero_api_read()
    int = 0
    name = ''
    for item in some_list:
        intelligence = s_h_dict[item]
        if intelligence > int:
            name = item
    print(f'Самый умный супергерой: {name}')

who_the_smartest(['Hulk', 'Captain America', 'Thanos'])