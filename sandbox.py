import nltk
from geotext import GeoText
import googlemaps

import config
import sample_data

gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)

SEARCH_RADIUS = 10000 # in meters
HOME_CITY = 'Boston'

'''
Get all emails
'''

'''
Process Resume
    Get skills
    Get location
'''

'''
Process Email
    Get skills
    Get location
    Match Email address to company
    Check Email against white list
'''



from nltk.tokenize import word_tokenize
pos = nltk.pos_tag(word_tokenize(sampleData.email1))
# print(pos)

proper_nouns = list(filter(lambda x: x[1] == 'NNP' or x[1] == 'NNS', pos))

places = GeoText(sampleData.email2)
print(places.cities)

for p in places.cities:
    try:
        my_dist = gmaps.distance_matrix(HOME_CITY, p)['rows'][0]['elements'][0]['distance']['value']
        lol_factor = (my_dist - SEARCH_RADIUS) / SEARCH_RADIUS * 100
        print('{} - {} - l{}l'.format(p, lol_factor, 'o' + int(lol_factor / 100) * 'o'))
    except KeyError:
        continue