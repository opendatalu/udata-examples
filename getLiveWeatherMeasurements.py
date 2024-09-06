import requests
API = 'https://data.public.lu/fr'

# the id of the resource you want to get
resource = '93c90cb8-4994-4be7-bcaa-cabe0e66ad9a'
filename = 'mf.pointtimeseriesobservation-hourly-live-asta.gml'

# download the resource and save it
print('Downloading: '+ filename)
s = requests.get('{}/datasets/r/{}'.format(API, resource))
s.raise_for_status()
with open(filename, 'wb') as f:
    f.write(s.content)
print('Downloaded!')

