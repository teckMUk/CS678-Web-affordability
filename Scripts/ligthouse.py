import requests
import os
import json
from tqdm import tqdm
from time import sleep

def get_lighthouse_score(url):
    
    apiKey =  "&key=AIzaSyDjUSABsl8wRbIInM_xnQNnimhdPbYoip4"
    base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='
    url = base_url + 'https://www.'+url+apiKey
    res = requests.get(url)
    
    return res.json()

sites_dir = os.path.join(os.getcwd(), 'sites')

files = os.listdir(sites_dir)

URLs = [x.replace('.xml', '') for x in files if x.endswith('.xml')]

newdict = {}

with open('Scripts\lighthouse_done.txt', 'r') as f:
    done = f.read().splitlines()
    URLs = [x for x in URLs if x not in done]

for i in tqdm(range(len(URLs))):
    newdict[URLs[i]] = get_lighthouse_score(URLs[i])

    with open('.\Scripts\lighthouse_results\\'+ URLs[i]+'.json', 'w+') as f:
        json.dump(newdict[URLs[i]], f)
        sleep(1)

    # append the URL to the lighthouse_done.txt file
    with open('Scripts\lighthouse_done.txt', 'a') as f:
        f.write(URLs[i] + '\n')