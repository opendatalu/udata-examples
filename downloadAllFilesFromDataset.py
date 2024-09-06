import requests, urllib.parse, os.path
API = 'https://data.public.lu/api/1'

# the id of the Dataset you want to get
dataset = 'cour-de-cassation'

# get all metadata from the dataset
r = requests.get('{}/datasets/{}/'.format(API, dataset))
r.raise_for_status()

# extract the information about the resources (= files)
resources = r.json()['resources']

# download the resources and save them
if resources:
    for i in resources:
        print('Downloading: '+ i['title'])
        s = requests.get(i['url'])
        s.raise_for_status()
        filename = os.path.basename(urllib.parse.urlparse(i['url']).path)
        with open(filename, 'wb') as f:
            f.write(s.content)
        print('Downloaded!')