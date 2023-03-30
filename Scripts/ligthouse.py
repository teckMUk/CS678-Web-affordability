import requests
import os

def get_lighthouse_score(url):
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    res = requests.get(base_url + 'https://www.'+url)
    
    return res.json()

sites_dir = os.path.join(os.getcwd(), 'sites')
files = os.listdir(sites_dir)

URLs = [x.replace('.xml', '') for x in files if x.endswith('.xml')]

print(get_lighthouse_score(URLs[0]))