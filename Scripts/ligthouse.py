import requests

def get_lighthouse_score(url):
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    res = requests.get(base_url + url)
    return res.json()['lighthouseResult']

# print(res)

# print(res.json())