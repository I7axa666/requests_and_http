import requests

class Steck:
    def get_questions(self):
        url = 'https://api.stackexchange.com/2.3/questions/'
        params = {'fromdate': 1667941200, 'order': 'desc', 'sort': 'activity', 'tagged': 'python', 'site': 'stackoverflow'}
        response = requests.get(url, params=params).json()
        for item in response['items']:
            print(item['title'])


if __name__ == '__main__':
    st = Steck()
    st.get_questions()
